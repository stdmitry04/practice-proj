from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from uuid import UUID
from typing import List
import json

from app.database import get_db
from app.models.language import Language
from app.models.roadmap_node import RoadmapNode
from app.models.roadmap_problem import RoadmapProblem, DifficultyEnum as DBDifficultyEnum, StatusEnum as DBStatusEnum, LevelEnum as DBLevelEnum
from app.schemas.roadmap import (
    RoadmapNodeSchema,
    RoadmapNodeWithProgress,
    RoadmapProblemSchema,
    RoadmapProblemSummary,
    GenerateProblemRequest,
    SubmitCodeRequest,
    SubmitCodeResponse,
    NodeProgressResponse,
    ModuleCompletionStatus,
)
from app.services.roadmap_generator import generate_roadmap_problem
from app.services.code_runner import run_code

router = APIRouter()


def parse_theory(theory):
    """Parse theory field if it's a JSON string, otherwise return as-is."""
    if theory is None:
        return None
    if isinstance(theory, str):
        try:
            return json.loads(theory)
        except (json.JSONDecodeError, ValueError):
            return None
    return theory


@router.get("/languages/{language_id}/roadmap", response_model=List[RoadmapNodeWithProgress])
async def get_language_roadmap(language_id: UUID, db: Session = Depends(get_db)):
    """Get all roadmap nodes for a language with progress information."""
    language = db.query(Language).filter(Language.id == language_id).first()
    if not language:
        raise HTTPException(status_code=404, detail="Language not found")

    nodes = db.query(RoadmapNode).filter(RoadmapNode.language_id == language_id).all()

    result = []
    for node in nodes:
        # Get problem counts by difficulty and status
        problems = db.query(RoadmapProblem).filter(RoadmapProblem.node_id == node.id).all()

        easy_count = sum(1 for p in problems if p.difficulty == DBDifficultyEnum.easy)
        medium_count = sum(1 for p in problems if p.difficulty == DBDifficultyEnum.medium)
        hard_count = sum(1 for p in problems if p.difficulty == DBDifficultyEnum.hard)
        easy_solved = sum(1 for p in problems if p.difficulty == DBDifficultyEnum.easy and p.status == DBStatusEnum.solved)
        medium_solved = sum(1 for p in problems if p.difficulty == DBDifficultyEnum.medium and p.status == DBStatusEnum.solved)
        hard_solved = sum(1 for p in problems if p.difficulty == DBDifficultyEnum.hard and p.status == DBStatusEnum.solved)

        node_data = RoadmapNodeWithProgress(
            id=node.id,
            language_id=node.language_id,
            name=node.name,
            slug=node.slug,
            description=node.description,
            position_x=node.position_x,
            position_y=node.position_y,
            parent_id=node.parent_id,
            order_index=node.order_index,
            concept_keywords=node.concept_keywords,
            topic=node.topic,
            node_type=node.node_type,
            module_order=node.module_order,
            theory=parse_theory(node.theory),
            created_at=node.created_at,
            easy_count=easy_count,
            medium_count=medium_count,
            hard_count=hard_count,
            easy_solved=easy_solved,
            medium_solved=medium_solved,
            hard_solved=hard_solved,
        )
        result.append(node_data)

    return result


@router.get("/nodes/{node_id}", response_model=RoadmapNodeSchema)
async def get_node(node_id: UUID, db: Session = Depends(get_db)):
    """Get a single roadmap node by ID."""
    node = db.query(RoadmapNode).filter(RoadmapNode.id == node_id).first()
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")
    return node


@router.get("/nodes/{node_id}/problems", response_model=List[RoadmapProblemSummary])
async def get_node_problems(node_id: UUID, db: Session = Depends(get_db)):
    """Get all problems for a roadmap node."""
    node = db.query(RoadmapNode).filter(RoadmapNode.id == node_id).first()
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")

    problems = db.query(RoadmapProblem).filter(RoadmapProblem.node_id == node_id).order_by(RoadmapProblem.created_at.desc()).all()
    return problems


@router.post("/nodes/{node_id}/generate", response_model=RoadmapProblemSchema)
async def generate_problem(node_id: UUID, request: GenerateProblemRequest, db: Session = Depends(get_db)):
    """Generate a new problem for a roadmap node."""
    node = db.query(RoadmapNode).filter(RoadmapNode.id == node_id).first()
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")

    # Get existing problems to pass to the generator for deduplication
    existing_problems = db.query(RoadmapProblem.title, RoadmapProblem.condensed_description).filter(
        RoadmapProblem.node_id == node_id
    ).all()
    existing_problems = [
        {"title": p.title, "condensed_description": p.condensed_description}
        for p in existing_problems
    ]

    try:
        problem_data = await generate_roadmap_problem(
            concept_name=node.name,
            keywords=node.concept_keywords or [],
            difficulty=request.difficulty.value,
            level=request.level.value,
            existing_problems=existing_problems,
        )

        problem = RoadmapProblem(
            node_id=node_id,
            difficulty=DBDifficultyEnum(request.difficulty.value),
            level=DBLevelEnum(request.level.value),
            status=DBStatusEnum.unsolved,
            title=problem_data["title"],
            description=problem_data["description"],
            template_code=problem_data["template_code"],
            solution_code=problem_data["solution_code"],
            test_cases=problem_data["test_cases"],
            hints=problem_data.get("hints"),
            description_hash=problem_data["description_hash"],
            condensed_description=problem_data["condensed_description"],
        )

        db.add(problem)
        db.commit()
        db.refresh(problem)
        return problem

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate problem: {str(e)}")


@router.delete("/problems/{problem_id}")
async def delete_problem(problem_id: UUID, db: Session = Depends(get_db)):
    """Delete a roadmap problem."""
    problem = db.query(RoadmapProblem).filter(RoadmapProblem.id == problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")

    db.delete(problem)
    db.commit()
    return {"status": "deleted"}


@router.get("/problems/{problem_id}", response_model=RoadmapProblemSchema)
async def get_problem(problem_id: UUID, db: Session = Depends(get_db)):
    """Get a single problem by ID."""
    problem = db.query(RoadmapProblem).filter(RoadmapProblem.id == problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    return problem


@router.post("/problems/{problem_id}/submit", response_model=SubmitCodeResponse)
async def submit_problem(problem_id: UUID, request: SubmitCodeRequest, db: Session = Depends(get_db)):
    """Submit code for a roadmap problem."""
    problem = db.query(RoadmapProblem).filter(RoadmapProblem.id == problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")

    # Get the language from the node
    node = problem.node
    language_slug = node.language.slug

    result = await run_code(
        language=language_slug,
        code=request.code,
        test_cases=problem.test_cases,
    )

    # Update problem status based on result
    if result.passed:
        problem.status = DBStatusEnum.solved
    elif problem.status == DBStatusEnum.unsolved:
        problem.status = DBStatusEnum.attempted

    db.commit()

    return SubmitCodeResponse(
        passed=result.passed,
        results=[{"name": r.name, "passed": r.passed, "expected": r.expected, "actual": r.actual, "error": r.error} for r in result.results],
        compile_error=result.compile_error,
        runtime_error=result.runtime_error,
    )


@router.get("/nodes/{node_id}/progress", response_model=NodeProgressResponse)
async def get_node_progress(node_id: UUID, db: Session = Depends(get_db)):
    """Get solved counts by difficulty for a node."""
    node = db.query(RoadmapNode).filter(RoadmapNode.id == node_id).first()
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")

    problems = db.query(RoadmapProblem).filter(RoadmapProblem.node_id == node_id).all()

    return NodeProgressResponse(
        easy_total=sum(1 for p in problems if p.difficulty == DBDifficultyEnum.easy),
        easy_solved=sum(1 for p in problems if p.difficulty == DBDifficultyEnum.easy and p.status == DBStatusEnum.solved),
        medium_total=sum(1 for p in problems if p.difficulty == DBDifficultyEnum.medium),
        medium_solved=sum(1 for p in problems if p.difficulty == DBDifficultyEnum.medium and p.status == DBStatusEnum.solved),
        hard_total=sum(1 for p in problems if p.difficulty == DBDifficultyEnum.hard),
        hard_solved=sum(1 for p in problems if p.difficulty == DBDifficultyEnum.hard and p.status == DBStatusEnum.solved),
    )


@router.get("/languages/{language_id}/modules/completion", response_model=List[ModuleCompletionStatus])
async def get_module_completion(language_id: UUID, db: Session = Depends(get_db)):
    """Get completion status for all modules in a language."""
    language = db.query(Language).filter(Language.id == language_id).first()
    if not language:
        raise HTTPException(status_code=404, detail="Language not found")

    # Get all module test nodes ordered by module_order
    module_nodes = (
        db.query(RoadmapNode)
        .filter(
            RoadmapNode.language_id == language_id,
            RoadmapNode.node_type == "module_test"
        )
        .order_by(RoadmapNode.module_order)
        .all()
    )

    result = []
    for module_node in module_nodes:
        # Get all problems for this module test node
        problems = db.query(RoadmapProblem).filter(RoadmapProblem.node_id == module_node.id).all()

        # Count hard problems solved
        hard_solved = sum(
            1 for p in problems
            if p.difficulty == DBDifficultyEnum.hard and p.status == DBStatusEnum.solved
        )

        # Get all concept nodes in this module
        concept_nodes = (
            db.query(RoadmapNode)
            .filter(
                RoadmapNode.language_id == language_id,
                RoadmapNode.topic == module_node.topic,
                RoadmapNode.node_type == "concept"
            )
            .all()
        )

        # Count completed concept nodes (at least one problem solved)
        nodes_complete = 0
        for node in concept_nodes:
            node_problems = db.query(RoadmapProblem).filter(
                RoadmapProblem.node_id == node.id,
                RoadmapProblem.status == DBStatusEnum.solved
            ).count()
            if node_problems > 0:
                nodes_complete += 1

        result.append(
            ModuleCompletionStatus(
                module_name=module_node.topic or "",
                module_order=module_node.module_order or 0,
                is_complete=hard_solved >= 1,
                nodes_complete=nodes_complete,
                nodes_total=len(concept_nodes),
                hard_problems_solved=hard_solved,
            )
        )

    return result


@router.post("/nodes/{node_id}/generate-module-test", response_model=RoadmapProblemSchema)
async def generate_module_test(node_id: UUID, db: Session = Depends(get_db)):
    """Generate a comprehensive module test problem combining all module concepts."""
    node = db.query(RoadmapNode).filter(RoadmapNode.id == node_id).first()
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")

    if node.node_type != "module_test":
        raise HTTPException(status_code=400, detail="This endpoint is only for module test nodes")

    # Get all concept nodes in this module
    concept_nodes = (
        db.query(RoadmapNode)
        .filter(
            RoadmapNode.language_id == node.language_id,
            RoadmapNode.topic == node.topic,
            RoadmapNode.node_type == "concept"
        )
        .all()
    )

    # Collect all keywords from concept nodes
    all_keywords = []
    for concept_node in concept_nodes:
        if concept_node.concept_keywords:
            all_keywords.extend(concept_node.concept_keywords)

    # Get existing problems for deduplication
    existing_problems = db.query(RoadmapProblem.title, RoadmapProblem.condensed_description).filter(
        RoadmapProblem.node_id == node_id
    ).all()
    existing_problems = [
        {"title": p.title, "condensed_description": p.condensed_description}
        for p in existing_problems
    ]

    try:
        from app.services.roadmap_generator import generate_module_test_problem

        problem_data = await generate_module_test_problem(
            module_name=node.topic or "module",
            keywords=all_keywords,
            existing_problems=existing_problems,
        )

        problem = RoadmapProblem(
            node_id=node_id,
            difficulty=DBDifficultyEnum.hard,
            status=DBStatusEnum.unsolved,
            title=problem_data["title"],
            description=problem_data["description"],
            template_code=problem_data["template_code"],
            solution_code=problem_data["solution_code"],
            test_cases=problem_data["test_cases"],
            hints=problem_data.get("hints"),
            description_hash=problem_data["description_hash"],
            condensed_description=problem_data["condensed_description"],
        )

        db.add(problem)
        db.commit()
        db.refresh(problem)
        return problem

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate module test: {str(e)}")

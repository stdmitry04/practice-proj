from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.models.topic import Topic
from app.models.exercise import Exercise
from app.schemas.exercise import (
    ExerciseSchema,
    ExerciseGenerateRequest,
    ExerciseSubmitRequest,
    ExerciseSubmitResponse,
)
from app.services.ai_generator import generate_exercise
from app.services.code_runner import run_code

router = APIRouter()


@router.post("/generate", response_model=ExerciseSchema)
async def generate_new_exercise(
    request: ExerciseGenerateRequest,
    db: Session = Depends(get_db)
):
    topic = db.query(Topic).filter(Topic.id == request.topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    exercise_data = await generate_exercise(
        language=topic.language.name,
        topic=topic.name,
        difficulty=topic.difficulty
    )

    exercise = Exercise(
        topic_id=topic.id,
        title=exercise_data["title"],
        description=exercise_data["description"],
        template_code=exercise_data["template_code"],
        solution_code=exercise_data["solution_code"],
        test_cases=exercise_data["test_cases"],
        hints=exercise_data.get("hints", [])
    )

    db.add(exercise)
    db.commit()
    db.refresh(exercise)

    return exercise


@router.get("/{exercise_id}", response_model=ExerciseSchema)
async def get_exercise(exercise_id: UUID, db: Session = Depends(get_db)):
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise


@router.post("/{exercise_id}/submit", response_model=ExerciseSubmitResponse)
async def submit_exercise(
    exercise_id: UUID,
    request: ExerciseSubmitRequest,
    db: Session = Depends(get_db)
):
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")

    language_slug = exercise.topic.language.slug

    result = await run_code(
        language=language_slug,
        code=request.code,
        test_cases=exercise.test_cases
    )

    return result

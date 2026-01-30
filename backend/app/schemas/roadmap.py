from pydantic import BaseModel, field_validator
from uuid import UUID
from datetime import datetime
from typing import List, Any
from enum import Enum
import json


class DifficultyEnum(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"


class LevelEnum(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"
    cheatsheet = "cheatsheet"


class StatusEnum(str, Enum):
    unsolved = "unsolved"
    attempted = "attempted"
    solved = "solved"


class NodeTypeEnum(str, Enum):
    concept = "concept"
    module_test = "module_test"


# Node schemas
class RoadmapNodeBase(BaseModel):
    name: str
    slug: str
    description: str | None = None
    position_x: int = 0
    position_y: int = 0
    parent_id: UUID | None = None
    order_index: int = 0
    concept_keywords: List[str] | None = None
    topic: str | None = None  # For visual grouping (e.g., 'fundamentals', 'oop', 'web')
    node_type: NodeTypeEnum = NodeTypeEnum.concept
    module_order: int | None = None
    theory: dict[str, str] | None = None  # {"beginner": "...", "intermediate": "...", "advanced": "...", "cheatsheet": "..."}

    @field_validator('theory', mode='before')
    @classmethod
    def parse_theory(cls, v):
        """Parse theory field if it's a JSON string and fix escaped newlines."""
        if v is None:
            return None
        if isinstance(v, str):
            try:
                parsed = json.loads(v)
            except (json.JSONDecodeError, ValueError):
                return None
        else:
            parsed = v

        # Convert literal \n strings to actual newlines for markdown rendering
        if isinstance(parsed, dict):
            for key in parsed:
                if isinstance(parsed[key], str):
                    parsed[key] = parsed[key].replace('\\n', '\n')
        return parsed


class RoadmapNodeCreate(RoadmapNodeBase):
    language_id: UUID


class RoadmapNodeSchema(RoadmapNodeBase):
    id: UUID
    language_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True


class RoadmapNodeWithProgress(RoadmapNodeSchema):
    easy_count: int = 0
    medium_count: int = 0
    hard_count: int = 0
    easy_solved: int = 0
    medium_solved: int = 0
    hard_solved: int = 0
    is_locked: bool = False


class ModuleCompletionStatus(BaseModel):
    module_name: str
    module_order: int
    is_complete: bool
    nodes_complete: int
    nodes_total: int
    hard_problems_solved: int

    class Config:
        from_attributes = True


# Problem schemas
class RoadmapProblemBase(BaseModel):
    title: str
    description: str
    template_code: str
    solution_code: str
    test_cases: dict[str, Any]
    hints: List[str] | None = None
    condensed_description: str


class RoadmapProblemCreate(RoadmapProblemBase):
    node_id: UUID
    difficulty: DifficultyEnum
    level: LevelEnum
    description_hash: str


class RoadmapProblemSchema(RoadmapProblemBase):
    id: UUID
    node_id: UUID
    difficulty: DifficultyEnum
    level: LevelEnum
    status: StatusEnum
    description_hash: str
    created_at: datetime

    class Config:
        from_attributes = True


class RoadmapProblemSummary(BaseModel):
    id: UUID
    title: str
    difficulty: DifficultyEnum
    level: LevelEnum
    status: StatusEnum
    created_at: datetime

    class Config:
        from_attributes = True


# Request/Response schemas
class GenerateProblemRequest(BaseModel):
    difficulty: DifficultyEnum
    level: LevelEnum = LevelEnum.beginner


class SubmitCodeRequest(BaseModel):
    code: str


class SubmitCodeResponse(BaseModel):
    passed: bool
    results: List[dict[str, Any]]
    compile_error: str | None = None
    runtime_error: str | None = None


class NodeProgressResponse(BaseModel):
    easy_total: int
    easy_solved: int
    medium_total: int
    medium_solved: int
    hard_total: int
    hard_solved: int

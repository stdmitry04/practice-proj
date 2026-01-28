from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List, Any
from enum import Enum


class DifficultyEnum(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"


class StatusEnum(str, Enum):
    unsolved = "unsolved"
    attempted = "attempted"
    solved = "solved"


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
    description_hash: str


class RoadmapProblemSchema(RoadmapProblemBase):
    id: UUID
    node_id: UUID
    difficulty: DifficultyEnum
    status: StatusEnum
    description_hash: str
    created_at: datetime

    class Config:
        from_attributes = True


class RoadmapProblemSummary(BaseModel):
    id: UUID
    title: str
    difficulty: DifficultyEnum
    status: StatusEnum
    created_at: datetime

    class Config:
        from_attributes = True


# Request/Response schemas
class GenerateProblemRequest(BaseModel):
    difficulty: DifficultyEnum


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

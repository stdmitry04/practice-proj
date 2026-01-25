from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List, Any


class TestCase(BaseModel):
    name: str
    input: str
    expected_output: str
    hidden: bool = False


class TestCasesConfig(BaseModel):
    test_cases: List[TestCase]
    entry_point: str | None = None
    timeout_ms: int = 5000


class ExerciseSchema(BaseModel):
    id: UUID
    topic_id: UUID
    title: str
    description: str
    template_code: str
    solution_code: str
    test_cases: TestCasesConfig | dict[str, Any]
    hints: List[str] | None
    created_at: datetime

    class Config:
        from_attributes = True


class ExerciseGenerateRequest(BaseModel):
    topic_id: UUID


class ExerciseSubmitRequest(BaseModel):
    code: str


class TestCaseResult(BaseModel):
    name: str
    passed: bool
    expected: str | None = None
    actual: str | None = None
    error: str | None = None


class ExerciseSubmitResponse(BaseModel):
    passed: bool
    results: List[TestCaseResult]
    compile_error: str | None = None
    runtime_error: str | None = None

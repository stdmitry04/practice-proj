import httpx
from typing import Any

from app.config import get_settings
from app.schemas.exercise import ExerciseSubmitResponse, TestCaseResult

settings = get_settings()

WORKER_URLS = {
    "python": settings.python_worker_url,
    "javascript": settings.javascript_worker_url,
    "cpp": settings.cpp_worker_url,
    "react": settings.react_worker_url,
}


async def run_code(language: str, code: str, test_cases: dict[str, Any]) -> ExerciseSubmitResponse:
    worker_url = WORKER_URLS.get(language)
    if not worker_url:
        return ExerciseSubmitResponse(
            passed=False,
            results=[],
            runtime_error=f"Unknown language: {language}"
        )

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{worker_url}/execute",
                json={
                    "code": code,
                    "test_cases": test_cases.get("test_cases", []),
                    "entry_point": test_cases.get("entry_point"),
                    "timeout_ms": test_cases.get("timeout_ms", 5000)
                }
            )

            if response.status_code != 200:
                return ExerciseSubmitResponse(
                    passed=False,
                    results=[],
                    runtime_error=f"Worker error: {response.text}"
                )

            data = response.json()

            results = [
                TestCaseResult(
                    name=r.get("name", ""),
                    passed=r.get("passed", False),
                    expected=r.get("expected"),
                    actual=r.get("actual"),
                    error=r.get("error")
                )
                for r in data.get("results", [])
            ]

            all_passed = all(r.passed for r in results) and len(results) > 0

            return ExerciseSubmitResponse(
                passed=all_passed,
                results=results,
                compile_error=data.get("compile_error"),
                runtime_error=data.get("runtime_error")
            )

    except httpx.TimeoutException:
        return ExerciseSubmitResponse(
            passed=False,
            results=[],
            runtime_error="Code execution timed out"
        )
    except Exception as e:
        return ExerciseSubmitResponse(
            passed=False,
            results=[],
            runtime_error=str(e)
        )

import json
import hashlib
from openai import AsyncOpenAI
from typing import List

from app.config import get_settings

settings = get_settings()
client = AsyncOpenAI(api_key=settings.openai_api_key)


SYSTEM_PROMPT = """You are an expert Python instructor who creates practical coding exercises.
Focus on REAL-WORLD backend development, not algorithmic puzzles or leetcode-style problems.
Your exercises should teach Python language features as they're used in production code.
Always respond with valid JSON only, no markdown formatting."""

USER_PROMPT_TEMPLATE = """Generate a Python practice exercise for:
Concept: {concept_name}
Related Keywords: {keywords}
Difficulty: {difficulty}

IMPORTANT GUIDELINES:
- Focus on {concept_name} and how it's used in REAL backend/production code
- DO NOT create algorithmic puzzles, sorting problems, or leetcode-style challenges
- Create scenarios like: building APIs, working with databases, handling configurations,
  processing data, building utilities, error handling patterns, etc.

The exercise should:
1. Demonstrate practical usage of {concept_name}
2. Be something a developer might actually encounter at work
3. Include realistic input/output scenarios
4. Have clear requirements

Difficulty guidelines:
- easy: Simple usage, one main concept, straightforward implementation
- medium: Combining concepts, edge cases, some design decisions
- hard: Complex scenarios, multiple interacting parts, production-quality code expected
{existing_problems_section}
Respond with ONLY valid JSON in this exact format:
{{
  "title": "Practical title describing what to build",
  "description": "Full markdown description with:\n- What to build and why\n- Requirements\n- Example usage",
  "template_code": "Starter code with TODO comments marking where the student should write code",
  "solution_code": "Complete working solution",
  "test_cases": {{
    "test_cases": [
      {{
        "name": "descriptive_test_name",
        "input": "input value or function args as string",
        "expected_output": "expected output as string",
        "hidden": false
      }}
    ],
    "entry_point": "function_name_to_call",
    "timeout_ms": 5000
  }},
  "hints": ["First hint about approach", "Second hint about implementation", "Third hint about edge cases"],
  "condensed_description": "A 2-3 sentence summary of what this exercise tests"
}}

Make sure:
- Template code is syntactically valid Python
- Solution passes all test cases
- Test cases cover normal usage and edge cases
- Entry point matches the main function students should implement
"""


def generate_hash(condensed_description: str) -> str:
    """Generate SHA-256 hash of the condensed description for record keeping."""
    return hashlib.sha256(condensed_description.encode()).hexdigest()


def build_existing_problems_section(existing_problems: List[dict]) -> str:
    """Build the prompt section that lists existing problems to avoid."""
    if not existing_problems:
        return ""

    problems_list = "\n".join(
        f"- {p['title']}: {p['condensed_description']}"
        for p in existing_problems
    )

    return f"""
IMPORTANT - These problems already exist for this concept. Generate something DIFFERENT:
{problems_list}

Do NOT repeat or closely resemble any of the above problems. Create a unique exercise.
"""


async def generate_roadmap_problem(
    concept_name: str,
    keywords: List[str],
    difficulty: str,
    existing_problems: List[dict],
) -> dict:
    """Generate a new roadmap problem using AI.

    Args:
        concept_name: The main concept to focus on (e.g., "Decorators")
        keywords: Related keywords for context (e.g., ["functools.wraps", "closures"])
        difficulty: One of "easy", "medium", "hard"
        existing_problems: List of existing problems with 'title' and 'condensed_description'

    Returns:
        dict with problem data including description_hash
    """
    keywords_str = ", ".join(keywords) if keywords else "general usage"
    existing_section = build_existing_problems_section(existing_problems)

    prompt = USER_PROMPT_TEMPLATE.format(
        concept_name=concept_name,
        keywords=keywords_str,
        difficulty=difficulty,
        existing_problems_section=existing_section,
    )

    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=2500
    )

    content = response.choices[0].message.content

    # Clean up potential markdown formatting
    if content.startswith("```"):
        lines = content.split("\n")
        # Remove first and last lines if they're markdown markers
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        content = "\n".join(lines)

    problem_data = json.loads(content)

    # Validate required fields
    required_fields = ["title", "description", "template_code", "solution_code", "test_cases", "condensed_description"]
    for field in required_fields:
        if field not in problem_data:
            raise ValueError(f"Missing required field: {field}")

    # Generate hash for record keeping
    condensed = problem_data["condensed_description"]
    problem_data["description_hash"] = generate_hash(condensed)

    return problem_data

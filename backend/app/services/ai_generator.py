import json
from openai import AsyncOpenAI

from app.config import get_settings

settings = get_settings()
client = AsyncOpenAI(api_key=settings.openai_api_key)


SYSTEM_PROMPT = """You are a coding instructor who creates practice exercises.
You generate exercises in a specific JSON format.
Always respond with valid JSON only, no markdown formatting."""

USER_PROMPT_TEMPLATE = """Generate a practice exercise for:
Language: {language}
Topic: {topic}
Difficulty: {difficulty}

Create an exercise with:
1. A clear task description (2-3 paragraphs explaining what to build)
2. Requirements and constraints
3. Example input/output if applicable
4. Starter code template with TODO comments marking where the student should write code
5. Complete working solution
6. Test cases for verification
7. 2-3 progressive hints

Respond with ONLY valid JSON in this exact format:
{{
  "title": "Exercise title",
  "description": "Full markdown description with requirements and examples",
  "template_code": "Starter code with TODO comments",
  "solution_code": "Complete working solution",
  "test_cases": {{
    "test_cases": [
      {{
        "name": "test_case_name",
        "input": "input value or function args as string",
        "expected_output": "expected output as string",
        "hidden": false
      }}
    ],
    "entry_point": "function_name_to_call",
    "timeout_ms": 5000
  }},
  "hints": ["First hint", "Second hint", "Third hint"]
}}

For {language}:
- Template should be syntactically valid and runnable
- Solution must pass all test cases
- Test cases should cover edge cases
- Entry point should be the main function name students implement
"""


async def generate_exercise(language: str, topic: str, difficulty: str) -> dict:
    prompt = USER_PROMPT_TEMPLATE.format(
        language=language,
        topic=topic,
        difficulty=difficulty
    )

    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2000
    )

    content = response.choices[0].message.content

    # Clean up potential markdown formatting
    if content.startswith("```"):
        lines = content.split("\n")
        content = "\n".join(lines[1:-1])

    exercise_data = json.loads(content)

    # Validate required fields
    required_fields = ["title", "description", "template_code", "solution_code", "test_cases"]
    for field in required_fields:
        if field not in exercise_data:
            raise ValueError(f"Missing required field: {field}")

    return exercise_data

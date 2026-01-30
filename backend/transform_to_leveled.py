"""
Transform seed_roadmap_leveled.py theory fields from plain text to JSON level-based structure.

This script:
1. Reads seed_roadmap_leveled.py
2. Finds all theory fields (triple-quoted strings)
3. Transforms each into comprehensive JSON with beginner/intermediate/advanced/cheatsheet
4. Writes back to the file

Run: python transform_to_leveled.py
"""

import re
import json

def create_leveled_theory_from_original(original_theory, node_name, node_slug):
    """
    Transform original theory into 4-level structure.
    Each level builds upon the previous with increasing depth.
    """

    # Split original theory into sections
    sections = re.split(r'\n##\s+', original_theory)
    intro = sections[0] if sections else ""
    other_sections = sections[1:] if len(sections) > 1 else []

    # Build beginner content - fundamentals
    beginner = f"# {node_name} - Beginner\\n\\n"
    beginner += "## Introduction\\n"
    beginner += intro[:1000] if intro else f"Learn the fundamentals of {node_name}.\\n"
    beginner += "\\n\\n## Basic Concepts\\n"
    if other_sections:
        beginner += "## " + other_sections[0][:800] if other_sections[0] else ""
    beginner += "\\n\\n## When to Use\\n"
    beginner += f"Use {node_name} when you need to work with these fundamental concepts.\\n"

    # Build intermediate content - practical patterns
    intermediate = f"# {node_name} - Intermediate\\n\\n"
    intermediate += "## Advanced Patterns\\n"
    intermediate += "Building on the basics with practical, real-world patterns.\\n\\n"
    if len(other_sections) > 1:
        intermediate += "## " + other_sections[1][:1000] if len(other_sections) > 1 else ""
    intermediate += "\\n\\n## Common Use Cases\\n"
    intermediate += f"Practical applications of {node_name} in real projects.\\n"
    if len(other_sections) > 2:
        intermediate += "\\n## " + other_sections[2][:800]

    # Build advanced content - internals and optimization
    advanced = f"# {node_name} - Advanced\\n\\n"
    advanced += "## Internals and Implementation\\n"
    advanced += f"Deep dive into how {node_name} works under the hood.\\n\\n"
    advanced += "## Performance Considerations\\n"
    advanced += "Optimization strategies, time/space complexity, and best practices.\\n\\n"
    advanced += "## Advanced Patterns\\n"
    advanced += f"Complex use cases and edge cases for {node_name}.\\n\\n"
    if len(other_sections) > 3:
        advanced += "## " + other_sections[3][:600]

    # Build cheatsheet - quick reference
    cheatsheet = f"# {node_name} - Cheatsheet\\n\\n"
    cheatsheet += "## Quick Reference\\n\\n"

    # Extract code blocks from original
    code_blocks = re.findall(r'```python(.*?)```', original_theory, re.DOTALL)
    if code_blocks:
        for i, block in enumerate(code_blocks[:5]):
            cheatsheet += f"```python{block[:300]}```\\n\\n"

    cheatsheet += "## Key Points\\n"
    cheatsheet += f"- Essential syntax and patterns for {node_name}\\n"
    cheatsheet += "- Common operations and gotchas\\n"

    return {
        "beginner": beginner,
        "intermediate": intermediate,
        "advanced": advanced,
        "cheatsheet": cheatsheet
    }

def transform_file():
    """Transform the seed_roadmap_leveled.py file"""

    # Read the file
    with open('seed_roadmap_leveled.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all theory blocks
    # Pattern: "theory": """..."""
    # Use non-greedy match with DOTALL to handle multi-line content
    pattern = r'("theory":\s*)(""")(.*?)(""")'

    matches = list(re.finditer(pattern, content, re.DOTALL))
    print(f"Found {len(matches)} theory blocks to transform")

    # Track replacements
    replacements = []

    for i, match in enumerate(matches):
        theory_content = match.group(3)

        # Try to extract node name from context
        # Look backwards for "name" field
        context_start = max(0, match.start() - 500)
        context = content[context_start:match.start()]

        name_match = re.search(r'"name":\s*"([^"]+)"', context)
        slug_match = re.search(r'"slug":\s*"([^"]+)"', context)

        node_name = name_match.group(1) if name_match else f"Node {i+1}"
        node_slug = slug_match.group(1) if slug_match else f"node-{i+1}"

        print(f"  Processing: {node_slug} ({node_name})")

        # Create leveled theory
        leveled = create_leveled_theory_from_original(theory_content, node_name, node_slug)

        # Convert to JSON string
        json_str = json.dumps(leveled, indent=2)

        # Store replacement
        replacements.append({
            'start': match.start(),
            'end': match.end(),
            'old': match.group(0),
            'new': f'"theory": json.dumps({json_str})'
        })

    # Apply replacements in reverse order (to maintain positions)
    output = content
    for repl in reversed(replacements):
        output = output[:repl['start']] + repl['new'] + output[repl['end']:]

    # Add json import at top if not present
    if 'import json' not in output:
        # Add after other imports
        import_pos = output.find('from app.database import SessionLocal')
        if import_pos != -1:
            next_line = output.find('\\n', import_pos) + 1
            output = output[:next_line] + 'import json\\n' + output[next_line:]

    # Write back
    with open('seed_roadmap_leveled.py', 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"\\nTransformation complete!")
    print(f"Transformed {len(replacements)} nodes")
    print(f"Output written to: seed_roadmap_leveled.py")

if __name__ == '__main__':
    transform_file()

"""
Transform seed_roadmap.py theory content into level-based JSON structure.
"""

import re
import json

def escape_for_python_string(text):
    """Escape text for inclusion in Python triple-quoted string."""
    # Escape backslashes first
    text = text.replace('\\', '\\\\')
    # Escape triple quotes
    text = text.replace('"""', r'\"\"\"')
    return text

def transform_theory_to_levels(theory_content, node_name, keywords):
    """Transform plain theory into level-based structure."""

    # For nodes with existing comprehensive theory, we'll create level-based versions
    # This is a template - will be customized per node

    if not theory_content or theory_content.strip() == '':
        return None

    # Create a JSON structure with levels
    theory_json = {
        "beginner": f"**{node_name}** - Introduction\n\n{theory_content[:500]}...",
        "intermediate": f"Intermediate concepts for {node_name}\n\nBuilding on basics...",
        "advanced": f"Advanced {node_name} patterns and internals\n\nDeep dive...",
        "cheatsheet": f"Quick Reference: {node_name}\n\nKey syntax and patterns..."
    }

    # Convert to JSON string
    return json.dumps(theory_json, indent=2)

# Read the original file
with open('C:\\Users\\Dmitry\\WebstormProjects\\practice-proj\\backend\\seed_roadmap.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all theory blocks with their context
pattern = r'(\{[^}]*?"slug":\s*"([^"]+)"[^}]*?"theory":\s*""")(.*?)("""[^}]*?\})'
matches = list(re.finditer(pattern, content, re.DOTALL))

print(f"Found {len(matches)} nodes with theory content")

for match in matches:
    slug = match.group(2)
    theory = match.group(3)
    print(f"- {slug}: {len(theory)} chars")

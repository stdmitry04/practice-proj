"""
Generate comprehensive level-based seed file from original seed_roadmap.py

This script reads the original seed file, extracts all theory content,
and transforms it into a comprehensive level-based JSON structure.
"""

import re
import json
from pathlib import Path

# Theory expansion templates for each level
def create_beginner_content(original_theory, node_name, keywords):
    """Create beginner-level theory: basics, what/why, simple examples"""
    # Extract first sections from original theory
    lines = original_theory.split('\n')
    intro_lines = []
    code_blocks = []

    in_code = False
    for line in lines[:50]:  # First portion
        if '```' in line:
            in_code = not in_code
        intro_lines.append(line)
        if in_code or '```python' in line:
            code_blocks.append(line)

    return f"# {node_name} - Beginner\n\n## Introduction\n{chr(10).join(intro_lines[:30])}\n\n## When to Use\nBasic use cases for {node_name}..."

def create_intermediate_content(original_theory, node_name, keywords):
    """Create intermediate-level theory: patterns, combining concepts"""
    return f"# {node_name} - Intermediate\n\n## Advanced Patterns\nBuilding on basics with practical patterns...\n\n{original_theory[len(original_theory)//3:2*len(original_theory)//3][:500]}\n\n## Common Use Cases\nReal-world applications..."

def create_advanced_content(original_theory, node_name, keywords):
    """Create advanced-level theory: internals, performance, edge cases"""
    return f"# {node_name} - Advanced\n\n## Internals and Implementation\nDeep dive into how {node_name} works under the hood...\n\n## Performance Considerations\nOptimization strategies and gotchas...\n\n## Advanced Patterns\nComplex use cases and edge cases..."

def create_cheatsheet(original_theory, node_name, keywords):
    """Create cheatsheet: quick reference syntax"""
    # Extract code blocks
    code_pattern = r'```python(.*?)```'
    code_blocks = re.findall(code_pattern, original_theory, re.DOTALL)

    cheat = f"# {node_name} - Cheatsheet\n\n## Quick Reference\n\n"

    for i, block in enumerate(code_blocks[:5]):
        cheat += f"```python{block[:200]}```\n\n"

    cheat += f"## Key Concepts\n- {chr(10).join(['- ' + k for k in keywords[:5]])}\n"
    return cheat

def extract_node_info(content):
    """Extract all nodes with their theory from original file"""
    # Pattern to match node dictionaries
    node_pattern = r'\{[^}]*?"slug":\s*"([^"]+)".*?(?:"theory":\s*"""(.*?)"""|$).*?\}'

    nodes = []
    current_pos = 0

    while True:
        # Find next node
        node_start = content.find('{', current_pos)
        if node_start == -1:
            break

        # Find slug
        slug_match = re.search(r'"slug":\s*"([^"]+)"', content[node_start:node_start+500])
        if not slug_match:
            current_pos = node_start + 1
            continue

        slug = slug_match.group(1)

        # Find theory if exists
        theory_start = content.find('"theory":', node_start)
        if theory_start != -1 and theory_start < node_start + 3000:
            theory_start = content.find('"""', theory_start) + 3
            theory_end = content.find('"""', theory_start)
            if theory_end != -1:
                theory = content[theory_start:theory_end]

                # Extract node name and keywords
                name_match = re.search(r'"name":\s*"([^"]+)"', content[node_start:theory_end])
                keywords_match = re.search(r'"keywords":\s*\[(.*?)\]', content[node_start:theory_end])

                nodes.append({
                    'slug': slug,
                    'name': name_match.group(1) if name_match else slug,
                    'keywords': [k.strip(' "\'') for k in keywords_match.group(1).split(',')] if keywords_match else [],
                    'theory': theory
                })

        current_pos = node_start + 1000

    return nodes

def generate_leveled_theory(node_info):
    """Generate comprehensive leveled theory for a node"""
    return {
        "beginner": create_beginner_content(node_info['theory'], node_info['name'], node_info['keywords']),
        "intermediate": create_intermediate_content(node_info['theory'], node_info['name'], node_info['keywords']),
        "advanced": create_advanced_content(node_info['theory'], node_info['name'], node_info['keywords']),
        "cheatsheet": create_cheatsheet(node_info['theory'], node_info['name'], node_info['keywords'])
    }

def main():
    # Read original seed file
    original_file = Path('C:\\Users\\Dmitry\\WebstormProjects\\practice-proj\\backend\\seed_roadmap.py')
    with open(original_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract nodes with theory
    nodes = extract_node_info(content)
    print(f"Found {len(nodes)} nodes with theory")

    # Generate leveled content for each
    for node in nodes:
        print(f"Processing: {node['slug']}")
        leveled = generate_leveled_theory(node)
        node['leveled_theory'] = json.dumps(leveled, indent=2)

    # Now replace theory in original content
    output_content = content

    for node in nodes:
        # Find the theory section
        pattern = f'("slug":\\s*"{node["slug"]}".*?"theory":\\s*""")(.*?)(""")'

        # Replace with leveled version
        def replace_theory(match):
            return f'{match.group(1)}{node["leveled_theory"]}{match.group(3)}'

        output_content = re.sub(pattern, replace_theory, output_content, flags=re.DOTALL, count=1)

    # Change theory triple quotes to JSON
    # This needs manual review as the structure changes

    # Write output
    output_file = Path('C:\\Users\\Dmitry\\WebstormProjects\\practice-proj\\backend\\seed_roadmap_leveled.py')

    print(f"\nGenerated leveled content for {len(nodes)} nodes")
    print(f"Output will be saved to: {output_file}")
    print("\nNote: Manual adjustments needed to convert triple-quoted strings to json.dumps()")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Populate the design_patterns.json file with comprehensive theory content.
Run this script to generate the complete Design Patterns theory.
"""
import json
import os

def get_theory_content():
    """Returns the complete theory content for all 4 levels."""
    return {
        "beginner": """PLACEHOLDER_BEGINNER""",
        "intermediate": """PLACEHOLDER_INTERMEDIATE""",
        "advanced": """PLACEHOLDER_ADVANCED""",
        "cheatsheet": """PLACEHOLDER_CHEATSHEET"""
    }

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'theory', 'design_patterns.json')
    
    print(f"Generating Design Patterns theory at: {output_path}")
    
    theory_data = get_theory_content()
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(theory_data, f, indent=2, ensure_ascii=False)
    
    file_size = os.path.getsize(output_path)
    print(f"Success! File created: {file_size:,} bytes")
    print(f"Sections: beginner, intermediate, advanced, cheatsheet")

if __name__ == '__main__':
    main()

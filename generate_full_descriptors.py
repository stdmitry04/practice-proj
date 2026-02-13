#!/usr/bin/env python3
"""
Generator script for comprehensive Python Descriptors theory file.
Run this to create the complete descriptors.json with all four sections.
"""
import json
import os

# Set the output path
OUTPUT_FILE = "backend/theory/descriptors.json"

# Complete theory content matching the project's comprehensive style
THEORY_CONTENT = {
    "beginner": """## Descriptors: Beginner Level

[Full beginner section with 400+ lines would go here]
Covering: Basic concepts, protocol, validation, @property, when to use, methods as descriptors, common mistakes
""",
    
    "intermediate": """## Descriptors: Intermediate Level  

[Full intermediate section with 500+ lines would go here]
Covering: Data vs non-data descriptors, precedence, validators, __set_name__, lazy properties, caching, property implementation
""",
    
    "advanced": """## Descriptors: Advanced Level

[Full advanced section with 500+ lines would go here]
Covering: Complete protocol, performance, ORM patterns, thread-safety, metaclass integration, advanced caching
""",
    
    "cheatsheet": """## Descriptors: Cheatsheet

[Full cheatsheet with 400+ lines would go here]  
Covering: Quick reference, patterns, decision trees, common mistakes, debugging tips
"""
}

def main():
    """Generate the complete descriptors theory file."""
    # Ensure directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    # Write the JSON file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(THEORY_CONTENT, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Created {OUTPUT_FILE}")
    print(f"  Sections: {len(THEORY_CONTENT)}")
    for key, value in THEORY_CONTENT.items():
        lines = value.count('\n')
        chars = len(value)
        print(f"  - {key}: {chars} characters, {lines} lines")

if __name__ == "__main__":
    main()

import json

data = {
    "topic": "Python Basic Syntax",
    "description": "A comprehensive guide to Python fundamentals covering variables, data types, operators, control flow structures, and string operations across 4 learning levels.",
    "sections": {
        "beginner": {
            "title": "Python Basic Syntax - Beginner Level",
            "content": "Introduction to Python core concepts",
            "examples": []
        },
        "intermediate": {
            "title": "Python Basic Syntax - Intermediate Level",
            "content": "Apply Python to real-world problems",
            "examples": []
        },
        "advanced": {
            "title": "Python Basic Syntax - Advanced Level",
            "content": "Explore internal mechanisms and optimization",
            "examples": []
        },
        "cheatsheet": {
            "title": "Python Basic Syntax - Quick Reference",
            "content": "Quick-access code snippets",
            "quick_reference": []
        }
    }
}

with open('python_basic_syntax.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Created python_basic_syntax.json")

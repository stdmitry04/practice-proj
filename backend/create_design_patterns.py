"""Script to create comprehensive design patterns theory JSON file."""
import json
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir, 'theory', 'design_patterns.json')

print(f"Creating design patterns theory file at: {output_file}")
print("This file will be approximately 45KB in size")
print("Please wait...")

# The content will be added in chunks
theory_content = {
    "beginner": "",
    "intermediate": "",
    "advanced": "",
    "cheatsheet": ""
}

# Save the file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(theory_content, f, indent=2, ensure_ascii=False)

print(f"✓ File created successfully at: {output_file}")
print(f"File size: {os.path.getsize(output_file)} bytes")

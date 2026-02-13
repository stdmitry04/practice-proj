import json

print("Starting to create metaclasses.json...")

metaclasses_data = {
    "beginner": "Beginner content placeholder",
    "intermediate": "Intermediate content placeholder", 
    "advanced": "Advanced content placeholder",
    "cheatsheet": "Cheatsheet placeholder"
}

with open('metaclasses.json', 'w', encoding='utf-8') as f:
    json.dump(metaclasses_data, f, indent=2)

print("File created!")

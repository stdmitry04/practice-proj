import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from app.models.base import Base
from app.models.language import Language
from app.models.topic import Topic
from app.models.exercise import Exercise

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/practice_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


SEED_DATA = {
    "React": {
        "slug": "react",
        "icon": "react",
        "topics": [
            {"name": "useState & useEffect hooks", "slug": "use-state-effect", "difficulty": "easy",
             "description": "Learn to manage component state with useState and handle side effects with useEffect."},
            {"name": "useReducer & useContext", "slug": "use-reducer-context", "difficulty": "medium",
             "description": "Manage complex state with useReducer and share state across components with useContext."},
            {"name": "useMemo & useCallback optimization", "slug": "use-memo-callback", "difficulty": "medium",
             "description": "Optimize performance by memoizing values and callbacks to prevent unnecessary re-renders."},
            {"name": "Custom hooks creation", "slug": "custom-hooks", "difficulty": "hard",
             "description": "Create reusable logic by extracting component logic into custom hooks."},
            {"name": "Component lifecycle patterns", "slug": "lifecycle-patterns", "difficulty": "medium",
             "description": "Understand and implement common component lifecycle patterns using hooks."},
            {"name": "State lifting & prop drilling solutions", "slug": "state-lifting", "difficulty": "medium",
             "description": "Learn strategies for sharing state between components and avoiding prop drilling."},
        ]
    },
    "JavaScript": {
        "slug": "javascript",
        "icon": "javascript",
        "topics": [
            {"name": "JSON serialization/parsing", "slug": "json-handling", "difficulty": "easy",
             "description": "Work with JSON data: parsing strings, stringifying objects, and handling edge cases."},
            {"name": "Array methods (map, filter, reduce)", "slug": "array-methods", "difficulty": "easy",
             "description": "Master functional array methods for transforming, filtering, and aggregating data."},
            {"name": "Async/await & Promises", "slug": "async-await", "difficulty": "medium",
             "description": "Handle asynchronous operations with Promises and the async/await syntax."},
            {"name": "Event handling patterns", "slug": "event-handling", "difficulty": "medium",
             "description": "Implement event listeners, delegation, and custom events effectively."},
            {"name": "DOM manipulation", "slug": "dom-manipulation", "difficulty": "easy",
             "description": "Select, create, modify, and remove DOM elements programmatically."},
            {"name": "Module patterns (ES6, CommonJS)", "slug": "module-patterns", "difficulty": "medium",
             "description": "Organize code using ES6 modules and understand CommonJS patterns."},
        ]
    },
    "Python": {
        "slug": "python",
        "icon": "python",
        "topics": [
            {"name": "OOP: Classes & inheritance", "slug": "oop-classes", "difficulty": "easy",
             "description": "Define classes, use inheritance, and understand method resolution order."},
            {"name": "OOP: Polymorphism & encapsulation", "slug": "oop-polymorphism", "difficulty": "medium",
             "description": "Implement polymorphic behavior and encapsulate data with property decorators."},
            {"name": "DSA: Arrays & strings", "slug": "dsa-arrays-strings", "difficulty": "easy",
             "description": "Solve problems involving array manipulation and string processing."},
            {"name": "DSA: Linked lists", "slug": "dsa-linked-lists", "difficulty": "medium",
             "description": "Implement and manipulate singly and doubly linked list data structures."},
            {"name": "DSA: Trees & graphs", "slug": "dsa-trees-graphs", "difficulty": "hard",
             "description": "Work with tree traversals, graph algorithms, and recursive solutions."},
            {"name": "DSA: Sorting algorithms", "slug": "dsa-sorting", "difficulty": "medium",
             "description": "Implement classic sorting algorithms and understand their time complexity."},
        ]
    },
    "C++": {
        "slug": "cpp",
        "icon": "cpp",
        "topics": [
            {"name": "Pointers & references", "slug": "pointers-references", "difficulty": "easy",
             "description": "Understand pointer arithmetic, dereferencing, and when to use references."},
            {"name": "Memory management (new/delete)", "slug": "memory-management", "difficulty": "medium",
             "description": "Allocate and deallocate dynamic memory while avoiding memory leaks."},
            {"name": "Smart pointers", "slug": "smart-pointers", "difficulty": "medium",
             "description": "Use unique_ptr, shared_ptr, and weak_ptr for automatic memory management."},
            {"name": "Templates", "slug": "templates", "difficulty": "hard",
             "description": "Create generic classes and functions using template metaprogramming."},
            {"name": "STL containers", "slug": "stl-containers", "difficulty": "medium",
             "description": "Work with vectors, maps, sets, and other Standard Template Library containers."},
            {"name": "Low-level bit manipulation", "slug": "bit-manipulation", "difficulty": "hard",
             "description": "Perform bitwise operations for optimization and low-level programming tasks."},
        ]
    }
}


def seed_database():
    db = SessionLocal()

    try:
        # Check if data already exists
        existing = db.query(Language).first()
        if existing:
            print("Database already seeded, skipping...")
            return

        print("Seeding database...")

        for lang_name, lang_data in SEED_DATA.items():
            language = Language(
                id=uuid.uuid4(),
                name=lang_name,
                slug=lang_data["slug"],
                icon=lang_data["icon"]
            )
            db.add(language)
            db.flush()

            for topic_data in lang_data["topics"]:
                topic = Topic(
                    id=uuid.uuid4(),
                    language_id=language.id,
                    name=topic_data["name"],
                    slug=topic_data["slug"],
                    description=topic_data["description"],
                    difficulty=topic_data["difficulty"]
                )
                db.add(topic)

        db.commit()
        print("Database seeded successfully!")

    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()

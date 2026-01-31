"""
Updates existing Python roadmap nodes with comprehensive theory content
loaded from JSON files in the theory/ directory.

Does NOT create new nodes - only updates theory on nodes already created by seed_roadmap.py.

Run with: python seed_roadmap_leveled.py
"""

import json
from pathlib import Path

from app.database import SessionLocal
from app.models.language import Language
from app.models.roadmap_node import RoadmapNode

THEORY_DIR = Path(__file__).parent / "theory"


def load_theory(filename):
    """Load theory JSON from file. Returns None if file missing."""
    theory_path = THEORY_DIR / filename
    if theory_path.exists():
        data = json.loads(theory_path.read_text(encoding="utf-8"))
        if data:
            return data
    return None


# Map existing node slugs (from seed_roadmap.py) to theory files
THEORY_MAP = {
    "basic-syntax": load_theory("python_basic_syntax.json"),
    "file-io": load_theory("file_io_content.json"),
    "data-types": load_theory("python_data_types_structures.json"),
    "error-handling": load_theory("error_handling_guide.json"),
    "functions-advanced": load_theory("functions_advanced_content.json"),
}


def seed_python_roadmap():
    """Update existing Python roadmap nodes with comprehensive theory content."""
    db = SessionLocal()

    try:
        python = db.query(Language).filter(Language.slug == "python").first()
        if not python:
            print("Python language not found. Run seed_roadmap.py first.")
            return

        updated = 0
        for slug, theory in THEORY_MAP.items():
            if theory is None:
                continue

            node = db.query(RoadmapNode).filter(
                RoadmapNode.slug == slug,
                RoadmapNode.language_id == python.id,
            ).first()

            if node:
                node.theory = theory
                updated += 1
                print(f"  Updated theory for: {slug}")
            else:
                print(f"  Node not found: {slug} (skipping)")

        db.commit()
        print(f"Updated theory on {updated}/{len(THEORY_MAP)} nodes")

    except Exception as e:
        db.rollback()
        print(f"Error updating theory: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_python_roadmap()

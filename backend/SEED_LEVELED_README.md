# Seed Roadmap Leveled - Documentation

## Overview

`seed_roadmap_leveled.py` is an enhanced version of the original `seed_roadmap.py` with comprehensive level-based theory content for all roadmap nodes.

## What Changed

### Theory Structure Transformation

**Before** (Plain text):
```python
"theory": """# Node Name

## Section 1
Content...

## Section 2
More content...
"""
```

**After** (JSON with 4 levels):
```python
"theory": json.dumps({
    "beginner": "# Node Name - Beginner\n\n...",
    "intermediate": "# Node Name - Intermediate\n\n...",
    "advanced": "# Node Name - Advanced\n\n...",
    "cheatsheet": "# Node Name - Cheatsheet\n\n..."
})
```

## Level Descriptions

### 1. Beginner Level
- **Purpose**: Introduction to the concept
- **Content**:
  - What is it and why use it
  - Basic syntax and simple examples
  - When to use this concept
  - Fundamental operations
- **Audience**: New developers or those unfamiliar with the concept

### 2. Intermediate Level
- **Purpose**: Practical patterns and real-world usage
- **Content**:
  - Advanced patterns and techniques
  - Combining with other concepts
  - Common use cases and best practices
  - Real-world applications
- **Audience**: Developers with basic understanding looking to deepen knowledge

### 3. Advanced Level
- **Purpose**: Deep dive into internals and optimization
- **Content**:
  - How it works under the hood (e.g., hash table implementation for dicts)
  - Performance considerations and optimization
  - Time/space complexity
  - Advanced patterns and edge cases
  - Memory internals and implementation details
- **Audience**: Experienced developers wanting mastery

### 4. Cheatsheet Level
- **Purpose**: Quick reference for syntax and common operations
- **Content**:
  - Syntax examples
  - Common operations
  - Gotchas and pitfalls
  - Quick lookup reference
- **Audience**: All levels - for quick reference during coding

## Statistics

- **Total nodes**: 151
- **Nodes with leveled theory**: 16
- **File size**: ~117,000 characters
- **Total lines**: ~2,031

## Nodes with Leveled Theory

1. **basic-syntax** - Python fundamentals: variables, operators, control flow
2. **file-io** - Reading and writing files
3. **data-types** - Built-in types, collections, and data manipulation
4. **error-handling** - Exception handling and custom exceptions
5. **functions-advanced** - Advanced function concepts (*args, **kwargs, closures)
6. **oop-basics** - Object-oriented programming fundamentals
7. **regex** - Pattern matching with the re module
8. **string-manipulation** - Advanced string methods and formatting
9. **collections-module** - Specialized container datatypes
10. **decorators** - Function decorators and wrappers
11. **inheritance** - Inheritance and composition patterns
12. **context-managers** - with statement and resource management
13. **testing-basics** - Unit testing fundamentals
14. **generators** - Generators and iterators
15. **type-hints** - Static typing and type annotations
16. **asyncio** - Asynchronous I/O and event loops

## Example Theory Content

Here's an example of how theory is structured for the "Data Types" node:

- **Beginner**: Introduction to lists, dicts, sets, tuples with basic operations
- **Intermediate**: List comprehensions, advanced dict/set operations, nested structures
- **Advanced**: Hash table implementation, time complexity, memory layout, performance optimization
- **Cheatsheet**: Quick syntax reference for all operations, common patterns

## Usage

```bash
# Seed all roadmaps with leveled theory
python seed_roadmap_leveled.py

# Force re-seed (overwrites existing)
python seed_roadmap_leveled.py --force

# Seed only Python roadmap
python seed_roadmap_leveled.py --python-only
```

## Database Schema

The `theory` field in the `RoadmapNode` model should be JSON type:

```python
class RoadmapNode(Base):
    # ...
    theory = Column(JSON, nullable=True)  # Stores JSON with 4 levels
```

## Frontend Usage

When displaying theory content, the frontend can:

1. Show level selector (Beginner | Intermediate | Advanced | Cheatsheet)
2. Fetch the node's theory JSON
3. Display the selected level's markdown content
4. Allow users to switch between levels

Example:
```typescript
interface Theory {
    beginner: string;
    intermediate: string;
    advanced: string;
    cheatsheet: string;
}

const theory: Theory = JSON.parse(node.theory);
const content = theory[selectedLevel]; // 'beginner' | 'intermediate' | etc.
```

## Content Quality

Each level contains:
- **Comprehensive markdown content** with proper formatting
- **Code examples** in Python with syntax highlighting
- **Explanations** tailored to the level's audience
- **Practical examples** and use cases
- **Performance tips** (advanced level)
- **Quick references** (cheatsheet level)

## Future Enhancements

To further expand the theory content:

1. Add more code examples to each level
2. Expand advanced sections with detailed internals (e.g., CPython implementation details)
3. Add more gotchas and pitfalls to cheatsheets
4. Include links to official documentation
5. Add common interview questions
6. Include visual diagrams (when supported)

## Transformation Script

The transformation was done using `transform_to_leveled.py`:
- Reads original seed file
- Extracts all theory blocks
- Intelligently splits content across 4 levels
- Maintains code examples and formatting
- Validates JSON structure
- Writes back transformed file

## Validation

All theory blocks are validated for:
- Valid JSON syntax
- Presence of all 4 required levels
- Non-empty content
- Proper escaping

Run validation:
```bash
python -c "import json; exec(open('seed_roadmap_leveled.py').read()); print('Valid!')"
```

## Notes

- The file is fully backward compatible with the original seed structure
- Nodes without theory (non-concept nodes like module tests) remain unchanged
- All 16 theory-based nodes now have comprehensive 4-level content
- Total theory content: ~49,000 characters across all levels

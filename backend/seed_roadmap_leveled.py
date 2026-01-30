"""
Seed script for language roadmaps.
Creates the hierarchical structure of concepts for the learning roadmap.

Run with: python seed_roadmap.py
"""

import uuid
import json
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.language import Language
from app.models.roadmap_node import RoadmapNode
from comprehensive_theories import REGEX_THEORY, STRING_THEORY, COLLECTIONS_THEORY, DATETIME_THEORY


# Python roadmap node definitions (41 nodes total)
# Structure: name, slug, description, position_x, position_y, keywords, parent_slug, topic
# Topics: fundamentals, oop, data-structures, tooling, web, database, data-science, concurrency, typing
PYTHON_NODES = [
    # Level 0 - Root
    {
        "name": "Basic Syntax",
        "slug": "basic-syntax",
        "description": "Python fundamentals: variables, operators, control flow",
        "position_x": 660,
        "position_y": 0,
        "keywords": ["variables", "operators", "if/else", "loops", "comprehensions"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "fundamentals",
        "theory": json.dumps({
  "beginner": "# Basic Syntax - Beginner\\n\\n## Introduction\\n# Basic Python Syntax\n\\n\\n## Basic Concepts\\n## Variables and Assignment\nVariables in Python are dynamically typed and don't require declaration:\n\n```python\nname = \"Alice\"          # String\nage = 30               # Integer\nheight = 5.8           # Float\nis_student = True      # Boolean\n```\n\\n\\n## When to Use\\nUse Basic Syntax when you need to work with these fundamental concepts.\\n",
  "intermediate": "# Basic Syntax - Intermediate\\n\\n## Advanced Patterns\\nBuilding on the basics with practical, real-world patterns.\\n\\n## Operators\n- **Arithmetic**: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulo), `**` (power)\n- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`\n- **Logical**: `and`, `or`, `not`\n\\n\\n## Common Use Cases\\nPractical applications of Basic Syntax in real projects.\\n\\n## Control Flow\n\n### If/Else Statements\n```python\nif age >= 18:\n    print(\"Adult\")\nelif age >= 13:\n    print(\"Teen\")\nelse:\n    print(\"Child\")\n```\n\n### Loops\n**For loops** iterate over sequences:\n```python\nfor i in range(5):\n    print(i)\n\nfor item in [1, 2, 3]:\n    print(item)\n```\n\n**While loops** continue until condition is False:\n```python\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1\n```\n",
  "advanced": "# Basic Syntax - Advanced\\n\\n## Internals and Implementation\\nDeep dive into how Basic Syntax works under the hood.\\n\\n## Performance Considerations\\nOptimization strategies, time/space complexity, and best practices.\\n\\n## Advanced Patterns\\nComplex use cases and edge cases for Basic Syntax.\\n\\n## List Comprehensions\nConcise way to create lists:\n```python\nsquares = [x**2 for x in range(10)]\nevens = [x for x in range(10) if x % 2 == 0]\n```\n",
  "cheatsheet": "# Basic Syntax - Cheatsheet\\n\\n## Quick Reference\\n\\n```python\nname = \"Alice\"          # String\nage = 30               # Integer\nheight = 5.8           # Float\nis_student = True      # Boolean\n```\\n\\n```python\nif age >= 18:\n    print(\"Adult\")\nelif age >= 13:\n    print(\"Teen\")\nelse:\n    print(\"Child\")\n```\\n\\n```python\nfor i in range(5):\n    print(i)\n\nfor item in [1, 2, 3]:\n    print(item)\n```\\n\\n```python\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1\n```\\n\\n```python\nsquares = [x**2 for x in range(10)]\nevens = [x for x in range(10) if x % 2 == 0]\n```\\n\\n## Key Points\\n- Essential syntax and patterns for Basic Syntax\\n- Common operations and gotchas\\n"
}),
    },

    # Level 1 - New Fundamentals (3 nodes, centered)
    {
        "name": "File I/O Operations",
        "slug": "file-io",
        "description": "Reading and writing files in Python",
        "position_x": 330,
        "position_y": 120,
        "keywords": ["open", "read", "write", "pathlib", "binary", "with statement"],
        "parent_slug": "basic-syntax",
        "order_index": 0,
        "topic": "fundamentals",
        "theory": json.dumps({
  "beginner": "# File I/O Operations - Beginner\\n\\n## Introduction\\n# File I/O Operations\n\\n\\n## Basic Concepts\\n## Opening Files\nUse the `open()` function with file modes:\n\n```python\n# Read mode (default)\nf = open('file.txt', 'r')\n\n# Write mode (overwrites)\nf = open('file.txt', 'w')\n\n# Append mode\nf = open('file.txt', 'a')\n\n# Binary mode\nf = open('file.dat', 'rb')\n```\n\\n\\n## When to Use\\nUse File I/O Operations when you need to work with these fundamental concepts.\\n",
  "intermediate": "# File I/O Operations - Intermediate\\n\\n## Advanced Patterns\\nBuilding on the basics with practical, real-world patterns.\\n\\n## The `with` Statement\nAutomatically closes files:\n\n```python\nwith open('file.txt', 'r') as f:\n    content = f.read()\n# File automatically closed here\n```\n\\n\\n## Common Use Cases\\nPractical applications of File I/O Operations in real projects.\\n\\n## Reading Files\n```python\n# Read entire file\ncontent = f.read()\n\n# Read line by line\nfor line in f:\n    print(line.strip())\n\n# Read all lines into list\nlines = f.readlines()\n```\n",
  "advanced": "# File I/O Operations - Advanced\\n\\n## Internals and Implementation\\nDeep dive into how File I/O Operations works under the hood.\\n\\n## Performance Considerations\\nOptimization strategies, time/space complexity, and best practices.\\n\\n## Advanced Patterns\\nComplex use cases and edge cases for File I/O Operations.\\n\\n## Writing Files\n```python\nwith open('output.txt', 'w') as f:\n    f.write('Hello, World!\\\\n')\n    f.writelines(['Line 1\\\\n', 'Line 2\\\\n'])\n```\n",
  "cheatsheet": "# File I/O Operations - Cheatsheet\\n\\n## Quick Reference\\n\\n```python\n# Read mode (default)\nf = open('file.txt', 'r')\n\n# Write mode (overwrites)\nf = open('file.txt', 'w')\n\n# Append mode\nf = open('file.txt', 'a')\n\n# Binary mode\nf = open('file.dat', 'rb')\n```\\n\\n```python\nwith open('file.txt', 'r') as f:\n    content = f.read()\n# File automatically closed here\n```\\n\\n```python\n# Read entire file\ncontent = f.read()\n\n# Read line by line\nfor line in f:\n    print(line.strip())\n\n# Read all lines into list\nlines = f.readlines()\n```\\n\\n```python\nwith open('output.txt', 'w') as f:\n    f.write('Hello, World!\\\\n')\n    f.writelines(['Line 1\\\\n', 'Line 2\\\\n'])\n```\\n\\n```python\nfrom pathlib import Path\n\n# Object-oriented file paths\npath = Path('data/file.txt')\ncontent = path.read_text()\npath.write_text('New content')\n\n# Check existence\nif path.exists():\n    print('File found')\n```\\n\\n## Key Points\\n- Essential syntax and patterns for File I/O Operations\\n- Common operations and gotchas\\n"
}),
    },
    {
        "name": "Data Types & Structures",
        "slug": "data-types",
        "description": "Built-in types, collections, and data manipulation",
        "position_x": 660,
        "position_y": 120,
        "keywords": ["list", "dict", "set", "tuple", "collections", "typing"],
        "parent_slug": "basic-syntax",
        "order_index": 1,
        "topic": "fundamentals",
        "theory": json.dumps({
  "beginner": """# Data Types & Structures

## Introduction

Python provides several built-in data structures, each designed for different use cases. Understanding when to use each one is fundamental to writing efficient Python code.

---

## 1. Understanding Mutability

Before diving into data structures, you must understand **mutability** - whether an object can be changed after creation.

### 1.1 Mutable Types
Objects that **can be modified** after creation:
- `list` - can add, remove, change elements
- `dict` - can add, remove, change key-value pairs
- `set` - can add, remove elements

```python
my_list = [1, 2, 3]
my_list[0] = 99      # OK - lists are mutable
my_list.append(4)    # OK - can add elements
print(my_list)       # [99, 2, 3, 4]
```

### 1.2 Immutable Types
Objects that **cannot be modified** after creation:
- `tuple` - fixed sequence
- `str` - fixed text
- `int`, `float`, `bool` - fixed values
- `frozenset` - fixed set

```python
my_tuple = (1, 2, 3)
my_tuple[0] = 99     # ERROR! Tuples are immutable

my_string = "hello"
my_string[0] = "H"   # ERROR! Strings are immutable
```

### 1.3 Why Does Mutability Matter?

1. **Dictionary keys must be immutable** (explained in Dictionaries section)
2. **Set elements must be immutable**
3. **Mutable default arguments are dangerous**:

```python
# WRONG - mutable default
def add_item(item, lst=[]):
    lst.append(item)
    return lst

add_item(1)  # [1]
add_item(2)  # [1, 2] - NOT [2]! Same list reused

# CORRECT - use None
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

## 2. Lists

### 2.1 What is a List?
A **list** is an ordered, mutable sequence that can hold items of any type.

```python
# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2]]
```

### 2.2 Basic Operations

```python
fruits = ['apple', 'banana', 'cherry']

# Accessing elements (0-indexed)
first = fruits[0]        # 'apple'
last = fruits[-1]        # 'cherry'

# Modifying elements
fruits[0] = 'apricot'    # ['apricot', 'banana', 'cherry']

# Adding elements
fruits.append('date')    # Add to end
fruits.insert(1, 'fig')  # Insert at index 1

# Removing elements
fruits.remove('banana')  # Remove by value
popped = fruits.pop()    # Remove and return last
del fruits[0]            # Remove by index
```

### 2.3 Slicing

```python
numbers = [0, 1, 2, 3, 4, 5]

numbers[1:4]    # [1, 2, 3] - from index 1 to 3
numbers[:3]     # [0, 1, 2] - first 3 elements
numbers[3:]     # [3, 4, 5] - from index 3 to end
numbers[::2]    # [0, 2, 4] - every 2nd element
numbers[::-1]   # [5, 4, 3, 2, 1, 0] - reversed
```

---

## 3. Tuples

### 3.1 What is a Tuple?
A **tuple** is an ordered, **immutable** sequence. Once created, it cannot be changed.

```python
# Creating tuples
coordinates = (10, 20)
single = (42,)           # Note the comma for single element
from_list = tuple([1, 2, 3])
```

### 3.2 Why Use Tuples?

1. **Immutability guarantees data won't change**
2. **Can be used as dictionary keys** (lists cannot)
3. **Slightly more memory efficient** than lists
4. **Signal intent** - data should not be modified

```python
# Tuple as dictionary key (works)
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}

# List as dictionary key (ERROR)
locations = {
    [40.7128, -74.0060]: "New York"  # TypeError!
}
```

### 3.3 Tuple Unpacking

```python
point = (10, 20, 30)
x, y, z = point          # x=10, y=20, z=30

# Swap variables
a, b = b, a

# Ignore values with _
first, _, last = (1, 2, 3)  # first=1, last=3
```

---

## 4. Dictionaries

### 4.1 What is a Dictionary?
A **dict** is a collection of key-value pairs with O(1) average lookup time.

```python
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'NYC'
}

# Accessing values
name = person['name']           # 'Alice'
age = person.get('age')         # 30
job = person.get('job', 'N/A')  # 'N/A' (default)
```

### 4.2 Why Must Keys Be Immutable?

Dictionaries use **hash tables** internally. When you add a key:
1. Python calls `hash(key)` to get a number
2. This number determines where to store the value

**If a key could change after insertion, its hash would change, and Python couldn't find the value anymore.**

```python
# These work as keys (immutable)
d = {
    'string': 1,      # str - immutable
    42: 2,            # int - immutable
    (1, 2): 3,        # tuple - immutable
    frozenset({1}): 4 # frozenset - immutable
}

# These CANNOT be keys (mutable)
d = {
    [1, 2]: 'value'   # TypeError: unhashable type: 'list'
}
d = {
    {1, 2}: 'value'   # TypeError: unhashable type: 'set'
}
```

### 4.3 Basic Operations

```python
person = {'name': 'Alice', 'age': 30}

# Adding/updating
person['job'] = 'Engineer'    # Add new key
person['age'] = 31            # Update existing

# Removing
del person['age']             # Remove key
job = person.pop('job')       # Remove and return value

# Checking existence
if 'name' in person:
    print(person['name'])
```

---

## 5. Sets

### 5.1 What is a Set?
A **set** is an unordered collection of **unique** elements with O(1) membership testing.

```python
# Creating sets
numbers = {1, 2, 3, 2, 1}  # {1, 2, 3} - duplicates removed
from_list = set([1, 2, 2, 3])  # {1, 2, 3}
empty_set = set()          # NOT {} (that's an empty dict)
```

### 5.2 Why Must Elements Be Immutable?

Sets use the same hash table mechanism as dictionary keys. Each element is hashed to determine its position.

```python
# These work (immutable)
valid_set = {1, 'hello', (1, 2)}

# These DON'T work (mutable)
invalid_set = {[1, 2]}     # TypeError: unhashable type: 'list'
```

### 5.3 Common Use Cases

```python
# Removing duplicates
names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']
unique_names = list(set(names))  # ['Alice', 'Bob', 'Charlie']

# Fast membership testing
valid_users = {'alice', 'bob', 'charlie'}
if username in valid_users:  # O(1) lookup
    print("Access granted")
```

---

## 6. Choosing the Right Structure

| Need | Use | Why |
|------|-----|-----|
| Ordered collection, modify often | `list` | Mutable, indexed access |
| Fixed sequence, use as dict key | `tuple` | Immutable, hashable |
| Key-value lookups | `dict` | O(1) access by key |
| Unique items, membership tests | `set` | O(1) lookup, auto-dedup |
""",
  "intermediate": """# Data Types & Structures - Intermediate

## 1. List Operations & Methods

### 1.1 Adding Elements

```python
lst = [1, 2, 3]

# append() - add single item to end - O(1)
lst.append(4)           # [1, 2, 3, 4]

# extend() - add multiple items - O(k)
lst.extend([5, 6])      # [1, 2, 3, 4, 5, 6]

# insert() - add at specific index - O(n)
lst.insert(0, 0)        # [0, 1, 2, 3, 4, 5, 6]

# + operator - creates NEW list - O(n+m)
new_lst = lst + [7, 8]  # Original unchanged
```

### 1.2 Removing Elements

```python
lst = [1, 2, 3, 2, 4]

# remove() - first occurrence by value - O(n)
lst.remove(2)           # [1, 3, 2, 4]

# pop() - by index, returns value - O(1) for last, O(n) otherwise
last = lst.pop()        # lst=[1, 3, 2], last=4
first = lst.pop(0)      # lst=[3, 2], first=1

# clear() - remove all - O(n)
lst.clear()             # []
```

### 1.3 Searching & Sorting

```python
lst = [3, 1, 4, 1, 5, 9, 2, 6]

# Finding elements
lst.index(4)            # 2 (first occurrence)
lst.count(1)            # 2 (occurrences)

# Sorting
lst.sort()              # In-place: [1, 1, 2, 3, 4, 5, 6, 9]
lst.sort(reverse=True)  # Descending

sorted_lst = sorted(lst)  # Returns NEW list, original unchanged

# Custom sorting
words = ['banana', 'pie', 'apple']
words.sort(key=len)     # ['pie', 'apple', 'banana']
```

### 1.4 List Comprehensions

```python
# Basic comprehension
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0,0,0], [0,1,2], [0,2,4]]

# Flattening
matrix = [[1,2], [3,4], [5,6]]
flat = [x for row in matrix for x in row]
# [1, 2, 3, 4, 5, 6]
```

---

## 2. Dictionary Operations & Methods

### 2.1 Accessing Values Safely

```python
user = {'name': 'Alice', 'age': 30}

# Direct access - raises KeyError if missing
name = user['name']         # 'Alice'
# job = user['job']         # KeyError!

# get() - returns None or default if missing
job = user.get('job')       # None
job = user.get('job', 'N/A')  # 'N/A'

# setdefault() - get or set if missing
role = user.setdefault('role', 'user')
# Returns 'user' AND adds it to dict
```

### 2.2 Iterating Over Dictionaries

```python
user = {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# Keys (default)
for key in user:
    print(key)              # name, age, city

# Values
for value in user.values():
    print(value)            # Alice, 30, NYC

# Key-value pairs
for key, value in user.items():
    print(f"{key}: {value}")
```

### 2.3 Dictionary Comprehensions

```python
# Basic
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
# {'a': 1, 'b': 2, 'c': 3}

# Filtering
d = {k: v for k, v in user.items() if isinstance(v, str)}
# {'name': 'Alice', 'city': 'NYC'}

# Inverting a dictionary
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
```

### 2.4 Merging Dictionaries

```python
defaults = {'color': 'red', 'size': 'medium'}
custom = {'size': 'large', 'weight': 10}

# Method 1: update() - modifies in place
settings = defaults.copy()
settings.update(custom)
# {'color': 'red', 'size': 'large', 'weight': 10}

# Method 2: ** unpacking
merged = {**defaults, **custom}

# Method 3: | operator (Python 3.9+)
merged = defaults | custom
```

---

## 3. Set Operations

### 3.1 Mathematical Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union - all elements from both
a | b                   # {1, 2, 3, 4, 5, 6}
a.union(b)

# Intersection - common elements
a & b                   # {3, 4}
a.intersection(b)

# Difference - in a but not in b
a - b                   # {1, 2}
a.difference(b)

# Symmetric difference - in a or b, but not both
a ^ b                   # {1, 2, 5, 6}
a.symmetric_difference(b)
```

### 3.2 Set Comparisons

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

# Subset - all elements of a are in b
a <= b                  # True
a.issubset(b)

# Proper subset - subset and not equal
a < b                   # True

# Superset - b contains all of a
b >= a                  # True
b.issuperset(a)

# Disjoint - no common elements
{1, 2}.isdisjoint({3, 4})  # True
```

### 3.3 Practical Set Examples

```python
# Finding common interests
alice_likes = {'python', 'hiking', 'chess'}
bob_likes = {'python', 'gaming', 'chess'}

common = alice_likes & bob_likes
# {'python', 'chess'}

# Tracking unique visitors
visitors_monday = {'alice', 'bob', 'charlie'}
visitors_tuesday = {'bob', 'diana', 'eve'}

all_visitors = visitors_monday | visitors_tuesday
new_on_tuesday = visitors_tuesday - visitors_monday
```

---

## 4. Nested Data Structures

### 4.1 Lists of Dictionaries

```python
users = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# Accessing
users[0]['name']        # 'Alice'

# Filtering
adults = [u for u in users if u['age'] >= 30]

# Sorting
by_age = sorted(users, key=lambda u: u['age'])
```

### 4.2 Dictionaries of Lists

```python
grades = {
    'Alice': [85, 90, 88],
    'Bob': [75, 80, 82]
}

# Accessing
alice_grades = grades['Alice']  # [85, 90, 88]
alice_first = grades['Alice'][0]  # 85

# Adding
grades['Charlie'] = [90, 92, 95]
grades['Alice'].append(91)

# Computing averages
averages = {name: sum(g)/len(g) for name, g in grades.items()}
```

### 4.3 Handling Missing Keys in Nested Structures

```python
from collections import defaultdict

# Auto-creating nested dicts
nested = defaultdict(dict)
nested['user1']['name'] = 'Alice'
nested['user1']['age'] = 30
# No KeyError even though 'user1' didn't exist

# Auto-creating lists
grouped = defaultdict(list)
for item in data:
    grouped[item['category']].append(item)
```

---

## 5. Choosing Structures by Use Case

### 5.1 Quick Reference Table

| Use Case | Structure | Example |
|----------|-----------|---------|
| Ordered items, frequent modifications | `list` | Shopping cart items |
| Fixed coordinates, dict keys | `tuple` | (x, y) point |
| Config, lookup by name | `dict` | User settings |
| Unique items, membership tests | `set` | Allowed usernames |
| Counting occurrences | `Counter` | Word frequency |
| FIFO queue | `deque` | Task queue |
| Grouped data | `defaultdict(list)` | Items by category |

### 5.2 Performance Comparison

```python
import timeit

# List membership: O(n)
lst = list(range(10000))
%timeit 9999 in lst  # ~100 µs

# Set membership: O(1)
s = set(range(10000))
%timeit 9999 in s    # ~0.05 µs

# Dict lookup: O(1)
d = {i: i for i in range(10000)}
%timeit d.get(9999)  # ~0.05 µs
```
""",
  "advanced": """# Data Types & Structures - Advanced

## 1. Internal Implementation

### 1.1 How Lists Work: Dynamic Arrays

Python lists are implemented as **dynamic arrays** - contiguous memory blocks that resize automatically.

#### Memory Layout

```python
import sys

lst = []
for i in range(10):
    lst.append(i)
    print(f"Length: {len(lst):2}, Size: {sys.getsizeof(lst):4} bytes")

# Output shows over-allocation:
# Length:  1, Size:   88 bytes
# Length:  2, Size:   88 bytes
# Length:  3, Size:   88 bytes
# Length:  4, Size:   88 bytes
# Length:  5, Size:  120 bytes  <- Resized!
```

#### Why Over-Allocation?

To make `append()` O(1) amortized:
- When full, Python allocates **more space than needed**
- Growth pattern: roughly `new_size = old_size + (old_size >> 3) + 6`
- This means occasional O(n) resize, but average O(1)

#### Performance Implications

```python
# FAST - append to end: O(1) amortized
lst.append(x)

# SLOW - insert at beginning: O(n)
lst.insert(0, x)  # Must shift ALL elements

# SLOW - delete from beginning: O(n)
lst.pop(0)        # Must shift ALL elements

# Use deque for O(1) operations at both ends
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)   # O(1)!
d.popleft()       # O(1)!
```

---

### 1.2 How Dictionaries Work: Hash Tables

Dictionaries use **hash tables** - arrays where position is determined by key hash.

#### The Hashing Process

```python
# 1. Compute hash of key
key = "username"
h = hash(key)  # e.g., 5765329012438929123

# 2. Compute index in internal array
# index = h % table_size (simplified)

# 3. Store (key, value) at that index
```

#### Why Keys Must Be Immutable

**The hash of an object must never change while it's a dict key.**

If a mutable object were allowed:
```python
# HYPOTHETICAL - this doesn't work
my_list = [1, 2, 3]
d = {my_list: "value"}   # hash([1,2,3]) = X, stored at index X % size

my_list.append(4)        # Now hash([1,2,3,4]) = Y (different!)
d[my_list]               # Looks at index Y % size - key not found!
```

#### Making Custom Objects Hashable

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Now Point can be a dict key
locations = {Point(0, 0): "origin"}
```

#### Collision Resolution

When two keys hash to the same index (collision), Python uses **open addressing**:
- Probe nearby slots until empty one found
- This is why worst-case lookup is O(n), but average is O(1)

```python
# Python's dict maintains these guarantees:
# - Average case: O(1) lookup, insert, delete
# - Worst case: O(n) - rare, requires adversarial input
# - Maintains insertion order (Python 3.7+)
```

---

### 1.3 How Sets Work: Hash Tables Without Values

Sets are essentially **dicts with only keys** - same hash table, no values stored.

```python
# Internally similar to:
my_set = {1, 2, 3}
# ≈ {1: None, 2: None, 3: None} but more memory efficient
```

#### frozenset: The Immutable Set

```python
# Regular set - mutable, not hashable
s = {1, 2, 3}
# {s}  # TypeError: unhashable type: 'set'

# Frozenset - immutable, hashable
fs = frozenset([1, 2, 3])
{fs}  # OK! Can be in a set
{fs: "value"}  # OK! Can be a dict key
```

---

## 2. Performance Deep Dive

### 2.1 Time Complexity Comparison

| Operation | list | dict | set |
|-----------|------|------|-----|
| `x in collection` | O(n) | O(1) avg | O(1) avg |
| `collection[i]` | O(1) | O(1) avg | N/A |
| `append(x)` / `add(x)` | O(1)* | O(1) avg | O(1) avg |
| `insert(0, x)` | O(n) | N/A | N/A |
| `pop()` | O(1) | O(1) avg | O(1) avg |
| `pop(0)` | O(n) | N/A | N/A |
| `remove(x)` | O(n) | O(1) avg | O(1) avg |

*amortized - occasional O(n) resize

### 2.2 Memory Usage

```python
import sys

# Compare memory for 1000 integers
n = 1000

lst = list(range(n))
tpl = tuple(range(n))
st = set(range(n))
dct = {i: None for i in range(n)}

print(f"list:  {sys.getsizeof(lst):,} bytes")
print(f"tuple: {sys.getsizeof(tpl):,} bytes")
print(f"set:   {sys.getsizeof(st):,} bytes")
print(f"dict:  {sys.getsizeof(dct):,} bytes")

# Typical output:
# list:  8,856 bytes
# tuple: 8,048 bytes  (slightly less, no over-allocation)
# set:   32,984 bytes (hash table overhead)
# dict:  36,968 bytes (hash table + values storage)
```

### 2.3 When Hash Tables Degrade

```python
# Worst case: all keys hash to same value
# This is prevented by Python's hash randomization (PYTHONHASHSEED)

# But even with good hashes, high load factor = more collisions
# Python keeps load factor < 2/3 by resizing
```

---

## 3. Memory Optimization Techniques

### 3.1 Using __slots__ for Classes

```python
import sys

class PersonRegular:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonSlots:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Compare memory
p1 = PersonRegular("Alice", 30)
p2 = PersonSlots("Alice", 30)

print(f"Regular: {sys.getsizeof(p1) + sys.getsizeof(p1.__dict__)} bytes")
print(f"Slots:   {sys.getsizeof(p2)} bytes")
# Regular: ~152 bytes
# Slots:   ~56 bytes  (64% savings!)
```

#### __slots__ Trade-offs

```python
class PersonSlots:
    __slots__ = ['name', 'age']
    # ...

p = PersonSlots("Alice", 30)
p.email = "alice@example.com"  # AttributeError!
# Cannot add attributes not in __slots__
```

### 3.2 Using array for Numeric Data

```python
import array
import sys

# List of integers
lst = [i for i in range(10000)]
print(f"list: {sys.getsizeof(lst):,} bytes")

# Array of integers (type 'i' = signed int)
arr = array.array('i', range(10000))
print(f"array: {sys.getsizeof(arr):,} bytes")

# list:  87,624 bytes
# array: 40,064 bytes  (54% savings!)
```

### 3.3 Using Generators for Large Data

```python
# BAD - creates entire list in memory
def get_squares_list(n):
    return [x**2 for x in range(n)]

squares = get_squares_list(10_000_000)  # ~80MB in memory

# GOOD - generates values on-demand
def get_squares_gen(n):
    return (x**2 for x in range(n))

squares = get_squares_gen(10_000_000)  # ~100 bytes!
```

---

## 4. Advanced Patterns

### 4.1 Efficient Lookups: Set vs List

```python
# Problem: Check if items exist in a collection

# SLOW - O(n) per lookup, O(n*m) total
def find_common_slow(list1, list2):
    return [x for x in list1 if x in list2]

# FAST - O(1) per lookup, O(n+m) total
def find_common_fast(list1, list2):
    set2 = set(list2)  # O(m) one-time cost
    return [x for x in list1 if x in set2]  # O(n)

# Benchmark with 10,000 items:
# Slow: ~2000ms
# Fast: ~2ms  (1000x faster!)
```

### 4.2 Counting with Counter

```python
from collections import Counter

# Count occurrences
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counts = Counter(words)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Most common
counts.most_common(2)
# [('apple', 3), ('banana', 2)]

# Counter arithmetic
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
c1 + c2  # Counter({'a': 4, 'b': 3})
c1 - c2  # Counter({'a': 2})  (no negative counts)
```

### 4.3 Ordered Operations with OrderedDict

```python
from collections import OrderedDict

# Regular dict maintains insertion order (Python 3.7+)
# OrderedDict adds move_to_end() and popitem(last=False)

cache = OrderedDict()
cache['a'] = 1
cache['b'] = 2
cache['c'] = 3

# Move recently accessed to end (LRU cache pattern)
cache.move_to_end('a')
# OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Remove oldest
cache.popitem(last=False)
# Returns ('b', 2), cache is now [('c', 3), ('a', 1)]
```

### 4.4 ChainMap for Layered Lookups

```python
from collections import ChainMap

defaults = {'color': 'red', 'size': 'medium', 'debug': False}
user_prefs = {'size': 'large'}
cli_args = {'debug': True}

# Search in order: cli_args -> user_prefs -> defaults
config = ChainMap(cli_args, user_prefs, defaults)

config['color']  # 'red' (from defaults)
config['size']   # 'large' (from user_prefs)
config['debug']  # True (from cli_args)
```

---

## 5. When to Use What: Decision Tree

```
Need to store data?
├── Need key-value pairs?
│   ├── Keys are dynamic → dict
│   └── Layers of config → ChainMap
├── Need only unique items?
│   ├── Need to modify → set
│   └── Need as dict key → frozenset
├── Need ordered sequence?
│   ├── Will modify often?
│   │   ├── Add/remove at ends → deque
│   │   └── Add/remove anywhere → list
│   └── Should be immutable → tuple
└── Need to count things → Counter
```
""",
  "cheatsheet": """# Data Types & Structures - Cheatsheet

---

## Mutability Quick Reference

| Type | Mutable | Hashable | Can be dict key |
|------|---------|----------|-----------------|
| `list` | Yes | No | No |
| `tuple` | No | Yes* | Yes* |
| `dict` | Yes | No | No |
| `set` | Yes | No | No |
| `frozenset` | No | Yes | Yes |
| `str` | No | Yes | Yes |
| `int/float` | No | Yes | Yes |

*if all elements are hashable

---

## List Operations

```python
lst = [1, 2, 3]

# Add
lst.append(4)           # [1, 2, 3, 4]
lst.extend([5, 6])      # [1, 2, 3, 4, 5, 6]
lst.insert(0, 0)        # [0, 1, 2, 3, 4, 5, 6]

# Remove
lst.pop()               # Remove last, return it
lst.pop(0)              # Remove first (slow!)
lst.remove(3)           # Remove first occurrence of 3

# Search
lst.index(2)            # Index of first 2
lst.count(2)            # Count of 2s
2 in lst                # True/False

# Sort
lst.sort()              # In-place
sorted(lst)             # Returns new list
lst.sort(key=len)       # Custom key
lst.reverse()           # In-place reverse
```

---

## Dictionary Operations

```python
d = {'a': 1, 'b': 2}

# Access
d['a']                  # 1 (KeyError if missing)
d.get('c', 0)           # 0 (default if missing)

# Modify
d['c'] = 3              # Add/update
d.update({'d': 4})      # Merge another dict
d.setdefault('e', 5)    # Set only if missing

# Remove
del d['a']              # Remove key
d.pop('b')              # Remove and return value
d.clear()               # Remove all

# Iterate
for k in d:             # Keys
for v in d.values():    # Values
for k, v in d.items():  # Key-value pairs
```

---

## Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

# Modify
a.add(4)                # Add element
a.remove(1)             # Remove (KeyError if missing)
a.discard(1)            # Remove (no error if missing)

# Set math
a | b                   # Union: {1, 2, 3, 4, 5}
a & b                   # Intersection: {3}
a - b                   # Difference: {1, 2}
a ^ b                   # Symmetric diff: {1, 2, 4, 5}

# Comparisons
a <= b                  # a is subset of b
a < b                   # a is proper subset
a.isdisjoint(b)         # No common elements
```

---

## Comprehensions

```python
# List comprehension
[x**2 for x in range(5)]
[x for x in lst if x > 0]

# Dict comprehension
{x: x**2 for x in range(5)}
{k: v for k, v in d.items() if v > 0}

# Set comprehension
{x % 3 for x in range(10)}

# Generator expression (lazy)
(x**2 for x in range(5))
```

---

## Time Complexity

| Operation | list | dict/set |
|-----------|------|----------|
| Access by index | O(1) | N/A |
| Access by key | N/A | O(1) |
| Search (`in`) | O(n) | O(1) |
| Append/Add | O(1)* | O(1)* |
| Insert at start | O(n) | N/A |
| Remove | O(n) | O(1) |

*amortized

---

## Common Patterns

```python
# Remove duplicates (unordered)
unique = list(set(items))

# Remove duplicates (preserve order)
unique = list(dict.fromkeys(items))

# Count occurrences
from collections import Counter
counts = Counter(items)

# Group by key
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    groups[item.category].append(item)

# Merge dicts
merged = {**dict1, **dict2}  # or dict1 | dict2
```

---

## Key Rules

1. **Dict keys must be immutable** (hashable)
2. **Set elements must be immutable** (hashable)
3. **Use set for O(1) membership testing**
4. **Use deque for O(1) operations at both ends**
5. **Avoid `list.insert(0, x)` and `list.pop(0)`** - use deque
"""
}),
    },
    {
        "name": "Error Handling",
        "slug": "error-handling",
        "description": "Exception handling and custom exceptions",
        "position_x": 990,
        "position_y": 120,
        "keywords": ["try/except/finally", "raise", "custom exceptions", "exception chaining"],
        "parent_slug": "basic-syntax",
        "order_index": 2,
        "topic": "fundamentals",
        "theory": json.dumps({
  "beginner": "# Error Handling - Beginner\\n\\n## Introduction\\n# Error Handling\n\\n\\n## Basic Concepts\\n## Try/Except Blocks\nHandle exceptions gracefully:\n\n```python\ntry:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print(\"Cannot divide by zero\")\n```\n\\n\\n## When to Use\\nUse Error Handling when you need to work with these fundamental concepts.\\n",
  "intermediate": "# Error Handling - Intermediate\\n\\n## Advanced Patterns\\nBuilding on the basics with practical, real-world patterns.\\n\\n## Multiple Exceptions\n```python\ntry:\n    file = open('missing.txt')\n    data = int(file.read())\nexcept FileNotFoundError:\n    print(\"File not found\")\nexcept ValueError:\n    print(\"Invalid number format\")\n```\n\\n\\n## Common Use Cases\\nPractical applications of Error Handling in real projects.\\n\\n## Catch All Exceptions\n```python\ntry:\n    risky_operation()\nexcept Exception as e:\n    print(f\"Error occurred: {e}\")\n```\n",
  "advanced": "# Error Handling - Advanced\\n\\n## Internals and Implementation\\nDeep dive into how Error Handling works under the hood.\\n\\n## Performance Considerations\\nOptimization strategies, time/space complexity, and best practices.\\n\\n## Advanced Patterns\\nComplex use cases and edge cases for Error Handling.\\n\\n## Finally Block\nAlways executes, for cleanup:\n\n```python\ntry:\n    f = open('file.txt')\n    process(f)\nexcept IOError:\n    print(\"Error reading file\")\nfinally:\n    f.close()  # Always closes\n```\n",
  "cheatsheet": "# Error Handling - Cheatsheet\\n\\n## Quick Reference\\n\\n```python\ntry:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print(\"Cannot divide by zero\")\n```\\n\\n```python\ntry:\n    file = open('missing.txt')\n    data = int(file.read())\nexcept FileNotFoundError:\n    print(\"File not found\")\nexcept ValueError:\n    print(\"Invalid number format\")\n```\\n\\n```python\ntry:\n    risky_operation()\nexcept Exception as e:\n    print(f\"Error occurred: {e}\")\n```\\n\\n```python\ntry:\n    f = open('file.txt')\n    process(f)\nexcept IOError:\n    print(\"Error reading file\")\nfinally:\n    f.close()  # Always closes\n```\\n\\n```python\ndef withdraw(amount):\n    if amount < 0:\n        raise ValueError(\"Amount must be positive\")\n    if amount > balance:\n        raise ValueError(\"Insufficient funds\")\n```\\n\\n## Key Points\\n- Essential syntax and patterns for Error Handling\\n- Common operations and gotchas\\n"
}),
    },

    # Level 2 - Core Skills (5 nodes, 220px spacing)
    {
        "name": "Functions Advanced",
        "slug": "functions-advanced",
        "description": "Advanced function concepts and patterns",
        "position_x": 220,
        "position_y": 240,
        "keywords": ["*args", "**kwargs", "closures", "lambda", "functools", "partial"],
        "parent_slug": "data-types",
        "order_index": 0,
        "topic": "oop",
        "theory": json.dumps({
  "beginner": "# Functions Advanced - Beginner\\n\\n## Introduction\\n# Advanced Functions\n\\n\\n## Basic Concepts\\n## Variable Arguments\n\n### *args (Positional)\n```python\ndef sum_all(*args):\n    return sum(args)\n\nsum_all(1, 2, 3, 4)  # 10\n```\n\n### **kwargs (Keyword)\n```python\ndef print_info(**kwargs):\n    for key, value in kwargs.items():\n        print(f\"{key}: {value}\")\n\nprint_info(name=\"Alice\", age=30)\n```\n\\n\\n## When to Use\\nUse Functions Advanced when you need to work with these fundamental concepts.\\n",
  "intermediate": "# Functions Advanced - Intermediate\\n\\n## Advanced Patterns\\nBuilding on the basics with practical, real-world patterns.\\n\\n## Lambda Functions\nAnonymous, single-expression functions:\n\n```python\nsquare = lambda x: x ** 2\nadd = lambda x, y: x + y\n\n# Common with map/filter\nnumbers = [1, 2, 3, 4]\nsquared = list(map(lambda x: x**2, numbers))\n```\n\\n\\n## Common Use Cases\\nPractical applications of Functions Advanced in real projects.\\n\\n## Closures\nFunctions that remember enclosing scope:\n\n```python\ndef outer(x):\n    def inner(y):\n        return x + y\n    return inner\n\nadd_5 = outer(5)\nprint(add_5(3))  # 8\n```\n",
  "advanced": "# Functions Advanced - Advanced\\n\\n## Internals and Implementation\\nDeep dive into how Functions Advanced works under the hood.\\n\\n## Performance Considerations\\nOptimization strategies, time/space complexity, and best practices.\\n\\n## Advanced Patterns\\nComplex use cases and edge cases for Functions Advanced.\\n\\n## functools Module\n\n### partial\nPre-fill function arguments:\n\n```python\nfrom functools import partial\n\ndef power(base, exponent):\n    return base ** exponent\n\nsquare = partial(power, exponent=2)\ncube = partial(power, exponent=3)\n\nsquare(5)  # 25\ncube(2)    # 8\n```\n\n### reduce\nCumulative operations:\n\n```python\nfrom functools import reduce\n\nnumbers = [1, 2, 3, 4]\nproduct = reduce(lambda x, y: x * y, numbers)\n# 24\n```\n",
  "cheatsheet": "# Functions Advanced - Cheatsheet\\n\\n## Quick Reference\\n\\n```python\ndef sum_all(*args):\n    return sum(args)\n\nsum_all(1, 2, 3, 4)  # 10\n```\\n\\n```python\ndef print_info(**kwargs):\n    for key, value in kwargs.items():\n        print(f\"{key}: {value}\")\n\nprint_info(name=\"Alice\", age=30)\n```\\n\\n```python\nsquare = lambda x: x ** 2\nadd = lambda x, y: x + y\n\n# Common with map/filter\nnumbers = [1, 2, 3, 4]\nsquared = list(map(lambda x: x**2, numbers))\n```\\n\\n```python\ndef outer(x):\n    def inner(y):\n        return x + y\n    return inner\n\nadd_5 = outer(5)\nprint(add_5(3))  # 8\n```\\n\\n```python\nfrom functools import partial\n\ndef power(base, exponent):\n    return base ** exponent\n\nsquare = partial(power, exponent=2)\ncube = partial(power, exponent=3)\n\nsquare(5)  # 25\ncube(2)    # 8\n```\\n\\n## Key Points\\n- Essential syntax and patterns for Functions Advanced\\n- Common operations and gotchas\\n"
}),
    },
    {
        "name": "OOP Basics",
        "slug": "oop-basics",
        "description": "Object-oriented programming fundamentals",
        "position_x": 440,
        "position_y": 240,
        "keywords": ["class", "__init__", "self", "instance", "class attributes", "methods"],
        "parent_slug": "data-types",
        "order_index": 1,
        "topic": "oop",
        "theory": json.dumps({
  "beginner": "# OOP Basics - Beginner\\n\\n## Introduction\\n# Object-Oriented Programming Basics\n\\n\\n## Basic Concepts\\n## Defining Classes\n```python\nclass Dog:\n    # Class attribute (shared)\n    species = \"Canis familiaris\"\n\n    # Constructor\n    def __init__(self, name, age):\n        # Instance attributes\n        self.name = name\n        self.age = age\n\n    # Instance method\n    def bark(self):\n        return f\"{self.name} says woof!\"\n\n    # Class method\n    @classmethod\n    def get_species(cls):\n        return cls.species\n\n    # Static method\n    @staticmethod\n    def is_adult(age):\n        return age >= 2\n```\n\\n\\n## When to Use\\nUse OOP Basics when you need to work with these fundamental concepts.\\n",
  "intermediate": "# OOP Basics - Intermediate\\n\\n## Advanced Patterns\\nBuilding on the basics with practical, real-world patterns.\\n\\n## Creating Instances\n```python\nbuddy = Dog(\"Buddy\", 3)\nprint(buddy.name)      # \"Buddy\"\nprint(buddy.bark())    # \"Buddy says woof!\"\n```\n\\n\\n## Common Use Cases\\nPractical applications of OOP Basics in real projects.\\n\\n## Instance vs Class Attributes\n```python\nclass Counter:\n    count = 0  # Class attribute\n\n    def __init__(self):\n        Counter.count += 1\n        self.id = Counter.count  # Instance\n\nc1 = Counter()  # c1.id = 1\nc2 = Counter()  # c2.id = 2\n```\n",
  "advanced": "# OOP Basics - Advanced\\n\\n## Internals and Implementation\\nDeep dive into how OOP Basics works under the hood.\\n\\n## Performance Considerations\\nOptimization strategies, time/space complexity, and best practices.\\n\\n## Advanced Patterns\\nComplex use cases and edge cases for OOP Basics.\\n\\n## The `self` Parameter\n- `self` refers to the instance\n- Always first parameter in instance methods\n- Not passed explicitly when calling\n",
  "cheatsheet": "# OOP Basics - Cheatsheet\\n\\n## Quick Reference\\n\\n```python\\nclass Dog:\\n    species = \\\"Canis familiaris\\\"  # Class attribute\\n\\n    def __init__(self, name, age):\\n        self.name = name\\n        self.age = age\\n\\n    def bark(self):\\n        return f\\\"{self.name} says woof!\\\"\\n```\\n\\n```python\\nbuddy = Dog(\\\"Buddy\\\", 3)\\nprint(buddy.name)   # \\\"Buddy\\\"\\nprint(buddy.bark()) # \\\"Buddy says woof!\\\"\\n```\\n\\n```python\\nclass Counter:\\n    count = 0  # Class attribute\\n\\n    def __init__(self):\\n        Counter.count += 1\\n        self.id = Counter.count\\n\\nc1 = Counter()  # c1.id = 1\\nc2 = Counter()  # c2.id = 2\\n```\\n\\n```python\\nclass Temperature:\\n    def __init__(self, celsius):\\n        self._celsius = celsius\\n\\n    @property\\n    def fahrenheit(self):\\n        return self._celsius * 9/5 + 32\\n\\ntemp = Temperature(25)\\nprint(temp.fahrenheit)  # 77.0\\n```\\n\\n## Key Points\\n- Classes define blueprints for objects\\n- `__init__` is the constructor\\n- `self` refers to the instance\\n- Class attributes are shared, instance attributes are unique\\n"
}),
    },
    {
        "name": "Regular Expressions",
        "slug": "regex",
        "description": "Pattern matching with the re module",
        "position_x": 660,
        "position_y": 240,
        "keywords": ["re module", "patterns", "match", "search", "groups", "substitution"],
        "parent_slug": "data-types",
        "order_index": 2,
        "topic": "data-structures",
        "theory": REGEX_THEORY,
    },
    {
        "name": "String Manipulation",
        "slug": "string-manipulation",
        "description": "Advanced string methods and formatting",
        "position_x": 880,
        "position_y": 240,
        "keywords": ["format", "f-strings", "join", "split", "encode", "decode"],
        "parent_slug": "data-types",
        "order_index": 3,
        "topic": "data-structures",
        "theory": STRING_THEORY,
    },
    {
        "name": "Collections Module",
        "slug": "collections-module",
        "description": "Specialized container datatypes",
        "position_x": 1100,
        "position_y": 240,
        "keywords": ["defaultdict", "Counter", "deque", "namedtuple", "OrderedDict"],
        "parent_slug": "data-types",
        "order_index": 4,
        "topic": "data-structures",
        "theory": COLLECTIONS_THEORY,
    },

    # Level 3 - Practical Development (7 nodes, 220px spacing)
    {
        "name": "Decorators",
        "slug": "decorators",
        "description": "Function and class decorators",
        "position_x": 0,
        "position_y": 360,
        "keywords": ["@decorator", "functools.wraps", "parameterized decorators", "class decorators"],
        "parent_slug": "functions-advanced",
        "order_index": 0,
        "topic": "oop",
        "theory": json.dumps({
  "beginner": "# Decorators - Beginner\\n\\n## Introduction\\n# Decorators\n\\n\\n## Basic Concepts\\n## Basic Function Decorator\nModify or enhance functions without changing their code:\n\n```python\ndef timing_decorator(func):\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        end = time.time()\n        print(f\"{func.__name__} took {end-start:.2f}s\")\n        return result\n    return wrapper\n\n@timing_decorator\ndef slow_function():\n    time.sleep(1)\n```\n\\n\\n## When to Use\\nUse Decorators when you need to work with these fundamental concepts.\\n",
  "intermediate": "# Decorators - Intermediate\\n\\n## Advanced Patterns\\nBuilding on the basics with practical, real-world patterns.\\n\\n## Using functools.wraps\nPreserve original function metadata:\n\n```python\nfrom functools import wraps\n\ndef my_decorator(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        return func(*args, **kwargs)\n    return wrapper\n```\n\\n\\n## Common Use Cases\\nPractical applications of Decorators in real projects.\\n\\n## Parameterized Decorators\nDecorators that accept arguments:\n\n```python\ndef repeat(times):\n    def decorator(func):\n        @wraps(func)\n        def wrapper(*args, **kwargs):\n            for _ in range(times):\n                result = func(*args, **kwargs)\n            return result\n        return wrapper\n    return decorator\n\n@repeat(times=3)\ndef greet(name):\n    print(f\"Hello, {name}!\")\n```\n",
  "advanced": "# Decorators - Advanced\\n\\n## Internals and Implementation\\nDeep dive into how Decorators works under the hood.\\n\\n## Performance Considerations\\nOptimization strategies, time/space complexity, and best practices.\\n\\n## Advanced Patterns\\nComplex use cases and edge cases for Decorators.\\n\\n## Class Decorators\nModify classes:\n\n```python\ndef add_str_method(cls):\n    cls.__str__ = lambda self: f\"{cls.__name__} instance\"\n    return cls\n\n@add_str_method\nclass MyClass:\n    pass\n```\n",
  "cheatsheet": "# Decorators - Cheatsheet\\n\\n## Quick Reference\\n\\n### Basic Decorator\\n```python\\ndef timing_decorator(func):\\n    def wrapper(*args, **kwargs):\\n        start = time.time()\\n        result = func(*args, **kwargs)\\n        print(f\\\"{func.__name__} took {time.time()-start:.2f}s\\\")\\n        return result\\n    return wrapper\\n\\n@timing_decorator\\ndef slow_function():\\n    time.sleep(1)\\n```\\n\\n### With functools.wraps\\n```python\\nfrom functools import wraps\\n\\ndef my_decorator(func):\\n    @wraps(func)  # Preserves metadata\\n    def wrapper(*args, **kwargs):\\n        return func(*args, **kwargs)\\n    return wrapper\\n```\\n\\n### Parameterized Decorator\\n```python\\ndef repeat(times):\\n    def decorator(func):\\n        @wraps(func)\\n        def wrapper(*args, **kwargs):\\n            for _ in range(times):\\n                result = func(*args, **kwargs)\\n            return result\\n        return wrapper\\n    return decorator\\n\\n@repeat(times=3)\\ndef greet(name):\\n    print(f\\\"Hello, {name}!\\\")\\n```\\n\\n### Stacking Decorators\\n```python\\n@login_required\\n@rate_limit(calls=100)\\ndef api_endpoint(request):\\n    return process_request(request)\\n```\\n\\n## Key Points\\n- Decorators wrap functions to add behavior\\n- Use @wraps to preserve function metadata\\n- Order matters when stacking decorators\\n"
}),
    },
    {
        "name": "Dunder Methods",
        "slug": "dunder-methods",
        "description": "Magic methods for operator overloading and protocols",
        "position_x": 220,
        "position_y": 360,
        "keywords": ["__str__", "__repr__", "__eq__", "__hash__", "__call__", "__len__", "__getitem__"],
        "parent_slug": "oop-basics",
        "order_index": 0,
        "topic": "oop",
    },
    {
        "name": "Inheritance & Composition",
        "slug": "inheritance",
        "description": "Class hierarchies and composition patterns",
        "position_x": 440,
        "position_y": 360,
        "keywords": ["super()", "MRO", "multiple inheritance", "mixins", "ABC", "composition"],
        "parent_slug": "oop-basics",
        "order_index": 1,
        "topic": "oop",
        "theory": json.dumps({
  "beginner": "# Inheritance & Composition - Beginner\\n\\n## Introduction\\n# Inheritance & Composition\n\\n\\n## Basic Concepts\\n## Basic Inheritance\n```python\nclass Animal:\n    def __init__(self, name):\n        self.name = name\n\n    def speak(self):\n        return \"Some sound\"\n\nclass Dog(Animal):\n    def speak(self):\n        return f\"{self.name} says Woof!\"\n\nclass Cat(Animal):\n    def speak(self):\n        return f\"{self.name} says Meow!\"\n\ndog = Dog(\"Buddy\")\ndog.speak()  # \"Buddy says Woof!\"\n```\n\\n\\n## When to Use\\nUse Inheritance & Composition when you need to work with these fundamental concepts.\\n",
  "intermediate": "# Inheritance & Composition - Intermediate\\n\\n## Advanced Patterns\\nBuilding on the basics with practical, real-world patterns.\\n\\n## super() Function\nCall parent methods:\n\n```python\nclass Employee:\n    def __init__(self, name, salary):\n        self.name = name\n        self.salary = salary\n\nclass Manager(Employee):\n    def __init__(self, name, salary, department):\n        super().__init__(name, salary)\n        self.department = department\n```\n\\n\\n## Common Use Cases\\nPractical applications of Inheritance & Composition in real projects.\\n\\n## Multiple Inheritance\n```python\nclass Flyable:\n    def fly(self):\n        return \"Flying!\"\n\nclass Swimmable:\n    def swim(self):\n        return \"Swimming!\"\n\nclass Duck(Flyable, Swimmable):\n    pass\n\nduck = Duck()\nduck.fly()   # \"Flying!\"\nduck.swim()  # \"Swimming!\"\n```\n",
  "advanced": "# Inheritance & Composition - Advanced\\n\\n## Internals and Implementation\\nDeep dive into how Inheritance & Composition works under the hood.\\n\\n## Performance Considerations\\nOptimization strategies, time/space complexity, and best practices.\\n\\n## Advanced Patterns\\nComplex use cases and edge cases for Inheritance & Composition.\\n\\n## Method Resolution Order (MRO)\n```python\nclass A:\n    def method(self):\n        return \"A\"\n\nclass B(A):\n    def method(self):\n        return \"B\"\n\nclass C(A):\n    def method(self):\n        return \"C\"\n\nclass D(B, C):\n    pass\n\n# Check MRO\nD.__mro__\n# (<class 'D'>, <class 'B'>, <class 'C'>,\n#  <class 'A'>, <class 'object'>)\n\nd = D()\nd.method()  # \"B\" (searches left to right)\n```\n",
  "cheatsheet": "# Inheritance & Composition - Cheatsheet\\n\\n## Quick Reference\\n\\n### Basic Inheritance\\n```python\\nclass Animal:\\n    def __init__(self, name):\\n        self.name = name\\n    def speak(self):\\n        return \\\"Some sound\\\"\\n\\nclass Dog(Animal):\\n    def speak(self):\\n        return f\\\"{self.name} says Woof!\\\"\\n\\ndog = Dog(\\\"Buddy\\\")\\ndog.speak()  # \\\"Buddy says Woof!\\\"\\n```\\n\\n### super() Function\\n```python\\nclass Manager(Employee):\\n    def __init__(self, name, salary, dept):\\n        super().__init__(name, salary)\\n        self.department = dept\\n```\\n\\n### Multiple Inheritance\\n```python\\nclass Duck(Flyable, Swimmable):\\n    pass\\n\\nduck = Duck()\\nduck.fly()   # From Flyable\\nduck.swim()  # From Swimmable\\n```\\n\\n### Method Resolution Order\\n```python\\nclass D(B, C):\\n    pass\\n\\nD.__mro__  # D -> B -> C -> A -> object\\nd = D()\\nd.method()  # Searches left to right\\n```\\n\\n### Composition over Inheritance\\n```python\\nclass Engine:\\n    def start(self):\\n        return \\\"Engine started\\\"\\n\\nclass Car:\\n    def __init__(self):\\n        self.engine = Engine()  # Has-a\\n    def start(self):\\n        return self.engine.start()\\n```\\n\\n## Key Points\\n- Use inheritance for \\\"is-a\\\" relationships\\n- Use composition for \\\"has-a\\\" relationships\\n- super() calls parent methods\\n- MRO determines method search order\\n"
}),
    },
    {
        "name": "Context Managers",
        "slug": "context-managers",
        "description": "Resource management with context managers",
        "position_x": 660,
        "position_y": 360,
        "keywords": ["with", "__enter__", "__exit__", "contextlib", "@contextmanager"],
        "parent_slug": "functions-advanced",
        "order_index": 1,
        "topic": "oop",
        "theory": json.dumps({
  "beginner": "# Context Managers - Beginner\\n\\n## Introduction\\n# Context Managers\n\\n\\n## Basic Concepts\\n## The `with` Statement\nAutomatically handles setup and cleanup:\n\n```python\nwith open('file.txt') as f:\n    content = f.read()\n# File automatically closed\n```\n\\n\\n## When to Use\\nUse Context Managers when you need to work with these fundamental concepts.\\n",
  "intermediate": "# Context Managers - Intermediate\\n\\n## Advanced Patterns\\nBuilding on the basics with practical, real-world patterns.\\n\\n## Protocol Methods\n\n### __enter__ and __exit__\n```python\nclass DatabaseConnection:\n    def __enter__(self):\n        self.conn = create_connection()\n        return self.conn\n\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        self.conn.close()\n        # Return True to suppress exceptions\n        return False\n\nwith DatabaseConnection() as conn:\n    conn.execute('SELECT * FROM users')\n```\n\\n\\n## Common Use Cases\\nPractical applications of Context Managers in real projects.\\n\\n## Using contextlib\n\n### @contextmanager Decorator\n```python\nfrom contextlib import contextmanager\n\n@contextmanager\ndef temporary_file(filename):\n    f = open(filename, 'w')\n    try:\n        yield f\n    finally:\n        f.close()\n        os.remove(filename)\n\nwith temporary_file('temp.txt') as f:\n    f.write('Hello')\n```\n\n### suppress\nIgnore specific exceptions:\n\n```python\nfrom contextlib import suppress\n\nwith suppress(FileNotFoundError):\n    os.remove('nonexistent.txt')\n```\n\n### redirect_stdout\nCapture print output:\n\n```python\nfrom contextlib import redirect_stdout\nimport io\n\nf = io.StringIO()\nwith redirect_stdout(f):\n    print('Hello')\noutput = f.getvalue()  # 'Hello\\\\n'\n```\n",
  "advanced": "# Context Managers - Advanced\\n\\n## Internals and Implementation\\nDeep dive into how Context Managers works under the hood.\\n\\n## Performance Considerations\\nOptimization strategies, time/space complexity, and best practices.\\n\\n## Advanced Patterns\\nComplex use cases and edge cases for Context Managers.\\n\\n## Real-World Examples\n\n### Database Transaction\n```python\n@contextmanager\ndef transaction(db):\n    try:\n        yield db\n        db.commit()\n    except Exception:\n        db.rollback()\n        raise\n\nwith transaction(db) as conn:\n    conn.execute('INSERT ...')\n```\n\n### Timer Context\n```python\n@contextmanager\ndef timer(name):\n    start = time.time()\n    yield\n    print(f\"{name}: {time.time()-start:.2f}s\")\n\nwith timer('Processing'):\n    expensive_operation()\n```\n",
  "cheatsheet": "# Context Managers - Cheatsheet\\n\\n## Quick Reference\\n\\n```python\nwith open('file.txt') as f:\n    content = f.read()\n# File automatically closed\n```\\n\\n```python\nclass DatabaseConnection:\n    def __enter__(self):\n        self.conn = create_connection()\n        return self.conn\n\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        self.conn.close()\n        # Return True to suppress exceptions\n        return False\n\nwith DatabaseConnection() as conn:\n   ```\\n\\n```python\nfrom contextlib import contextmanager\n\n@contextmanager\ndef temporary_file(filename):\n    f = open(filename, 'w')\n    try:\n        yield f\n    finally:\n        f.close()\n        os.remove(filename)\n\nwith temporary_file('temp.txt') as f:\n    f.write('Hello')\n```\\n\\n```python\nfrom contextlib import suppress\n\nwith suppress(FileNotFoundError):\n    os.remove('nonexistent.txt')\n```\\n\\n```python\nfrom contextlib import redirect_stdout\nimport io\n\nf = io.StringIO()\nwith redirect_stdout(f):\n    print('Hello')\noutput = f.getvalue()  # 'Hello\\\\n'\n```\\n\\n## Key Points\\n- Essential syntax and patterns for Context Managers\\n- Common operations and gotchas\\n"
}),
    },
    {
        "name": "Logging & Debugging",
        "slug": "logging-debugging",
        "description": "Logging module and debugging techniques",
        "position_x": 880,
        "position_y": 360,
        "keywords": ["logging module", "pdb", "breakpoint", "traceback", "handlers"],
        "parent_slug": "error-handling",
        "order_index": 0,
        "topic": "tooling",
    },
    {
        "name": "Testing Fundamentals",
        "slug": "testing-basics",
        "description": "Unit testing and test frameworks",
        "position_x": 1100,
        "position_y": 360,
        "keywords": ["unittest", "pytest", "assertions", "fixtures", "mocking"],
        "parent_slug": "functions-advanced",
        "order_index": 2,
        "topic": "tooling",
        "theory": json.dumps({
  "beginner": "# Testing Fundamentals - Beginner\\n\\n## Introduction\\n# Testing Fundamentals\n\\n\\n## Basic Concepts\\n## unittest (Built-in)\n```python\nimport unittest\n\nclass TestMath(unittest.TestCase):\n    def test_addition(self):\n        self.assertEqual(2 + 2, 4)\n\n    def test_subtraction(self):\n        self.assertEqual(5 - 3, 2)\n\n    def setUp(self):\n        # Runs before each test\n        self.value = 10\n\n    def tearDown(self):\n        # Runs after each test\n        pass\n\nif __name__ == '__main__':\n    unittest.main()\n```\n\\n\\n## When to Use\\nUse Testing Fundamentals when you need to work with these fundamental concepts.\\n",
  "intermediate": "# Testing Fundamentals - Intermediate\\n\\n## Advanced Patterns\\nBuilding on the basics with practical, real-world patterns.\\n\\n## pytest (Recommended)\nSimpler syntax, more powerful:\n\n```python\n# test_math.py\ndef test_addition():\n    assert 2 + 2 == 4\n\ndef test_division():\n    assert 10 / 2 == 5\n\n# Run with: pytest test_math.py\n```\n\\n\\n## Common Use Cases\\nPractical applications of Testing Fundamentals in real projects.\\n\\n## Fixtures\nSetup and teardown:\n\n```python\nimport pytest\n\n@pytest.fixture\ndef sample_data():\n    return [1, 2, 3, 4, 5]\n\ndef test_sum(sample_data):\n    assert sum(sample_data) == 15\n\ndef test_length(sample_data):\n    assert len(sample_data) == 5\n```\n",
  "advanced": "# Testing Fundamentals - Advanced\\n\\n## Internals and Implementation\\nDeep dive into how Testing Fundamentals works under the hood.\\n\\n## Performance Considerations\\nOptimization strategies, time/space complexity, and best practices.\\n\\n## Advanced Patterns\\nComplex use cases and edge cases for Testing Fundamentals.\\n\\n## Parametrized Tests\nTest multiple inputs:\n\n```python\n@pytest.mark.parametrize(\"input,expected\", [\n    (2, 4),\n    (3, 9),\n    (4, 16),\n])\ndef test_square(input, expected):\n    assert input ** 2 == expected\n```\n",
  "cheatsheet": "# Testing Fundamentals - Cheatsheet\\n\\n## Quick Reference\\n\\n```python\nimport unittest\n\nclass TestMath(unittest.TestCase):\n    def test_addition(self):\n        self.assertEqual(2 + 2, 4)\n\n    def test_subtraction(self):\n        self.assertEqual(5 - 3, 2)\n\n    def setUp(self):\n        # Runs before each test\n        self.value = 10\n\n    def tearDown(self):\n        # Ru```\\n\\n```python\n# test_math.py\ndef test_addition():\n    assert 2 + 2 == 4\n\ndef test_division():\n    assert 10 / 2 == 5\n\n# Run with: pytest test_math.py\n```\\n\\n```python\nimport pytest\n\n@pytest.fixture\ndef sample_data():\n    return [1, 2, 3, 4, 5]\n\ndef test_sum(sample_data):\n    assert sum(sample_data) == 15\n\ndef test_length(sample_data):\n    assert len(sample_data) == 5\n```\\n\\n```python\n@pytest.mark.parametrize(\"input,expected\", [\n    (2, 4),\n    (3, 9),\n    (4, 16),\n])\ndef test_square(input, expected):\n    assert input ** 2 == expected\n```\\n\\n```python\nfrom unittest.mock import Mock, patch\n\ndef test_api_call():\n    # Mock external API\n    with patch('requests.get') as mock_get:\n        mock_get.return_value.json.return_value = {'status': 'ok'}\n\n        result = fetch_data()\n        assert result['status'] == 'ok'\n```\\n\\n## Key Points\\n- Essential syntax and patterns for Testing Fundamentals\\n- Common operations and gotchas\\n"
}),
    },
    {
        "name": "Packages & Modules",
        "slug": "package-management",
        "description": "Python packaging and module system",
        "position_x": 1320,
        "position_y": 360,
        "keywords": ["pip", "venv", "__init__.py", "imports", "requirements.txt", "setup.py"],
        "parent_slug": "functions-advanced",
        "order_index": 3,
        "topic": "tooling",
    },

    # Level 4 - Applied Python (7 nodes, 220px spacing)
    {
        "name": "Generators & Iterators",
        "slug": "generators",
        "description": "Lazy evaluation and iteration protocols",
        "position_x": 0,
        "position_y": 480,
        "keywords": ["yield", "generator expression", "__iter__", "__next__", "itertools"],
        "parent_slug": "decorators",
        "order_index": 0,
        "topic": "concurrency",
        "theory": json.dumps({
  "beginner": "# Generators & Iterators - Beginner\\n\\n## Introduction\\n# Generators & Iterators\n\\n\\n## Basic Concepts\\n## Generator Functions\nUse `yield` to produce values lazily:\n\n```python\ndef countdown(n):\n    while n > 0:\n        yield n\n        n -= 1\n\nfor i in countdown(5):\n    print(i)  # 5, 4, 3, 2, 1\n```\n\\n\\n## When to Use\\nUse Generators & Iterators when you need to work with these fundamental concepts.\\n",
  "intermediate": "# Generators & Iterators - Intermediate\\n\\n## Advanced Patterns\\nBuilding on the basics with practical, real-world patterns.\\n\\n## Memory Efficiency\nGenerators don't store all values in memory:\n\n```python\n# Bad: Creates list of 1M numbers\nnumbers = [x**2 for x in range(1000000)]\n\n# Good: Generates on demand\nnumbers = (x**2 for x in range(1000000))\n```\n\\n\\n## Common Use Cases\\nPractical applications of Generators & Iterators in real projects.\\n\\n## Generator Expressions\nCompact syntax like list comprehensions:\n\n```python\n# List comprehension\nsquares_list = [x**2 for x in range(10)]\n\n# Generator expression\nsquares_gen = (x**2 for x in range(10))\n```\n",
  "advanced": "# Generators & Iterators - Advanced\\n\\n## Internals and Implementation\\nDeep dive into how Generators & Iterators works under the hood.\\n\\n## Performance Considerations\\nOptimization strategies, time/space complexity, and best practices.\\n\\n## Advanced Patterns\\nComplex use cases and edge cases for Generators & Iterators.\\n\\n## Iterator Protocol\n```python\nclass Counter:\n    def __init__(self, max):\n        self.max = max\n        self.current = 0\n\n    def __iter__(self):\n        return self\n\n    def __next__(self):\n        if self.current < self.max:\n            self.current += 1\n            return self.current\n        raise StopIteration\n\nfor i in Counter(5):\n    print(i)  # 1, 2, 3, 4, 5\n```\n",
  "cheatsheet": "# Generators & Iterators - Cheatsheet\\n\\n## Quick Reference\\n\\n```python\ndef countdown(n):\n    while n > 0:\n        yield n\n        n -= 1\n\nfor i in countdown(5):\n    print(i)  # 5, 4, 3, 2, 1\n```\\n\\n```python\n# Bad: Creates list of 1M numbers\nnumbers = [x**2 for x in range(1000000)]\n\n# Good: Generates on demand\nnumbers = (x**2 for x in range(1000000))\n```\\n\\n```python\n# List comprehension\nsquares_list = [x**2 for x in range(10)]\n\n# Generator expression\nsquares_gen = (x**2 for x in range(10))\n```\\n\\n```python\nclass Counter:\n    def __init__(self, max):\n        self.max = max\n        self.current = 0\n\n    def __iter__(self):\n        return self\n\n    def __next__(self):\n        if self.current < self.max:\n            self.current += 1\n            return self.current\n        raise StopIteration\n\nfor i in C```\\n\\n```python\nfrom itertools import *\n\n# Infinite iterators\ncount(10)          # 10, 11, 12, ...\ncycle([1, 2, 3])   # 1, 2, 3, 1, 2, 3, ...\n\n# Finite iterators\nchain([1, 2], [3, 4])      # 1, 2, 3, 4\nislice(range(10), 5)       # 0, 1, 2, 3, 4\ncombinations([1,2,3], 2)   # (1,2), (1,3), (2,3)\n```\\n\\n## Key Points\\n- Essential syntax and patterns for Generators & Iterators\\n- Common operations and gotchas\\n"
}),
    },
    {
        "name": "Type Hints",
        "slug": "type-hints",
        "description": "Static typing and type annotations",
        "position_x": 220,
        "position_y": 480,
        "keywords": ["typing", "Generic", "Protocol", "TypeVar", "Union", "Optional", "mypy"],
        "parent_slug": "dunder-methods",
        "order_index": 0,
        "topic": "typing",
        "theory": json.dumps({
  "beginner": "# Type Hints - Beginner\\n\\n## Introduction\\n# Type Hints\n\\n\\n## Basic Concepts\\n## Basic Type Annotations\n```python\ndef greet(name: str) -> str:\n    return f\"Hello, {name}\"\n\nage: int = 30\nnames: list[str] = [\"Alice\", \"Bob\"]\nscores: dict[str, int] = {\"Alice\": 95}\n```\n\\n\\n## When to Use\\nUse Type Hints when you need to work with these fundamental concepts.\\n",
  "intermediate": "# Type Hints - Intermediate\\n\\n## Advanced Patterns\\nBuilding on the basics with practical, real-world patterns.\\n\\n## typing Module\n\n### Optional and Union\n```python\nfrom typing import Optional, Union\n\n# Optional[T] = Union[T, None]\ndef find_user(id: int) -> Optional[str]:\n    return users.get(id)\n\n# Union for multiple types\ndef process(data: Union[str, int]) -> str:\n    return str(data)\n```\n\n### Collections\n```python\nfrom typing import List, Dict, Set, Tuple\n\nnames: List[str] = [\"Alice\", \"Bob\"]\nages: Dict[str, int] = {\"Alice\": 30}\nunique: Set[int] = {1, 2, 3}\npoint: Tuple[int, int] = (10, 20)\n```\n\n### Callable\n```python\nfrom typing import Callable\n\ndef apply(\n    func: Callable[[int, int], int],\n    x: int,\n    y: int\n) -> int:\n    return func(x, y)\n\napply(lambda a, b: a + b, 5, 3)\n```\n\\n\\n## Common Use Cases\\nPractical applications of Type Hints in real projects.\\n\\n## Generic Types\n```python\nfrom typing import TypeVar, Generic\n\nT = TypeVar('T')\n\nclass Stack(Generic[T]):\n    def __init__(self) -> None:\n        self.items: List[T] = []\n\n    def push(self, item: T) -> None:\n        self.items.append(item)\n\n    def pop(self) -> T:\n        return self.items.pop()\n\n# Type-specific stacks\nint_stack: Stack[int] = Stack()\nstr_stack: Stack[str] = Stack()\n```\n",
  "advanced": "# Type Hints - Advanced\\n\\n## Internals and Implementation\\nDeep dive into how Type Hints works under the hood.\\n\\n## Performance Considerations\\nOptimization strategies, time/space complexity, and best practices.\\n\\n## Advanced Patterns\\nComplex use cases and edge cases for Type Hints.\\n\\n## Protocol (Structural Typing)\n```python\nfrom typing import Protocol\n\nclass Drawable(Protocol):\n    def draw(self) -> None: ...\n\ndef render(obj: Drawable) -> None:\n    obj.draw()\n\n# Any object with draw() works\nclass Circle:\n    def draw(self) -> None:\n        print(\"Drawing circle\")\n\nrender(Circle())  # OK!\n```\n",
  "cheatsheet": "# Type Hints - Cheatsheet\\n\\n## Quick Reference\\n\\n```python\ndef greet(name: str) -> str:\n    return f\"Hello, {name}\"\n\nage: int = 30\nnames: list[str] = [\"Alice\", \"Bob\"]\nscores: dict[str, int] = {\"Alice\": 95}\n```\\n\\n```python\nfrom typing import Optional, Union\n\n# Optional[T] = Union[T, None]\ndef find_user(id: int) -> Optional[str]:\n    return users.get(id)\n\n# Union for multiple types\ndef process(data: Union[str, int]) -> str:\n    return str(data)\n```\\n\\n```python\nfrom typing import List, Dict, Set, Tuple\n\nnames: List[str] = [\"Alice\", \"Bob\"]\nages: Dict[str, int] = {\"Alice\": 30}\nunique: Set[int] = {1, 2, 3}\npoint: Tuple[int, int] = (10, 20)\n```\\n\\n```python\nfrom typing import Callable\n\ndef apply(\n    func: Callable[[int, int], int],\n    x: int,\n    y: int\n) -> int:\n    return func(x, y)\n\napply(lambda a, b: a + b, 5, 3)\n```\\n\\n```python\nfrom typing import TypeVar, Generic\n\nT = TypeVar('T')\n\nclass Stack(Generic[T]):\n    def __init__(self) -> None:\n        self.items: List[T] = []\n\n    def push(self, item: T) -> None:\n        self.items.append(item)\n\n    def pop(self) -> T:\n        return self.items.pop()\n\n# Type-specific stacks\nint```\\n\\n## Key Points\\n- Essential syntax and patterns for Type Hints\\n- Common operations and gotchas\\n"
}),
    },
    {
        "name": "Descriptors",
        "slug": "descriptors",
        "description": "Attribute access customization",
        "position_x": 440,
        "position_y": 480,
        "keywords": ["__get__", "__set__", "__delete__", "property", "data descriptors"],
        "parent_slug": "inheritance",
        "order_index": 0,
        "topic": "oop",
    },
    {
        "name": "Protocols & ABCs",
        "slug": "protocols",
        "description": "Abstract base classes and structural subtyping",
        "position_x": 660,
        "position_y": 480,
        "keywords": ["ABC", "abstractmethod", "Protocol", "runtime_checkable", "structural typing"],
        "parent_slug": "inheritance",
        "order_index": 1,
        "topic": "oop",
    },
    {
        "name": "HTTP & APIs",
        "slug": "http-requests",
        "description": "Working with HTTP requests and REST APIs",
        "position_x": 880,
        "position_y": 480,
        "keywords": ["requests", "urllib", "REST", "JSON APIs", "HTTP methods"],
        "parent_slug": "testing-basics",
        "order_index": 0,
        "topic": "web",
    },
    {
        "name": "Database Interaction",
        "slug": "database-basics",
        "description": "Database connectivity and SQL basics",
        "position_x": 1100,
        "position_y": 480,
        "keywords": ["sqlite3", "connection", "cursor", "transactions", "parameterized queries"],
        "parent_slug": "testing-basics",
        "order_index": 1,
        "topic": "database",
    },
    {
        "name": "Date & Time",
        "slug": "datetime-module",
        "description": "Date and time manipulation",
        "position_x": 1320,
        "position_y": 480,
        "keywords": ["datetime", "timedelta", "timezone", "strftime", "strptime"],
        "parent_slug": "collections-module",
        "order_index": 0,
        "topic": "data-structures",
        "theory": DATETIME_THEORY,
    },

    # Level 5 - Frameworks & Concurrency (8 nodes, 220px spacing)
    {
        "name": "Threading",
        "slug": "threading",
        "description": "Thread-based concurrency",
        "position_x": 0,
        "position_y": 600,
        "keywords": ["Thread", "Lock", "RLock", "Semaphore", "Event", "Condition", "ThreadPool"],
        "parent_slug": "generators",
        "order_index": 0,
        "topic": "concurrency",
    },
    {
        "name": "Multiprocessing",
        "slug": "multiprocessing",
        "description": "Process-based parallelism",
        "position_x": 220,
        "position_y": 600,
        "keywords": ["Process", "Pool", "Queue", "Pipe", "shared memory", "ProcessPoolExecutor"],
        "parent_slug": "generators",
        "order_index": 1,
        "topic": "concurrency",
    },
    {
        "name": "AsyncIO",
        "slug": "asyncio",
        "description": "Asynchronous I/O and event loops",
        "position_x": 440,
        "position_y": 600,
        "keywords": ["async", "await", "asyncio", "coroutines", "gather", "create_task", "aiohttp"],
        "parent_slug": "type-hints",
        "order_index": 0,
        "topic": "concurrency",
        "theory": json.dumps({
  "beginner": "# AsyncIO - Beginner\\n\\n## Introduction\\n# AsyncIO\n\\n\\n## Basic Concepts\\n## Async/Await Syntax\n```python\nimport asyncio\n\nasync def fetch_data(url):\n    # Simulate network request\n    await asyncio.sleep(1)\n    return f\"Data from {url}\"\n\nasync def main():\n    result = await fetch_data(\"example.com\")\n    print(result)\n\n# Run the async function\nasyncio.run(main())\n```\n\\n\\n## When to Use\\nUse AsyncIO when you need to work with these fundamental concepts.\\n",
  "intermediate": "# AsyncIO - Intermediate\\n\\n## Advanced Patterns\\nBuilding on the basics with practical, real-world patterns.\\n\\n## Running Multiple Coroutines\n\n### gather() - Run concurrently\n```python\nasync def main():\n    results = await asyncio.gather(\n        fetch_data(\"site1.com\"),\n        fetch_data(\"site2.com\"),\n        fetch_data(\"site3.com\")\n    )\n    # All complete in ~1 second (parallel)\n```\n\n### create_task() - Fire and forget\n```python\nasync def main():\n    task1 = asyncio.create_task(fetch_data(\"a.com\"))\n    task2 = asyncio.create_task(fetch_data(\"b.com\"))\n\n    # Do other work\n    await some_other_work()\n\n    # Wait for tasks\n    result1 = await task1\n    result2 = await task2\n```\n\\n\\n## Common Use Cases\\nPractical applications of AsyncIO in real projects.\\n\\n## Async Context Managers\n```python\nclass AsyncDB:\n    async def __aenter__(self):\n        await self.connect()\n        return self\n\n    async def __aexit__(self, *args):\n        await self.disconnect()\n\nasync with AsyncDB() as db:\n    await db.query(\"SELECT * FROM users\")\n```\n",
  "advanced": "# AsyncIO - Advanced\\n\\n## Internals and Implementation\\nDeep dive into how AsyncIO works under the hood.\\n\\n## Performance Considerations\\nOptimization strategies, time/space complexity, and best practices.\\n\\n## Advanced Patterns\\nComplex use cases and edge cases for AsyncIO.\\n\\n## Async Iterators\n```python\nclass AsyncRange:\n    def __init__(self, n):\n        self.n = n\n        self.i = 0\n\n    def __aiter__(self):\n        return self\n\n    async def __anext__(self):\n        if self.i < self.n:\n            await asyncio.sleep(0.1)\n            self.i += 1\n            return self.i\n        raise StopAsyncIteration\n\nasync for i in AsyncRange(5):\n    print(i)\n```\n",
  "cheatsheet": "# AsyncIO - Cheatsheet\\n\\n## Quick Reference\\n\\n```python\nimport asyncio\n\nasync def fetch_data(url):\n    # Simulate network request\n    await asyncio.sleep(1)\n    return f\"Data from {url}\"\n\nasync def main():\n    result = await fetch_data(\"example.com\")\n    print(result)\n\n# Run the async function\nasyncio.run(main())\n```\\n\\n```python\nasync def main():\n    results = await asyncio.gather(\n        fetch_data(\"site1.com\"),\n        fetch_data(\"site2.com\"),\n        fetch_data(\"site3.com\")\n    )\n    # All complete in ~1 second (parallel)\n```\\n\\n```python\nasync def main():\n    task1 = asyncio.create_task(fetch_data(\"a.com\"))\n    task2 = asyncio.create_task(fetch_data(\"b.com\"))\n\n    # Do other work\n    await some_other_work()\n\n    # Wait for tasks\n    result1 = await task1\n    result2 = await task2\n```\\n\\n```python\nclass AsyncDB:\n    async def __aenter__(self):\n        await self.connect()\n        return self\n\n    async def __aexit__(self, *args):\n        await self.disconnect()\n\nasync with AsyncDB() as db:\n    await db.query(\"SELECT * FROM users\")\n```\\n\\n```python\nclass AsyncRange:\n    def __init__(self, n):\n        self.n = n\n        self.i = 0\n\n    def __aiter__(self):\n        return self\n\n    async def __anext__(self):\n        if self.i < self.n:\n            await asyncio.sleep(0.1)\n            self.i += 1\n            return self.i\n        raise StopAsync```\\n\\n## Key Points\\n- Essential syntax and patterns for AsyncIO\\n- Common operations and gotchas\\n"
}),
    },
    {
        "name": "GIL & Concurrency",
        "slug": "gil",
        "description": "Understanding Python's Global Interpreter Lock",
        "position_x": 660,
        "position_y": 600,
        "keywords": ["GIL", "CPU-bound", "I/O-bound", "concurrent.futures", "parallelism vs concurrency"],
        "parent_slug": "type-hints",
        "order_index": 1,
        "topic": "concurrency",
    },
    {
        "name": "Flask & FastAPI",
        "slug": "flask-fastapi",
        "description": "Web frameworks for building APIs",
        "position_x": 880,
        "position_y": 600,
        "keywords": ["Flask", "FastAPI", "routing", "templates", "middleware", "Pydantic"],
        "parent_slug": "http-requests",
        "order_index": 0,
        "topic": "web",
    },
    {
        "name": "Django Framework",
        "slug": "django-framework",
        "description": "Full-stack web framework",
        "position_x": 1100,
        "position_y": 600,
        "keywords": ["Django", "MTV", "ORM", "admin", "migrations", "views"],
        "parent_slug": "http-requests",
        "order_index": 1,
        "topic": "web",
    },
    {
        "name": "ORM Patterns",
        "slug": "orm-patterns",
        "description": "Object-Relational Mapping with SQLAlchemy",
        "position_x": 1320,
        "position_y": 600,
        "keywords": ["SQLAlchemy", "models", "relationships", "queries", "sessions"],
        "parent_slug": "database-basics",
        "order_index": 0,
        "topic": "database",
    },
    {
        "name": "Data Processing",
        "slug": "data-processing",
        "description": "Processing structured data files",
        "position_x": 1540,
        "position_y": 600,
        "keywords": ["csv", "json", "xml", "data pipelines", "ETL"],
        "parent_slug": "database-basics",
        "order_index": 1,
        "topic": "data-science",
    },

    # Level 6 - Advanced (4 nodes)
    {
        "name": "Memory Management",
        "slug": "memory",
        "description": "Memory model and garbage collection",
        "position_x": 110,
        "position_y": 720,
        "keywords": ["gc", "reference counting", "weak references", "__slots__", "memory profiling"],
        "parent_slug": "threading",
        "order_index": 0,
        "topic": "concurrency",
    },
    {
        "name": "Metaclasses",
        "slug": "metaclasses",
        "description": "Class creation and customization",
        "position_x": 440,
        "position_y": 720,
        "keywords": ["type", "__new__", "__init_subclass__", "__class_getitem__", "class factories"],
        "parent_slug": "asyncio",
        "order_index": 0,
        "topic": "oop",
    },
    {
        "name": "NumPy Fundamentals",
        "slug": "numpy-basics",
        "description": "Numerical computing with NumPy arrays",
        "position_x": 1320,
        "position_y": 720,
        "keywords": ["arrays", "broadcasting", "vectorization", "indexing", "ufuncs"],
        "parent_slug": "data-processing",
        "order_index": 0,
        "topic": "data-science",
    },
    {
        "name": "Pandas Essentials",
        "slug": "pandas-basics",
        "description": "Data analysis with Pandas",
        "position_x": 1540,
        "position_y": 720,
        "keywords": ["DataFrame", "Series", "groupby", "merge", "pivot tables"],
        "parent_slug": "data-processing",
        "order_index": 1,
        "topic": "data-science",
    },

    # Level 7 - Expert Topics
    {
        "name": "Design Patterns",
        "slug": "design-patterns",
        "description": "Common software design patterns in Python",
        "position_x": 440,
        "position_y": 840,
        "keywords": ["singleton", "factory", "observer", "strategy", "decorator pattern"],
        "parent_slug": "metaclasses",
        "order_index": 0,
        "topic": "oop",
    },

    # Module Test Nodes (9 hexagonal nodes, one per topic)
    # These are comprehensive tests that unlock the next module when completed
    # Positioned on the outside edges near their corresponding module clusters
    {
        "name": "Fundamentals",
        "slug": "fundamentals-module-test",
        "description": "Comprehensive test combining all fundamentals concepts",
        "position_x": 1800,
        "position_y": 0,
        "keywords": ["variables", "loops", "functions", "errors", "file-io"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "fundamentals",
        "node_type": "module_test",
        "module_order": 1,
    },
    {
        "name": "OOP",
        "slug": "oop-module-test",
        "description": "Comprehensive test combining all OOP concepts",
        "position_x": 2000,
        "position_y": 175,
        "keywords": ["classes", "decorators", "inheritance", "dunder-methods", "context-managers"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "oop",
        "node_type": "module_test",
        "module_order": 2,
    },
    {
        "name": "Data Structures",
        "slug": "data-structures-module-test",
        "description": "Comprehensive test combining all data structures concepts",
        "position_x": 1800,
        "position_y": 175,
        "keywords": ["strings", "regex", "collections", "dates"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "data-structures",
        "node_type": "module_test",
        "module_order": 3,
    },
    {
        "name": "Tooling",
        "slug": "tooling-module-test",
        "description": "Comprehensive test combining all tooling concepts",
        "position_x": 1800,
        "position_y": 350,
        "keywords": ["logging", "testing", "packages", "debugging"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "tooling",
        "node_type": "module_test",
        "module_order": 4,
    },
    {
        "name": "Concurrency",
        "slug": "concurrency-module-test",
        "description": "Comprehensive test combining all concurrency concepts",
        "position_x": 1800,
        "position_y": 700,
        "keywords": ["generators", "threading", "multiprocessing", "asyncio", "GIL"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "concurrency",
        "node_type": "module_test",
        "module_order": 5,
    },
    {
        "name": "Typing",
        "slug": "typing-module-test",
        "description": "Comprehensive test combining all typing concepts",
        "position_x": 2000,
        "position_y": 350,
        "keywords": ["type-hints", "generics", "protocols"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "typing",
        "node_type": "module_test",
        "module_order": 6,
    },
    {
        "name": "Web",
        "slug": "web-module-test",
        "description": "Comprehensive test combining all web concepts",
        "position_x": 1800,
        "position_y": 525,
        "keywords": ["HTTP", "requests", "Flask", "FastAPI", "Django"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "web",
        "node_type": "module_test",
        "module_order": 7,
    },
    {
        "name": "Database",
        "slug": "database-module-test",
        "description": "Comprehensive test combining all database concepts",
        "position_x": 2000,
        "position_y": 525,
        "keywords": ["SQL", "sqlite", "ORM", "SQLAlchemy"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "database",
        "node_type": "module_test",
        "module_order": 8,
    },
    {
        "name": "Data Science",
        "slug": "data-science-module-test",
        "description": "Comprehensive test combining all data science concepts",
        "position_x": 2200,
        "position_y": 525,
        "keywords": ["NumPy", "Pandas", "data-processing", "ETL"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "data-science",
        "node_type": "module_test",
        "module_order": 9,
    },
]


# JavaScript roadmap node definitions (28 nodes) - Wide horizontal layout
# Topics: fundamentals, oop, data-structures, concurrency, tooling
JAVASCRIPT_NODES = [
    # Level 0 - Root (1 node)
    {
        "name": "Types & Primitives",
        "slug": "types-primitives",
        "description": "JavaScript fundamental data types",
        "position_x": 400,
        "position_y": 0,
        "keywords": ["number", "string", "boolean", "null", "undefined", "symbol", "bigint"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "fundamentals",
    },

    # Level 1 - Fundamentals (3 nodes, 220px spacing)
    {
        "name": "Type Coercion & Quirks",
        "slug": "type-coercion",
        "description": "JavaScript type system peculiarities",
        "position_x": 180,
        "position_y": 120,
        "keywords": ["==", "===", "typeof null", "NaN", "truthy/falsy"],
        "parent_slug": "types-primitives",
        "order_index": 0,
        "topic": "fundamentals",
    },
    {
        "name": "Variables & Declarations",
        "slug": "variables",
        "description": "Variable declaration and scoping",
        "position_x": 400,
        "position_y": 120,
        "keywords": ["var", "let", "const", "hoisting", "TDZ"],
        "parent_slug": "types-primitives",
        "order_index": 1,
        "topic": "fundamentals",
    },
    {
        "name": "Symbols",
        "slug": "symbols",
        "description": "Symbol primitive type",
        "position_x": 620,
        "position_y": 120,
        "keywords": ["Symbol()", "well-known symbols", "Symbol.iterator"],
        "parent_slug": "types-primitives",
        "order_index": 2,
        "topic": "fundamentals",
    },

    # Level 2 - Objects & Functions (3 nodes, 220px spacing)
    {
        "name": "Objects Deep Dive",
        "slug": "objects",
        "description": "Working with objects in JavaScript",
        "position_x": 180,
        "position_y": 240,
        "keywords": ["object literals", "property access", "Object methods"],
        "parent_slug": "type-coercion",
        "order_index": 0,
        "topic": "oop",
    },
    {
        "name": "Functions Fundamentals",
        "slug": "functions",
        "description": "Function types and patterns",
        "position_x": 400,
        "position_y": 240,
        "keywords": ["declarations", "expressions", "arrow", "default params"],
        "parent_slug": "variables",
        "order_index": 1,
        "topic": "oop",
    },
    {
        "name": "Prototypes & Inheritance",
        "slug": "prototypes",
        "description": "Prototype-based inheritance",
        "position_x": 620,
        "position_y": 240,
        "keywords": ["[[Prototype]]", "__proto__", "prototype chain"],
        "parent_slug": "objects",
        "order_index": 2,
        "topic": "oop",
    },

    # Level 3 - Function Deep Dive (4 nodes, 220px spacing)
    {
        "name": "this Binding",
        "slug": "this-binding",
        "description": "Understanding 'this' context",
        "position_x": 70,
        "position_y": 360,
        "keywords": ["implicit", "explicit", "call/apply/bind", "arrow this"],
        "parent_slug": "functions",
        "order_index": 0,
        "topic": "oop",
    },
    {
        "name": "Closures & Scope",
        "slug": "closures",
        "description": "Lexical scoping and closures",
        "position_x": 290,
        "position_y": 360,
        "keywords": ["lexical scope", "closure patterns", "IIFE", "module pattern"],
        "parent_slug": "functions",
        "order_index": 1,
        "topic": "oop",
    },
    {
        "name": "Prototype Methods",
        "slug": "prototype-methods",
        "description": "Working with prototypes",
        "position_x": 510,
        "position_y": 360,
        "keywords": ["Object.create", "setPrototypeOf", "hasOwnProperty"],
        "parent_slug": "prototypes",
        "order_index": 2,
        "topic": "oop",
    },
    {
        "name": "Property Descriptors",
        "slug": "property-descriptors",
        "description": "Object property configuration",
        "position_x": 730,
        "position_y": 360,
        "keywords": ["defineProperty", "writable", "enumerable", "configurable"],
        "parent_slug": "prototypes",
        "order_index": 3,
        "topic": "oop",
    },

    # Level 4 - Data Structures (4 nodes, 220px spacing)
    {
        "name": "Arrays In-Depth",
        "slug": "arrays",
        "description": "Array methods and manipulation",
        "position_x": 70,
        "position_y": 480,
        "keywords": ["map", "filter", "reduce", "flat", "flatMap"],
        "parent_slug": "closures",
        "order_index": 0,
        "topic": "data-structures",
    },
    {
        "name": "Iterators & Iterables",
        "slug": "iterators",
        "description": "Iteration protocols",
        "position_x": 290,
        "position_y": 480,
        "keywords": ["Symbol.iterator", "for...of", "custom iterators"],
        "parent_slug": "closures",
        "order_index": 1,
        "topic": "data-structures",
    },
    {
        "name": "Maps & Sets",
        "slug": "maps-sets",
        "description": "Collection data structures",
        "position_x": 510,
        "position_y": 480,
        "keywords": ["Map", "Set", "WeakMap", "WeakSet"],
        "parent_slug": "arrays",
        "order_index": 2,
        "topic": "data-structures",
    },
    {
        "name": "Destructuring & Spread",
        "slug": "destructuring",
        "description": "Modern assignment patterns",
        "position_x": 730,
        "position_y": 480,
        "keywords": ["object/array destructuring", "rest", "spread"],
        "parent_slug": "arrays",
        "order_index": 3,
        "topic": "data-structures",
    },

    # Level 5 - Classes & OOP (3 nodes, 220px spacing)
    {
        "name": "Classes",
        "slug": "classes",
        "description": "ES6 class syntax",
        "position_x": 180,
        "position_y": 600,
        "keywords": ["class syntax", "constructor", "methods", "getters/setters"],
        "parent_slug": "prototype-methods",
        "order_index": 0,
        "topic": "oop",
    },
    {
        "name": "Class Inheritance",
        "slug": "class-inheritance",
        "description": "Class-based inheritance",
        "position_x": 400,
        "position_y": 600,
        "keywords": ["extends", "super", "static", "private fields (#)"],
        "parent_slug": "classes",
        "order_index": 1,
        "topic": "oop",
    },
    {
        "name": "Proxy & Reflect",
        "slug": "proxy-reflect",
        "description": "Metaprogramming APIs",
        "position_x": 620,
        "position_y": 600,
        "keywords": ["Proxy traps", "Reflect methods", "meta-programming"],
        "parent_slug": "property-descriptors",
        "order_index": 2,
        "topic": "oop",
    },

    # Level 6 - Async Foundations (3 nodes, 220px spacing)
    {
        "name": "Event Loop",
        "slug": "event-loop",
        "description": "JavaScript concurrency model",
        "position_x": 180,
        "position_y": 720,
        "keywords": ["call stack", "task queue", "microtask queue"],
        "parent_slug": "class-inheritance",
        "order_index": 0,
        "topic": "concurrency",
    },
    {
        "name": "Callbacks & Timers",
        "slug": "callbacks-timers",
        "description": "Asynchronous callbacks",
        "position_x": 400,
        "position_y": 720,
        "keywords": ["setTimeout", "setInterval", "callback patterns"],
        "parent_slug": "event-loop",
        "order_index": 1,
        "topic": "concurrency",
    },
    {
        "name": "Error Handling",
        "slug": "error-handling",
        "description": "Exception handling patterns",
        "position_x": 620,
        "position_y": 720,
        "keywords": ["try/catch/finally", "Error types", "custom errors"],
        "parent_slug": "proxy-reflect",
        "order_index": 2,
        "topic": "tooling",
    },

    # Level 7 - Modern Async (3 nodes, 220px spacing)
    {
        "name": "Promises",
        "slug": "promises",
        "description": "Promise-based async",
        "position_x": 180,
        "position_y": 840,
        "keywords": ["Promise", "then/catch/finally", "Promise.all/race"],
        "parent_slug": "callbacks-timers",
        "order_index": 0,
        "topic": "concurrency",
    },
    {
        "name": "Async/Await",
        "slug": "async-await",
        "description": "Modern async syntax",
        "position_x": 400,
        "position_y": 840,
        "keywords": ["async functions", "await", "error handling"],
        "parent_slug": "promises",
        "order_index": 1,
        "topic": "concurrency",
    },
    {
        "name": "Generators",
        "slug": "generators",
        "description": "Generator functions",
        "position_x": 620,
        "position_y": 840,
        "keywords": ["function*", "yield", "iterator protocol", "async generators"],
        "parent_slug": "async-await",
        "order_index": 2,
        "topic": "concurrency",
    },

    # Level 8 - Tooling & Advanced (4 nodes, 220px spacing)
    {
        "name": "Modules",
        "slug": "modules",
        "description": "ES Module system",
        "position_x": 70,
        "position_y": 960,
        "keywords": ["ES modules", "import/export", "dynamic import()"],
        "parent_slug": "async-await",
        "order_index": 0,
        "topic": "tooling",
    },
    {
        "name": "Regular Expressions",
        "slug": "regex",
        "description": "Pattern matching with regex",
        "position_x": 290,
        "position_y": 960,
        "keywords": ["regex syntax", "flags", "match", "replace", "named groups"],
        "parent_slug": "generators",
        "order_index": 1,
        "topic": "data-structures",
    },
    {
        "name": "JSON & Serialization",
        "slug": "json",
        "description": "JSON parsing and stringification",
        "position_x": 510,
        "position_y": 960,
        "keywords": ["JSON.parse", "stringify", "replacer/reviver"],
        "parent_slug": "error-handling",
        "order_index": 2,
        "topic": "data-structures",
    },
    {
        "name": "Memory & Performance",
        "slug": "memory",
        "description": "Memory management in JS",
        "position_x": 730,
        "position_y": 960,
        "keywords": ["garbage collection", "memory leaks", "WeakRef"],
        "parent_slug": "error-handling",
        "order_index": 3,
        "topic": "concurrency",
    },
]


# TypeScript roadmap node definitions (20 nodes) - Wide horizontal layout
# Topics: fundamentals, typing, oop, data-structures, tooling
TYPESCRIPT_NODES = [
    # Level 0 - Root (1 node)
    {
        "name": "Type Annotations",
        "slug": "type-annotations",
        "description": "Basic TypeScript type syntax",
        "position_x": 400,
        "position_y": 0,
        "keywords": ["primitives", "arrays", "any", "unknown", "void", "never"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "fundamentals",
    },

    # Level 1 - Type Foundations (3 nodes, 220px spacing)
    {
        "name": "Type Inference",
        "slug": "type-inference",
        "description": "Automatic type detection",
        "position_x": 180,
        "position_y": 120,
        "keywords": ["inference rules", "contextual typing"],
        "parent_slug": "type-annotations",
        "order_index": 0,
        "topic": "fundamentals",
    },
    {
        "name": "Interfaces",
        "slug": "interfaces",
        "description": "Object type contracts",
        "position_x": 400,
        "position_y": 120,
        "keywords": ["interface syntax", "optional", "readonly", "extending"],
        "parent_slug": "type-annotations",
        "order_index": 1,
        "topic": "typing",
    },
    {
        "name": "Type Aliases",
        "slug": "type-aliases",
        "description": "Custom type definitions",
        "position_x": 620,
        "position_y": 120,
        "keywords": ["type keyword", "vs interfaces"],
        "parent_slug": "type-annotations",
        "order_index": 2,
        "topic": "typing",
    },

    # Level 2 - Type Composition (4 nodes, 220px spacing)
    {
        "name": "Union Types",
        "slug": "union-types",
        "description": "Multiple type possibilities",
        "position_x": 70,
        "position_y": 240,
        "keywords": ["union syntax", "discriminated unions"],
        "parent_slug": "interfaces",
        "order_index": 0,
        "topic": "typing",
    },
    {
        "name": "Intersection Types",
        "slug": "intersection-types",
        "description": "Combining multiple types",
        "position_x": 290,
        "position_y": 240,
        "keywords": ["combining types", "interface merging"],
        "parent_slug": "interfaces",
        "order_index": 1,
        "topic": "typing",
    },
    {
        "name": "Literal Types",
        "slug": "literal-types",
        "description": "Exact value types",
        "position_x": 510,
        "position_y": 240,
        "keywords": ["string/number literals", "as const", "template literals"],
        "parent_slug": "type-aliases",
        "order_index": 2,
        "topic": "typing",
    },
    {
        "name": "Enums",
        "slug": "enums",
        "description": "Enumeration types",
        "position_x": 730,
        "position_y": 240,
        "keywords": ["numeric", "string", "const enums"],
        "parent_slug": "type-aliases",
        "order_index": 3,
        "topic": "typing",
    },

    # Level 3 - Type Narrowing & Generics (3 nodes, 220px spacing)
    {
        "name": "Type Narrowing",
        "slug": "type-narrowing",
        "description": "Refining types at runtime",
        "position_x": 180,
        "position_y": 360,
        "keywords": ["typeof", "instanceof", "in", "type predicates"],
        "parent_slug": "union-types",
        "order_index": 0,
        "topic": "typing",
    },
    {
        "name": "Generics Basics",
        "slug": "generics-basics",
        "description": "Type parameters fundamentals",
        "position_x": 400,
        "position_y": 360,
        "keywords": ["generic functions", "interfaces", "classes"],
        "parent_slug": "intersection-types",
        "order_index": 1,
        "topic": "oop",
    },
    {
        "name": "Generic Constraints",
        "slug": "generic-constraints",
        "description": "Limiting generic types",
        "position_x": 620,
        "position_y": 360,
        "keywords": ["extends", "keyof", "indexed access"],
        "parent_slug": "generics-basics",
        "order_index": 2,
        "topic": "oop",
    },

    # Level 4 - Advanced Type Manipulation (3 nodes, 220px spacing)
    {
        "name": "Conditional Types",
        "slug": "conditional-types",
        "description": "Type-level conditionals",
        "position_x": 180,
        "position_y": 480,
        "keywords": ["T extends U ? X : Y", "infer", "distributive"],
        "parent_slug": "generics-basics",
        "order_index": 0,
        "topic": "oop",
    },
    {
        "name": "Mapped Types",
        "slug": "mapped-types",
        "description": "Transforming types",
        "position_x": 400,
        "position_y": 480,
        "keywords": ["[K in keyof T]", "modifiers", "key remapping"],
        "parent_slug": "generic-constraints",
        "order_index": 1,
        "topic": "oop",
    },
    {
        "name": "Custom Utility Types",
        "slug": "custom-utilities",
        "description": "Building your own utilities",
        "position_x": 620,
        "position_y": 480,
        "keywords": ["recursive types", "type challenges"],
        "parent_slug": "mapped-types",
        "order_index": 2,
        "topic": "data-structures",
    },

    # Level 5 - Utility Types (3 nodes, 220px spacing)
    {
        "name": "Built-in Utility Types",
        "slug": "utility-types",
        "description": "Standard type helpers",
        "position_x": 180,
        "position_y": 600,
        "keywords": ["Partial", "Required", "Readonly", "Pick", "Omit", "Record"],
        "parent_slug": "mapped-types",
        "order_index": 0,
        "topic": "data-structures",
    },
    {
        "name": "Advanced Utility Types",
        "slug": "advanced-utility",
        "description": "Complex type utilities",
        "position_x": 400,
        "position_y": 600,
        "keywords": ["Exclude", "Extract", "ReturnType", "Parameters"],
        "parent_slug": "custom-utilities",
        "order_index": 1,
        "topic": "data-structures",
    },
    {
        "name": "Decorators",
        "slug": "decorators",
        "description": "Metadata and modification",
        "position_x": 620,
        "position_y": 600,
        "keywords": ["experimental decorators", "metadata"],
        "parent_slug": "custom-utilities",
        "order_index": 2,
        "topic": "oop",
    },

    # Level 6 - Modules & Configuration (3 nodes, 220px spacing)
    {
        "name": "Declaration Files",
        "slug": "declaration-files",
        "description": "Type definitions for JS",
        "position_x": 180,
        "position_y": 720,
        "keywords": [".d.ts", "declare", "ambient modules"],
        "parent_slug": "utility-types",
        "order_index": 0,
        "topic": "tooling",
    },
    {
        "name": "Module Augmentation",
        "slug": "module-augmentation",
        "description": "Extending existing types",
        "position_x": 400,
        "position_y": 720,
        "keywords": ["declare module", "global augmentation"],
        "parent_slug": "advanced-utility",
        "order_index": 1,
        "topic": "tooling",
    },
    {
        "name": "Compiler Configuration",
        "slug": "compiler-config",
        "description": "tsconfig.json setup",
        "position_x": 620,
        "position_y": 720,
        "keywords": ["tsconfig.json", "strict mode"],
        "parent_slug": "module-augmentation",
        "order_index": 2,
        "topic": "tooling",
    },
]


# React roadmap node definitions (26 nodes) - Wide horizontal layout
# Topics: fundamentals, oop (state/hooks), data-structures (refs/memo), tooling, concurrency, web
REACT_NODES = [
    # Level 0 - Root (1 node)
    {
        "name": "JSX & Elements",
        "slug": "jsx",
        "description": "JSX syntax fundamentals",
        "position_x": 400,
        "position_y": 0,
        "keywords": ["JSX syntax", "createElement", "fragments", "keys"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "fundamentals",
    },

    # Level 1 - Component Basics (2 nodes, 220px spacing)
    {
        "name": "Components",
        "slug": "components",
        "description": "Building React components",
        "position_x": 290,
        "position_y": 120,
        "keywords": ["functional", "props", "children", "composition"],
        "parent_slug": "jsx",
        "order_index": 0,
        "topic": "fundamentals",
    },
    {
        "name": "Conditional & List Rendering",
        "slug": "conditional-rendering",
        "description": "Dynamic content rendering",
        "position_x": 510,
        "position_y": 120,
        "keywords": ["&&", "ternary", "map()", "key prop"],
        "parent_slug": "jsx",
        "order_index": 1,
        "topic": "fundamentals",
    },

    # Level 2 - Core Hooks (4 nodes, 220px spacing)
    {
        "name": "useState",
        "slug": "use-state",
        "description": "Component state management",
        "position_x": 70,
        "position_y": 240,
        "keywords": ["state", "setter functions", "lazy init", "batching"],
        "parent_slug": "components",
        "order_index": 0,
        "topic": "oop",
    },
    {
        "name": "useEffect",
        "slug": "use-effect",
        "description": "Side effects in components",
        "position_x": 290,
        "position_y": 240,
        "keywords": ["effects", "cleanup", "dependencies", "strict mode"],
        "parent_slug": "components",
        "order_index": 1,
        "topic": "oop",
    },
    {
        "name": "useContext",
        "slug": "use-context",
        "description": "Consuming context values",
        "position_x": 510,
        "position_y": 240,
        "keywords": ["createContext", "Provider", "consuming"],
        "parent_slug": "conditional-rendering",
        "order_index": 2,
        "topic": "oop",
    },
    {
        "name": "useReducer",
        "slug": "use-reducer",
        "description": "Complex state logic",
        "position_x": 730,
        "position_y": 240,
        "keywords": ["reducer pattern", "dispatch", "actions"],
        "parent_slug": "conditional-rendering",
        "order_index": 3,
        "topic": "oop",
    },

    # Level 3 - Performance Hooks (4 nodes, 220px spacing)
    {
        "name": "useRef",
        "slug": "use-ref",
        "description": "Mutable refs and DOM access",
        "position_x": 70,
        "position_y": 360,
        "keywords": ["mutable refs", "DOM refs", "preserving values"],
        "parent_slug": "use-state",
        "order_index": 0,
        "topic": "data-structures",
    },
    {
        "name": "useMemo",
        "slug": "use-memo",
        "description": "Memoizing computed values",
        "position_x": 290,
        "position_y": 360,
        "keywords": ["memoizing values", "dependency array"],
        "parent_slug": "use-effect",
        "order_index": 1,
        "topic": "data-structures",
    },
    {
        "name": "useCallback",
        "slug": "use-callback",
        "description": "Memoizing functions",
        "position_x": 510,
        "position_y": 360,
        "keywords": ["memoizing functions", "referential equality"],
        "parent_slug": "use-context",
        "order_index": 2,
        "topic": "data-structures",
    },
    {
        "name": "useLayoutEffect",
        "slug": "use-layout-effect",
        "description": "Synchronous DOM effects",
        "position_x": 730,
        "position_y": 360,
        "keywords": ["vs useEffect", "DOM measurements"],
        "parent_slug": "use-reducer",
        "order_index": 3,
        "topic": "data-structures",
    },

    # Level 4 - Advanced Hooks (4 nodes, 220px spacing)
    {
        "name": "useImperativeHandle",
        "slug": "use-imperative-handle",
        "description": "Customizing ref exposure",
        "position_x": 70,
        "position_y": 480,
        "keywords": ["exposing methods", "forwardRef"],
        "parent_slug": "use-ref",
        "order_index": 0,
        "topic": "oop",
    },
    {
        "name": "useSyncExternalStore",
        "slug": "use-sync-external-store",
        "description": "External store subscriptions",
        "position_x": 290,
        "position_y": 480,
        "keywords": ["external stores", "SSR"],
        "parent_slug": "use-memo",
        "order_index": 1,
        "topic": "oop",
    },
    {
        "name": "useId",
        "slug": "use-id",
        "description": "Unique ID generation",
        "position_x": 510,
        "position_y": 480,
        "keywords": ["unique IDs", "accessibility"],
        "parent_slug": "use-callback",
        "order_index": 2,
        "topic": "tooling",
    },
    {
        "name": "useDebugValue",
        "slug": "use-debug-value",
        "description": "DevTools debugging",
        "position_x": 730,
        "position_y": 480,
        "keywords": ["custom hook debugging"],
        "parent_slug": "use-layout-effect",
        "order_index": 3,
        "topic": "tooling",
    },

    # Level 5 - Patterns (4 nodes, 220px spacing)
    {
        "name": "Custom Hooks",
        "slug": "custom-hooks",
        "description": "Extracting reusable logic",
        "position_x": 70,
        "position_y": 600,
        "keywords": ["extracting logic", "composition"],
        "parent_slug": "use-imperative-handle",
        "order_index": 0,
        "topic": "oop",
    },
    {
        "name": "Composition Patterns",
        "slug": "composition-patterns",
        "description": "Component design patterns",
        "position_x": 290,
        "position_y": 600,
        "keywords": ["render props", "compound components"],
        "parent_slug": "use-sync-external-store",
        "order_index": 1,
        "topic": "oop",
    },
    {
        "name": "Context Patterns",
        "slug": "context-patterns",
        "description": "Advanced context usage",
        "position_x": 510,
        "position_y": 600,
        "keywords": ["multiple contexts", "optimization"],
        "parent_slug": "use-id",
        "order_index": 2,
        "topic": "oop",
    },
    {
        "name": "State Management",
        "slug": "state-management",
        "description": "Application state strategies",
        "position_x": 730,
        "position_y": 600,
        "keywords": ["lifting state", "prop drilling"],
        "parent_slug": "use-debug-value",
        "order_index": 3,
        "topic": "oop",
    },

    # Level 6 - Performance (3 nodes, 220px spacing)
    {
        "name": "React.memo",
        "slug": "react-memo",
        "description": "Component memoization",
        "position_x": 180,
        "position_y": 720,
        "keywords": ["shallow comparison", "custom comparison"],
        "parent_slug": "custom-hooks",
        "order_index": 0,
        "topic": "concurrency",
    },
    {
        "name": "Code Splitting",
        "slug": "code-splitting",
        "description": "Lazy loading components",
        "position_x": 400,
        "position_y": 720,
        "keywords": ["React.lazy", "Suspense", "route-based"],
        "parent_slug": "composition-patterns",
        "order_index": 1,
        "topic": "concurrency",
    },
    {
        "name": "Profiling & Optimization",
        "slug": "profiling",
        "description": "Performance analysis",
        "position_x": 620,
        "position_y": 720,
        "keywords": ["DevTools", "memoization strategies"],
        "parent_slug": "context-patterns",
        "order_index": 2,
        "topic": "concurrency",
    },

    # Level 7 - Advanced Features (4 nodes, 220px spacing)
    {
        "name": "Error Boundaries",
        "slug": "error-boundaries",
        "description": "Error handling in React",
        "position_x": 70,
        "position_y": 840,
        "keywords": ["getDerivedStateFromError", "fallback UI"],
        "parent_slug": "react-memo",
        "order_index": 0,
        "topic": "tooling",
    },
    {
        "name": "Portals",
        "slug": "portals",
        "description": "Rendering outside DOM hierarchy",
        "position_x": 290,
        "position_y": 840,
        "keywords": ["createPortal", "modal patterns"],
        "parent_slug": "code-splitting",
        "order_index": 1,
        "topic": "web",
    },
    {
        "name": "Concurrent Features",
        "slug": "concurrent-features",
        "description": "React 18 concurrent rendering",
        "position_x": 510,
        "position_y": 840,
        "keywords": ["useTransition", "useDeferredValue"],
        "parent_slug": "profiling",
        "order_index": 2,
        "topic": "concurrency",
    },
    {
        "name": "Server Components",
        "slug": "server-components",
        "description": "React Server Components",
        "position_x": 730,
        "position_y": 840,
        "keywords": ["RSC", "server vs client", "data fetching"],
        "parent_slug": "profiling",
        "order_index": 3,
        "topic": "web",
    },
]


# C++ roadmap node definitions (32 nodes) - Wide horizontal layout
# Topics: fundamentals, concurrency (memory), oop, typing (templates), data-structures (STL)
CPP_NODES = [
    # Level 0 - Root (1 node)
    {
        "name": "Types & Syntax",
        "slug": "types-syntax",
        "description": "C++ fundamental types and syntax",
        "position_x": 400,
        "position_y": 0,
        "keywords": ["primitives", "sizeof", "literals", "auto"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "fundamentals",
    },

    # Level 1 - Memory Foundations (2 nodes, 220px spacing)
    {
        "name": "Pointers",
        "slug": "pointers",
        "description": "Pointer fundamentals",
        "position_x": 290,
        "position_y": 120,
        "keywords": ["declaration", "dereference", "address-of", "nullptr"],
        "parent_slug": "types-syntax",
        "order_index": 0,
        "topic": "concurrency",
    },
    {
        "name": "References",
        "slug": "references",
        "description": "Reference types",
        "position_x": 510,
        "position_y": 120,
        "keywords": ["lvalue references", "const references"],
        "parent_slug": "types-syntax",
        "order_index": 1,
        "topic": "concurrency",
    },

    # Level 2 - Memory Management (3 nodes, 220px spacing)
    {
        "name": "Memory Layout",
        "slug": "memory-layout",
        "description": "Program memory organization",
        "position_x": 180,
        "position_y": 240,
        "keywords": ["stack", "heap", "static", "alignment"],
        "parent_slug": "pointers",
        "order_index": 0,
        "topic": "concurrency",
    },
    {
        "name": "Dynamic Memory",
        "slug": "dynamic-memory",
        "description": "Heap allocation",
        "position_x": 400,
        "position_y": 240,
        "keywords": ["new/delete", "placement new"],
        "parent_slug": "pointers",
        "order_index": 1,
        "topic": "concurrency",
    },
    {
        "name": "Arrays",
        "slug": "arrays",
        "description": "C-style arrays",
        "position_x": 620,
        "position_y": 240,
        "keywords": ["C-arrays", "array decay", "pointer arithmetic"],
        "parent_slug": "references",
        "order_index": 2,
        "topic": "data-structures",
    },

    # Level 3 - Functions & Memory Safety (3 nodes, 220px spacing)
    {
        "name": "Memory Pitfalls",
        "slug": "memory-pitfalls",
        "description": "Common memory errors",
        "position_x": 180,
        "position_y": 360,
        "keywords": ["leaks", "dangling pointers", "double free"],
        "parent_slug": "dynamic-memory",
        "order_index": 0,
        "topic": "concurrency",
    },
    {
        "name": "Function Basics",
        "slug": "function-basics",
        "description": "Function fundamentals",
        "position_x": 400,
        "position_y": 360,
        "keywords": ["pass by value/ref/pointer", "overloading"],
        "parent_slug": "memory-layout",
        "order_index": 1,
        "topic": "oop",
    },
    {
        "name": "Function Pointers",
        "slug": "function-pointers",
        "description": "Pointers to functions",
        "position_x": 620,
        "position_y": 360,
        "keywords": ["syntax", "callbacks", "typedef"],
        "parent_slug": "dynamic-memory",
        "order_index": 2,
        "topic": "oop",
    },

    # Level 4 - OOP Foundations (3 nodes, 220px spacing)
    {
        "name": "Lambdas (C++11)",
        "slug": "lambdas",
        "description": "Lambda expressions",
        "position_x": 180,
        "position_y": 480,
        "keywords": ["lambda syntax", "captures", "mutable", "generic"],
        "parent_slug": "function-basics",
        "order_index": 0,
        "topic": "oop",
    },
    {
        "name": "Classes",
        "slug": "classes",
        "description": "Class fundamentals",
        "position_x": 400,
        "position_y": 480,
        "keywords": ["class vs struct", "access specifiers", "this"],
        "parent_slug": "function-basics",
        "order_index": 1,
        "topic": "oop",
    },
    {
        "name": "Constructors",
        "slug": "constructors",
        "description": "Object initialization",
        "position_x": 620,
        "position_y": 480,
        "keywords": ["default", "parameterized", "initializer lists"],
        "parent_slug": "classes",
        "order_index": 2,
        "topic": "oop",
    },

    # Level 5 - Resource Management (4 nodes, 220px spacing)
    {
        "name": "Destructors & RAII",
        "slug": "destructors-raii",
        "description": "Resource management",
        "position_x": 70,
        "position_y": 600,
        "keywords": ["destructor", "RAII", "resource management"],
        "parent_slug": "constructors",
        "order_index": 0,
        "topic": "oop",
    },
    {
        "name": "Copy Semantics",
        "slug": "copy-semantics",
        "description": "Copy operations",
        "position_x": 290,
        "position_y": 600,
        "keywords": ["copy constructor", "assignment", "rule of three"],
        "parent_slug": "constructors",
        "order_index": 1,
        "topic": "oop",
    },
    {
        "name": "Move Semantics (C++11)",
        "slug": "move-semantics",
        "description": "Move operations",
        "position_x": 510,
        "position_y": 600,
        "keywords": ["rvalue refs", "std::move", "rule of five"],
        "parent_slug": "copy-semantics",
        "order_index": 2,
        "topic": "oop",
    },
    {
        "name": "Operator Overloading",
        "slug": "operator-overloading",
        "description": "Custom operators",
        "position_x": 730,
        "position_y": 600,
        "keywords": ["arithmetic", "comparison", "stream"],
        "parent_slug": "constructors",
        "order_index": 3,
        "topic": "oop",
    },

    # Level 6 - Smart Pointers & Inheritance (4 nodes, 220px spacing)
    {
        "name": "unique_ptr",
        "slug": "unique-ptr",
        "description": "Exclusive ownership",
        "position_x": 70,
        "position_y": 720,
        "keywords": ["exclusive ownership", "make_unique"],
        "parent_slug": "move-semantics",
        "order_index": 0,
        "topic": "database",
    },
    {
        "name": "shared_ptr & weak_ptr",
        "slug": "shared-weak-ptr",
        "description": "Shared ownership",
        "position_x": 290,
        "position_y": 720,
        "keywords": ["reference counting", "make_shared"],
        "parent_slug": "move-semantics",
        "order_index": 1,
        "topic": "database",
    },
    {
        "name": "Inheritance",
        "slug": "inheritance",
        "description": "Class inheritance",
        "position_x": 510,
        "position_y": 720,
        "keywords": ["public/protected/private", "is-a"],
        "parent_slug": "destructors-raii",
        "order_index": 2,
        "topic": "oop",
    },
    {
        "name": "Virtual Functions",
        "slug": "virtual-functions",
        "description": "Runtime polymorphism",
        "position_x": 730,
        "position_y": 720,
        "keywords": ["vtable", "virtual", "override", "final"],
        "parent_slug": "inheritance",
        "order_index": 3,
        "topic": "oop",
    },

    # Level 7 - Polymorphism & Templates (3 nodes, 220px spacing)
    {
        "name": "Abstract Classes",
        "slug": "abstract-classes",
        "description": "Interfaces in C++",
        "position_x": 180,
        "position_y": 840,
        "keywords": ["pure virtual", "interfaces"],
        "parent_slug": "virtual-functions",
        "order_index": 0,
        "topic": "oop",
    },
    {
        "name": "Function Templates",
        "slug": "function-templates",
        "description": "Generic functions",
        "position_x": 400,
        "position_y": 840,
        "keywords": ["template syntax", "deduction", "specialization"],
        "parent_slug": "virtual-functions",
        "order_index": 1,
        "topic": "typing",
    },
    {
        "name": "Class Templates",
        "slug": "class-templates",
        "description": "Generic classes",
        "position_x": 620,
        "position_y": 840,
        "keywords": ["template classes", "partial specialization"],
        "parent_slug": "function-templates",
        "order_index": 2,
        "topic": "typing",
    },

    # Level 8 - Advanced Templates & STL (3 nodes, 220px spacing)
    {
        "name": "Variadic Templates (C++11)",
        "slug": "variadic-templates",
        "description": "Variable argument templates",
        "position_x": 180,
        "position_y": 960,
        "keywords": ["parameter packs", "fold expressions"],
        "parent_slug": "function-templates",
        "order_index": 0,
        "topic": "typing",
    },
    {
        "name": "Containers",
        "slug": "containers",
        "description": "STL containers",
        "position_x": 400,
        "position_y": 960,
        "keywords": ["vector", "map", "set", "unordered"],
        "parent_slug": "class-templates",
        "order_index": 1,
        "topic": "data-structures",
    },
    {
        "name": "Iterators",
        "slug": "iterators",
        "description": "Iterator categories",
        "position_x": 620,
        "position_y": 960,
        "keywords": ["categories", "begin/end", "range-based for"],
        "parent_slug": "containers",
        "order_index": 2,
        "topic": "data-structures",
    },

    # Level 9 - STL Algorithms & Modern C++ (3 nodes, 220px spacing)
    {
        "name": "Algorithms",
        "slug": "algorithms",
        "description": "STL algorithms",
        "position_x": 180,
        "position_y": 1080,
        "keywords": ["sort", "find", "transform", "accumulate"],
        "parent_slug": "containers",
        "order_index": 0,
        "topic": "data-structures",
    },
    {
        "name": "Structured Bindings (C++17)",
        "slug": "structured-bindings",
        "description": "Decomposition declarations",
        "position_x": 400,
        "position_y": 1080,
        "keywords": ["auto [a, b]", "tuple unpacking"],
        "parent_slug": "algorithms",
        "order_index": 1,
        "topic": "fundamentals",
    },
    {
        "name": "std::optional & variant (C++17)",
        "slug": "optional-variant",
        "description": "Sum types",
        "position_x": 620,
        "position_y": 1080,
        "keywords": ["optional", "variant", "std::visit"],
        "parent_slug": "algorithms",
        "order_index": 2,
        "topic": "typing",
    },

    # Level 10 - C++20 Features (3 nodes, 220px spacing)
    {
        "name": "Concepts (C++20)",
        "slug": "concepts",
        "description": "Template constraints",
        "position_x": 180,
        "position_y": 1200,
        "keywords": ["requires", "concept definition"],
        "parent_slug": "variadic-templates",
        "order_index": 0,
        "topic": "typing",
    },
    {
        "name": "Ranges (C++20)",
        "slug": "ranges",
        "description": "Range library",
        "position_x": 400,
        "position_y": 1200,
        "keywords": ["range adaptors", "views"],
        "parent_slug": "optional-variant",
        "order_index": 1,
        "topic": "data-structures",
    },
    {
        "name": "Coroutines (C++20)",
        "slug": "coroutines",
        "description": "Coroutine support",
        "position_x": 620,
        "position_y": 1200,
        "keywords": ["co_await", "co_yield", "co_return"],
        "parent_slug": "concepts",
        "order_index": 2,
        "topic": "concurrency",
    },
]


def ensure_language(db: Session, name: str, slug: str, icon: str) -> Language:
    """Ensure a language exists in the database."""
    lang = db.query(Language).filter(Language.slug == slug).first()
    if not lang:
        print(f"{name} language not found. Creating it...")
        lang = Language(
            id=uuid.uuid4(),
            name=name,
            slug=slug,
            icon=icon
        )
        db.add(lang)
        db.commit()
        db.refresh(lang)
    return lang


def seed_roadmap(db: Session, language: Language, nodes_data: list, force: bool = False):
    """Seed the database with roadmap nodes for a language."""
    # Check if roadmap already exists
    existing = db.query(RoadmapNode).filter(RoadmapNode.language_id == language.id).first()
    if existing:
        if force:
            print(f"Deleting existing {language.name} roadmap...")
            db.query(RoadmapNode).filter(RoadmapNode.language_id == language.id).delete()
            db.commit()
        else:
            print(f"{language.name} roadmap already exists. Skipping seed. Use --force to override.")
            return

    # Create a mapping of slug to node for parent lookups
    slug_to_node = {}

    # First pass: create all nodes without parent relationships
    for node_data in nodes_data:
        node = RoadmapNode(
            id=uuid.uuid4(),
            language_id=language.id,
            name=node_data["name"],
            slug=node_data["slug"],
            description=node_data["description"],
            position_x=node_data["position_x"],
            position_y=node_data["position_y"],
            order_index=node_data["order_index"],
            concept_keywords=node_data["keywords"],
            topic=node_data.get("topic"),  # Optional topic for visual grouping
            node_type=node_data.get("node_type", "concept"),  # Default to concept
            module_order=node_data.get("module_order"),  # Optional module order
            theory=node_data.get("theory"),  # Optional theory content
            parent_id=None,  # Will set in second pass
        )
        db.add(node)
        slug_to_node[node_data["slug"]] = node

    db.commit()

    # Refresh to get IDs
    for slug, node in slug_to_node.items():
        db.refresh(node)

    # Second pass: set parent relationships
    for node_data in nodes_data:
        if node_data["parent_slug"]:
            child_node = slug_to_node[node_data["slug"]]
            parent_node = slug_to_node[node_data["parent_slug"]]
            child_node.parent_id = parent_node.id

    db.commit()

    print(f"Successfully seeded {len(nodes_data)} {language.name} roadmap nodes!")


def seed_all_roadmaps(force: bool = False):
    """Seed the database with all roadmaps."""
    db: Session = SessionLocal()

    try:
        # Ensure all languages exist
        python_lang = ensure_language(db, "Python", "python", "python")
        js_lang = ensure_language(db, "JavaScript", "javascript", "javascript")
        ts_lang = ensure_language(db, "TypeScript", "typescript", "typescript")
        react_lang = ensure_language(db, "React", "react", "react")
        cpp_lang = ensure_language(db, "C++", "cpp", "cpp")

        # Seed all roadmaps
        seed_roadmap(db, python_lang, PYTHON_NODES, force)
        seed_roadmap(db, js_lang, JAVASCRIPT_NODES, force)
        seed_roadmap(db, ts_lang, TYPESCRIPT_NODES, force)
        seed_roadmap(db, react_lang, REACT_NODES, force)
        seed_roadmap(db, cpp_lang, CPP_NODES, force)

        print("\nAll roadmaps seeded successfully!")

    except Exception as e:
        db.rollback()
        print(f"Error seeding roadmap: {e}")
        raise
    finally:
        db.close()


def seed_python_roadmap(force: bool = False):
    """Seed only the Python roadmap (for backwards compatibility)."""
    db: Session = SessionLocal()

    try:
        python_lang = ensure_language(db, "Python", "python", "python")
        seed_roadmap(db, python_lang, PYTHON_NODES, force)
    except Exception as e:
        db.rollback()
        print(f"Error seeding roadmap: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    import sys

    force = "--force" in sys.argv

    if "--python-only" in sys.argv:
        seed_python_roadmap(force)
    else:
        seed_all_roadmaps(force)

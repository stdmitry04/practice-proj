"""
Comprehensive leveled theory content for Collections Module.
Output format: Python dictionary with json.dumps() for seed file.
"""

import json

# Collections Module - Complete Theory Structure
collections_theory = json.dumps({
    "beginner": """# Collections Module - Beginner

## Introduction

The `collections` module provides specialized container data types that extend Python's built-in types. These are optimized for specific use cases and can dramatically simplify your code.

### Why Collections Exists

While Python's built-in types (list, dict, set, tuple) handle most tasks, the collections module provides specialized tools that:
- Solve specific problems more elegantly
- Offer better performance for certain operations
- Reduce code complexity by eliminating common patterns

---

## 1. The Problem We're Solving

### Using Built-in Dict (The Hard Way)

```python
# Counting words without collections
word_count = {}
for word in ["apple", "apple", "banana", "apple", "cherry", "banana"]:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)  # {'apple': 3, 'banana': 2, 'cherry': 1}
```

### Using defaultdict (The Collections Way)

```python
from collections import defaultdict

word_count = defaultdict(int)
for word in ["apple", "apple", "banana", "apple", "cherry", "banana"]:
    word_count[word] += 1

print(dict(word_count))  # {'apple': 3, 'banana': 2, 'cherry': 1}
```

The second approach is cleaner and more Pythonic.

---

## 2. defaultdict - Never Worry About KeyError

`defaultdict` is a dict subclass that calls a factory function when accessing missing keys.

### Basic Usage

```python
from collections import defaultdict

# Create a defaultdict with int factory (missing keys return 0)
counts = defaultdict(int)
counts['apple'] += 1
counts['banana'] += 1
counts['apple'] += 1
print(counts)  # defaultdict(<class 'int'>, {'apple': 2, 'banana': 1})

# Convert to regular dict
print(dict(counts))  # {'apple': 2, 'banana': 1}
```

### Different Factory Functions

```python
from collections import defaultdict

# int factory - missing keys return 0
int_dict = defaultdict(int)
int_dict['x'] += 5  # Works! No KeyError

# list factory - missing keys return []
list_dict = defaultdict(list)
list_dict['fruits'].append('apple')
list_dict['fruits'].append('banana')
print(list_dict)  # defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})

# set factory - missing keys return set()
set_dict = defaultdict(set)
set_dict['numbers'].add(1)
set_dict['numbers'].add(2)
print(set_dict)  # defaultdict(<class 'set'>, {'numbers': {1, 2}})
```

### When to Use defaultdict

Use defaultdict when:
- You want to avoid KeyError for missing keys
- You need to aggregate data (counting, grouping)
- You're building data structures incrementally

---

## 3. Counter - Counting Made Easy

`Counter` is a dict subclass for counting hashable objects.

### Basic Usage

```python
from collections import Counter

# Count elements in a list
colors = ['red', 'blue', 'red', 'green', 'blue', 'red']
color_counts = Counter(colors)
print(color_counts)  # Counter({'red': 3, 'blue': 2, 'green': 1})

# Count characters in a string
text = "hello"
char_counts = Counter(text)
print(char_counts)  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
```

### Most Common Elements

```python
from collections import Counter

text = "the quick brown fox jumps over the lazy dog"
words = text.split()
word_counts = Counter(words)

# Get the 3 most common words
print(word_counts.most_common(3))
# [('the', 2), ('quick', 1), ('brown', 1)]

# Get all elements in count order
print(word_counts.most_common())
```

### When to Use Counter

Use Counter when:
- You need to count occurrences of items
- You need the most common elements
- You want clean, readable code for frequency analysis

---

## 4. deque - Double-Ended Queue

`deque` (double-ended queue) is optimized for fast operations on both ends.

### Basic Usage

```python
from collections import deque

# Create a deque
d = deque([1, 2, 3])
print(d)  # deque([1, 2, 3])

# Add to right (end)
d.append(4)
print(d)  # deque([1, 2, 3, 4])

# Add to left (beginning)
d.appendleft(0)
print(d)  # deque([0, 1, 2, 3, 4])

# Remove from right
d.pop()  # 4
print(d)  # deque([0, 1, 2, 3])

# Remove from left
d.popleft()  # 0
print(d)  # deque([1, 2, 3])
```

### Why Use deque Instead of List?

```python
import timeit
from collections import deque

# List - O(n) for insert at beginning
def list_prepend():
    lst = []
    for i in range(1000):
        lst.insert(0, i)

# deque - O(1) for appendleft
def deque_prepend():
    d = deque()
    for i in range(1000):
        d.appendleft(i)

# deque is much faster for this operation
print(timeit.timeit(list_prepend, number=1000))    # ~0.5s
print(timeit.timeit(deque_prepend, number=1000))   # ~0.01s
```

### When to Use deque

Use deque when:
- You need fast operations on both ends
- You're implementing a queue or stack
- You want O(1) performance for append/pop on both sides

---

## 5. namedtuple - Lightweight Immutable Objects

`namedtuple` creates a lightweight, immutable class with named fields.

### Basic Usage

```python
from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create instances
p1 = Point(10, 20)
print(p1)  # Point(x=10, y=20)

# Access by name (better than p1[0])
print(p1.x)  # 10
print(p1.y)  # 20

# Access by index (still works)
print(p1[0])  # 10
print(p1[1])  # 20
```

### Multiple Ways to Create namedtuple

```python
from collections import namedtuple

# String with space-separated names
Person1 = namedtuple('Person', 'name age city')

# List of names
Person2 = namedtuple('Person', ['name', 'age', 'city'])

# All equivalent
p1 = Person1('Alice', 30, 'NYC')
p2 = Person2('Bob', 25, 'LA')
print(p1)  # Person(name='Alice', age=30, city='NYC')
print(p2)  # Person(name='Bob', age=25, city='LA')
```

### Immutability

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

# Immutable - cannot change
p.x = 30  # AttributeError: can't set attribute

# But you can create a new instance
p2 = Point(30, p.y)
print(p2)  # Point(x=30, y=20)
```

### When to Use namedtuple

Use namedtuple when:
- You need a lightweight, immutable object
- You want to avoid creating a full class
- You need better readability than tuples with indices
- Performance is critical (very memory efficient)

---

## Summary

Collections module provides specialized tools:

| Container | Best For | Key Feature |
|-----------|----------|------------|
| **defaultdict** | Avoiding KeyError | Automatic default values |
| **Counter** | Counting items | Frequency analysis |
| **deque** | Fast operations on both ends | O(1) append/pop on both sides |
| **namedtuple** | Lightweight immutable objects | Named fields like a class |

Each solves a specific problem that built-in types don't handle as elegantly.
""",

    "intermediate": """# Collections Module - Intermediate

## 1. defaultdict - Advanced Patterns

### 1.1 Different Factory Functions

```python
from collections import defaultdict

# int: for counting
freq = defaultdict(int)
for letter in "hello":
    freq[letter] += 1
print(freq)  # defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 2, 'o': 1})

# list: for grouping/collecting
groups = defaultdict(list)
people = [('Alice', 'NYC'), ('Bob', 'LA'), ('Charlie', 'NYC')]
for name, city in people:
    groups[city].append(name)
print(groups)  # defaultdict(<class 'list'>, {'NYC': ['Alice', 'Charlie'], 'LA': ['Bob']})

# set: for unique values
tags = defaultdict(set)
items = [('book', 'read'), ('book', 'learn'), ('movie', 'watch')]
for item, tag in items:
    tags[item].add(tag)
print(tags)  # defaultdict(<class 'set'>, {'book': {'read', 'learn'}, 'movie': {'watch'}})

# dict: for nested dictionaries
nested = defaultdict(dict)
nested['user1']['email'] = 'user1@example.com'
nested['user2']['email'] = 'user2@example.com'
print(nested)  # defaultdict(<class 'dict'>, {'user1': {'email': 'user1@example.com'}, ...})
```

### 1.2 Custom Factory Functions

```python
from collections import defaultdict

# Lambda for complex defaults
pairs = defaultdict(lambda: [0, 0])
pairs['apple'][0] += 1  # count
pairs['apple'][1] = 2.5  # price
print(pairs)  # defaultdict(<lambda>, {'apple': [1, 2.5]})

# Nested defaultdicts
tree = lambda: defaultdict(tree)
d = tree()
d['a']['b']['c'] = 'value'
print(d)  # works with arbitrary nesting!
```

### 1.3 Pattern: Building Inverted Index

```python
from collections import defaultdict

# Inverted index - find documents containing words
documents = {
    'doc1': 'python collections module',
    'doc2': 'python data structures',
    'doc3': 'learning collections'
}

word_to_docs = defaultdict(list)
for doc_id, content in documents.items():
    for word in content.split():
        word_to_docs[word].append(doc_id)

print(word_to_docs['python'])       # ['doc1', 'doc2']
print(word_to_docs['collections'])  # ['doc1', 'doc3']
```

---

## 2. Counter - Deep Dive

### 2.1 Creating Counters

```python
from collections import Counter

# From iterable
c1 = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(c1)  # Counter({'a': 3, 'b': 2, 'c': 1})

# From string
c2 = Counter('abracadabra')
print(c2)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# From dict
c3 = Counter({'a': 3, 'b': 1})
print(c3)  # Counter({'a': 3, 'b': 1})

# From keyword arguments
c4 = Counter(a=3, b=1)
print(c4)  # Counter({'a': 3, 'b': 1})
```

### 2.2 Most Common Elements

```python
from collections import Counter

words = "the quick brown fox jumps over the lazy dog".split()
counter = Counter(words)

# Get top 3 most common
print(counter.most_common(3))
# [('the', 2), ('quick', 1), ('brown', 1)]

# Get top 1
print(counter.most_common(1))
# [('the', 2)]

# Get all, sorted by frequency
print(counter.most_common())
# [('the', 2), ('quick', 1), ('brown', 1), ...]

# Least common (reverse order)
print(counter.most_common()[::-1])
# [('dog', 1), ('lazy', 1), ...]
```

### 2.3 Arithmetic Operations

```python
from collections import Counter

# Create two counters
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2, c=3)

# Addition (combine counts)
combined = c1 + c2
print(combined)  # Counter({'a': 4, 'c': 3, 'b': 3})

# Subtraction (keep positive counts only)
diff = c1 - c2
print(diff)  # Counter({'a': 2})

# Intersection (minimum counts)
inter = c1 & c2
print(inter)  # Counter({'a': 1, 'b': 1})

# Union (maximum counts)
union = c1 | c2
print(union)  # Counter({'a': 3, 'c': 3, 'b': 2})
```

### 2.4 Common Counter Methods

```python
from collections import Counter

c = Counter(a=4, b=2, c=3, d=1)

# Most common
print(c.most_common(2))  # [('a', 4), ('c', 3)]

# Elements - returns iterator of elements repeated by count
print(list(c.elements()))  # ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd']

# Subtract another counter
c.subtract(Counter(a=1, b=1))
print(c)  # Counter({'a': 3, 'c': 3, 'b': 1, 'd': 1})

# Update with another counter
c.update(Counter(a=1, e=2))
print(c)  # Counter({'a': 4, 'c': 3, 'e': 2, 'b': 1, 'd': 1})

# Delete elements with zero or negative counts
print(+c)  # Counter({'a': 4, 'c': 3, 'e': 2, 'b': 1, 'd': 1})
```

### 2.5 Pattern: Find Common Elements

```python
from collections import Counter

# Find common elements between lists
list1 = ['apple', 'banana', 'apple', 'cherry']
list2 = ['apple', 'apple', 'banana', 'date']

c1 = Counter(list1)
c2 = Counter(list2)

# Elements in both
common = c1 & c2
print(common)  # Counter({'apple': 2, 'banana': 1})

# Elements only in first
only_first = c1 - c2
print(only_first)  # Counter({'cherry': 1})
```

---

## 3. deque - Advanced Operations

### 3.1 Basic Deque Operations

```python
from collections import deque

d = deque([1, 2, 3, 4, 5])

# Operations on right (end)
d.append(6)          # Add to right: [1, 2, 3, 4, 5, 6]
val = d.pop()        # Remove from right: 6, deque: [1, 2, 3, 4, 5]

# Operations on left (beginning)
d.appendleft(0)      # Add to left: [0, 1, 2, 3, 4, 5]
val = d.popleft()    # Remove from left: 0, deque: [1, 2, 3, 4, 5]
```

### 3.2 Rotation

```python
from collections import deque

d = deque([1, 2, 3, 4, 5])

# Rotate right (positive)
d.rotate(2)
print(d)  # deque([4, 5, 1, 2, 3])

# Rotate left (negative)
d.rotate(-2)
print(d)  # deque([1, 2, 3, 4, 5])

# Practical: circular buffer for sliding window
window = deque([1, 2, 3], maxlen=3)
for i in [4, 5, 6]:
    window.append(i)
    print(list(window))  # [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]
```

### 3.3 Bounded Deque (maxlen)

```python
from collections import deque

# Create deque with max length
d = deque(maxlen=3)

# Adding elements
d.append(1)  # [1]
d.append(2)  # [1, 2]
d.append(3)  # [1, 2, 3]
d.append(4)  # [2, 3, 4] - oldest removed automatically

print(d)  # deque([2, 3, 4], maxlen=3)

# Useful for: sliding windows, LRU tracking, fixed-size buffers
```

### 3.4 Deque vs List Performance

```python
from collections import deque

# For operations at both ends, deque is much faster
operations = 100000

# Prepending to list is O(n)
import timeit
list_time = timeit.timeit(lambda: [].insert(0, 1), number=operations) / operations
print(f"List prepend: {list_time*1000:.4f} ms")

# Prepending to deque is O(1)
def deque_prepend():
    d = deque()
    d.appendleft(1)
deque_time = timeit.timeit(deque_prepend, number=operations) / operations
print(f"Deque prepend: {deque_time*1000:.4f} ms")
# deque is ~100x faster
```

---

## 4. namedtuple - Practical Patterns

### 4.1 Creating and Using namedtuples

```python
from collections import namedtuple

# Define a template
Person = namedtuple('Person', ['name', 'age', 'email'])

# Create instances
alice = Person('Alice', 30, 'alice@example.com')
bob = Person('Bob', 25, 'bob@example.com')

# Access by name
print(alice.name)   # 'Alice'
print(alice.age)    # 30

# Access by index
print(alice[0])     # 'Alice'
print(alice[1])     # 30

# Iterate like tuple
for field in alice:
    print(field)
```

### 4.2 Converting to/from Dicts

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

# Create from dict using unpacking
data = {'x': 10, 'y': 20}
p = Point(**data)
print(p)  # Point(x=10, y=20)

# Convert to dict
point_dict = p._asdict()
print(point_dict)  # OrderedDict([('x', 10), ('y', 20)])

# In Python 3.10+, convert to regular dict
print(dict(p._asdict()))  # {'x': 10, 'y': 20}
```

### 4.3 Creating Modified Copies

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)

# Use _replace to create new instance with changes
p2 = p1._replace(x=30)
print(p1)  # Point(x=10, y=20)
print(p2)  # Point(x=30, y=20)

# Original unchanged (immutability)
```

### 4.4 Default Values

```python
from collections import namedtuple

# Defaults for the last N fields
Person = namedtuple('Person', ['name', 'age', 'email'])
Person.__new__.__defaults__ = (None, None)  # Last 2 fields have defaults

p1 = Person('Alice', 30)  # email defaults to None
p2 = Person('Bob', 25, 'bob@example.com')

print(p1)  # Person(name='Alice', age=30, email=None)
print(p2)  # Person(name='Bob', age=25, email='bob@example.com')
```

### 4.5 Pattern: Database-like Rows

```python
from collections import namedtuple

# Define row structure
User = namedtuple('User', ['id', 'username', 'email', 'created'])

# Create rows
users = [
    User(1, 'alice', 'alice@example.com', '2024-01-01'),
    User(2, 'bob', 'bob@example.com', '2024-01-02'),
    User(3, 'charlie', 'charlie@example.com', '2024-01-03'),
]

# Easy filtering
early_users = [u for u in users if u.id < 3]
print(early_users)

# Readable access
for user in users:
    print(f"{user.username}: {user.email}")
```

---

## 5. Practical Real-World Examples

### 5.1 Word Frequency Analysis

```python
from collections import Counter

text = """
Python is great. Python is powerful.
Collections in Python are useful.
"""

# Clean and count
words = text.lower().split()
words = [w.strip('.,') for w in words]  # Remove punctuation
counter = Counter(words)

# Top 5 most common
print("Top 5 words:")
for word, count in counter.most_common(5):
    print(f"  {word}: {count}")
```

### 5.2 Grouping Data

```python
from collections import defaultdict

# Group students by grade
students = [
    ('Alice', 'A'),
    ('Bob', 'B'),
    ('Charlie', 'A'),
    ('David', 'C'),
    ('Eve', 'B'),
]

by_grade = defaultdict(list)
for name, grade in students:
    by_grade[grade].append(name)

for grade in sorted(by_grade):
    print(f"Grade {grade}: {', '.join(by_grade[grade])}")
```

### 5.3 Sliding Window Algorithm

```python
from collections import deque

def max_in_sliding_window(nums, k):
    \"\"\"Find max element in each sliding window of size k\"\"\"
    if not nums or k <= 0:
        return []

    result = []
    window = deque()

    for i, num in enumerate(nums):
        # Remove elements outside window
        while window and window[0][1] < i - k + 1:
            window.popleft()

        # Remove smaller elements
        while window and window[-1][0] <= num:
            window.pop()

        window.append((num, i))

        # Add result when window is full
        if i >= k - 1:
            result.append(window[0][0])

    return result

print(max_in_sliding_window([1, 3, 1, 2, 0, 5], 3))
# [3, 3, 2, 5]
```

### 5.4 Fixed-Size Cache

```python
from collections import deque

class FixedSizeCache:
    def __init__(self, capacity):
        self.cache = deque(maxlen=capacity)
        self.data = {}

    def add(self, key, value):
        if key in self.data:
            self.cache.remove(key)
        self.cache.append(key)
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def items(self):
        return [(k, self.data[k]) for k in self.cache]

cache = FixedSizeCache(3)
cache.add('a', 1)
cache.add('b', 2)
cache.add('c', 3)
cache.add('d', 4)  # 'a' is removed

print(cache.items())  # [('b', 2), ('c', 3), ('d', 4)]
```

---

## 6. When to Use Each Collections Type

| Use Case | Best Tool | Example |
|----------|-----------|---------|
| Count occurrences | `Counter` | Word frequency, vote counting |
| Group by key | `defaultdict(list)` | Group students by grade |
| Avoid KeyError | `defaultdict` | Building aggregations |
| Fast queue operations | `deque` | Breadth-first search, queues |
| Lightweight objects | `namedtuple` | Database rows, coordinates |
| Sliding window | `deque` | Max/min in window, buffering |
| Inverted index | `defaultdict(list)` | Search indexing |
| Frequency comparison | `Counter` | Finding common elements |
"""
    ,

    "advanced": """# Collections Module - Advanced

## 1. OrderedDict - When Order Matters

### 1.1 History and Purpose

In Python 3.7+, regular dicts maintain insertion order. However, `OrderedDict` still useful for:
- Backward compatibility
- Explicit semantic meaning (order is important)
- Special methods like `move_to_end()`

```python
from collections import OrderedDict

# Regular dict (maintains order in 3.7+)
d = {}
d['z'] = 1
d['a'] = 2
d['m'] = 3

# OrderedDict - explicitly documents that order matters
od = OrderedDict()
od['z'] = 1
od['a'] = 2
od['m'] = 3

print(d)   # {'z': 1, 'a': 2, 'm': 3}
print(od)  # OrderedDict([('z', 1), ('a', 2), ('m', 3)])
```

### 1.2 move_to_end()

```python
from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Move to end (default)
od.move_to_end('a')
print(od)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Move to beginning
od.move_to_end('c', last=False)
print(od)  # OrderedDict([('c', 3), ('b', 2), ('a', 1)])
```

### 1.3 Pattern: LRU Cache with OrderedDict

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Mark as recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove least recently used (first item)
            self.cache.popitem(last=False)

    def items(self):
        return list(self.cache.items())

cache = LRUCache(3)
cache.put('a', 1)
cache.put('b', 2)
cache.put('c', 3)
cache.get('a')  # 'a' now most recently used
cache.put('d', 4)  # 'b' is removed (least recently used)

print(cache.items())  # [('c', 3), ('a', 1), ('d', 4)]
```

### 1.4 Comparison: OrderedDict vs dict

```python
from collections import OrderedDict
import sys

# Memory usage
d = {}
od = OrderedDict()

print(f"Dict size: {sys.getsizeof(d)}")
print(f"OrderedDict size: {sys.getsizeof(od)}")
# OrderedDict uses more memory due to doubly-linked list

# Performance
import timeit

# OrderedDict is slower for most operations
time_dict = timeit.timeit(lambda: {i: i for i in range(1000)})
time_od = timeit.timeit(lambda: OrderedDict((i, i) for i in range(1000)))

print(f"Dict creation: {time_dict:.4f}s")
print(f"OrderedDict creation: {time_od:.4f}s")
# Regular dict is ~2x faster
```

---

## 2. ChainMap - Layered Dictionaries

### 2.1 Basic Usage

```python
from collections import ChainMap

defaults = {'host': 'localhost', 'port': 8000, 'debug': False}
env = {'host': 'example.com', 'debug': True}
cli = {'port': 9000}

# Chain them together with priority (left to right)
config = ChainMap(cli, env, defaults)

print(config['host'])    # 'example.com' (from env)
print(config['port'])    # 9000 (from cli)
print(config['debug'])   # True (from env)

# Lookup order: cli -> env -> defaults
```

### 2.2 Pattern: Configuration Layers

```python
from collections import ChainMap
import os

# Different configuration layers
file_config = {'database': 'prod_db', 'timeout': 30}
env_config = {k.lower(): v for k, v in os.environ.items()}
defaults = {'database': 'local_db', 'timeout': 10, 'retries': 3}

# Merge in priority order
config = ChainMap(env_config, file_config, defaults)

# Gets from highest priority layer that has it
print(config['timeout'])      # From file_config
print(config['retries'])      # From defaults
print(config['database'])     # From file_config
```

### 2.3 Pattern: Function Scope Chain

```python
from collections import ChainMap

def example():
    scope = ChainMap(locals(), globals())
    x = 10

    # Can access both local and global variables
    print(scope.get('x'))  # 10 (local)
    print(scope.get('__name__'))  # '__main__' (global)

example()
```

### 2.4 Adding New Maps

```python
from collections import ChainMap

map1 = {'a': 1, 'b': 2}
map2 = {'b': 20, 'c': 30}

chain = ChainMap(map1, map2)
print(chain)  # ChainMap({'a': 1, 'b': 2}, {'b': 20, 'c': 30})

# Create new ChainMap with additional map at start
chain2 = chain.new_child({'a': 100, 'd': 40})
print(chain2)  # ChainMap({'a': 100, 'd': 40}, {'a': 1, 'b': 2}, {'b': 20, 'c': 30})

# Parent access
print(chain2.parents)  # ChainMap({'a': 1, 'b': 2}, {'b': 20, 'c': 30})
```

---

## 3. UserDict, UserList, UserString

### 3.1 When to Subclass These vs Built-ins

```python
# Bad: Subclassing built-in dict
class MyDict(dict):
    def __setitem__(self, key, value):
        print(f"Setting {key} to {value}")
        super().__setitem__(key, value)

d = MyDict()
d['x'] = 1  # Works
d.update({'y': 2})  # PROBLEM: Bypasses __setitem__!
print(d)  # {'x': 1, 'y': 2}
```

### 3.2 UserDict - The Right Way

```python
from collections import UserDict

class MyDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key} to {value}")
        super().__setitem__(key, value)

d = MyDict()
d['x'] = 1  # Setting x to 1
d.update({'y': 2})  # Setting y to 2
print(d)  # {'x': 1, 'y': 2}
```

### 3.3 UserDict Example: Case-Insensitive Dict

```python
from collections import UserDict

class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(str(key).lower(), value)

    def __getitem__(self, key):
        return super().__getitem__(str(key).lower())

    def __contains__(self, key):
        return super().__contains__(str(key).lower())

d = CaseInsensitiveDict()
d['Name'] = 'Alice'
d['EMAIL'] = 'alice@example.com'

print(d['name'])      # 'Alice'
print(d['email'])     # 'alice@example.com'
print('NAME' in d)    # True
```

### 3.4 UserList Example: Type-Checked List

```python
from collections import UserList

class IntList(UserList):
    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise TypeError(f"Expected int, got {type(value)}")
        super().__setitem__(index, value)

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Expected int, got {type(value)}")
        super().append(value)

lst = IntList([1, 2, 3])
lst.append(4)  # OK
lst[0] = 10  # OK
lst.append("five")  # TypeError!
```

### 3.5 UserString Example: Immutable String Wrapper

```python
from collections import UserString

class ImmutableString(UserString):
    def __init__(self, seq):
        super().__init__(seq)
        self._frozen = True

    def __setitem__(self, index, value):
        raise TypeError("ImmutableString does not support item assignment")

s = ImmutableString("hello")
print(s)  # hello
s[0] = 'H'  # TypeError!
```

---

## 4. Performance Benchmarks

### 4.1 Counter vs Manual Counting

```python
from collections import Counter
import timeit

data = list(range(1000)) * 10

# Using Counter
def with_counter():
    return Counter(data)

# Manual counting
def manual_count():
    counts = {}
    for item in data:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

time_counter = timeit.timeit(with_counter, number=10000)
time_manual = timeit.timeit(manual_count, number=10000)

print(f"Counter: {time_counter:.4f}s")
print(f"Manual: {time_manual:.4f}s")
# Counter is ~2x faster
```

### 4.2 deque vs list

```python
from collections import deque
import timeit

# Prepending 1000 items
def list_prepend():
    lst = []
    for i in range(1000):
        lst.insert(0, i)

def deque_prepend():
    d = deque()
    for i in range(1000):
        d.appendleft(i)

time_list = timeit.timeit(list_prepend, number=100)
time_deque = timeit.timeit(deque_prepend, number=100)

print(f"List: {time_list:.4f}s")
print(f"Deque: {time_deque:.4f}s")
# Deque is ~50-100x faster
```

### 4.3 defaultdict vs dict with get()

```python
from collections import defaultdict
import timeit

# Using defaultdict
def with_defaultdict():
    d = defaultdict(int)
    for i in range(1000):
        d[i % 100] += 1

# Using dict with get()
def with_dict():
    d = {}
    for i in range(1000):
        d[i % 100] = d.get(i % 100, 0) + 1

time_dd = timeit.timeit(with_defaultdict, number=10000)
time_dict = timeit.timeit(with_dict, number=10000)

print(f"defaultdict: {time_dd:.4f}s")
print(f"dict.get(): {time_dict:.4f}s")
# Similar performance, but defaultdict more readable
```

---

## 5. Internal Implementation Details

### 5.1 How defaultdict Works

```python
from collections import defaultdict

# defaultdict stores default_factory
d = defaultdict(int)

print(d.default_factory)  # <class 'int'>

# When accessing missing key, calls default_factory
value = d['missing']  # Calls int() -> 0
print(value)  # 0
print(d)  # defaultdict(<class 'int'>, {'missing': 0})

# Can set to None to raise KeyError
d2 = defaultdict()
d2.default_factory = None
d2['x'] = 1

try:
    d2['y']  # KeyError
except KeyError:
    print("KeyError raised")
```

### 5.2 How Counter Works

```python
from collections import Counter

# Counter is a dict with additional methods
c = Counter(['a', 'b', 'a'])

# Access missing keys returns 0, not KeyError
print(c['missing'])  # 0
print(c)  # Counter({'a': 2, 'b': 1})

# Internally uses dict, subclasses defaultdict behavior
```

### 5.3 How namedtuple is Generated

```python
from collections import namedtuple

# namedtuple dynamically creates a class
Point = namedtuple('Point', ['x', 'y'])

# Created class has:
print(Point.__bases__)  # (tuple,)
print(Point._fields)  # ('x', 'y')
print(Point._field_defaults)  # {}

# Generate readable methods
print(Point.__doc__)  # Generated docstring

# __new__ is optimized for memory efficiency
p = Point(10, 20)
print(isinstance(p, tuple))  # True
```

---

## 6. Advanced Patterns and Tricks

### 6.1 Nested defaultdict

```python
from collections import defaultdict

# Tree-like structure with arbitrary depth
def tree():
    return defaultdict(tree)

d = tree()
d['a']['b']['c'] = 'value'
d['a']['b']['d'] = 'value2'
d['x']['y'] = 'another'

print(dict(d))
# Works with arbitrary nesting!
```

### 6.2 Counter with Custom Objects

```python
from collections import Counter

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

people = [
    Person('Alice', 30),
    Person('Bob', 25),
    Person('Alice', 30),
]

counter = Counter(people)
print(counter)  # Counter({Person(Alice, 30): 2, Person(Bob, 25): 1})
```

### 6.3 deque as Double-Ended Priority Queue

```python
from collections import deque

class PriorityDeque:
    def __init__(self):
        self.items = deque()

    def add(self, item, priority):
        # Add in priority order
        added = False
        for i in range(len(self.items)):
            if priority > self.items[i][1]:
                self.items.insert(i, (item, priority))
                added = True
                break
        if not added:
            self.items.append((item, priority))

    def pop_max(self):
        return self.items.popleft()[0]

    def pop_min(self):
        return self.items.pop()[0]

pq = PriorityDeque()
pq.add('A', 3)
pq.add('B', 1)
pq.add('C', 2)

print(pq.pop_max())  # A (priority 3)
print(pq.pop_min())  # B (priority 1)
```

### 6.4 Memory-Efficient Counters for Large Data

```python
from collections import Counter

def count_large_file(filename, chunk_size=1000):
    \"\"\"Efficiently count lines in large file\"\"\"
    counter = Counter()

    with open(filename, 'r') as f:
        chunk = []
        for line in f:
            chunk.append(line.strip())
            if len(chunk) >= chunk_size:
                counter.update(chunk)
                chunk = []
        if chunk:
            counter.update(chunk)

    return counter

# Memory-efficient: processes in chunks
# counter = count_large_file('huge_file.txt')
```

---

## 7. Comparison Table: When to Use What

| Scenario | Tool | Reason |
|----------|------|--------|
| Count items | `Counter` | Built-in most_common, arithmetic |
| Avoid KeyError | `defaultdict` | Automatic defaults |
| Queue operations | `deque` | O(1) on both ends |
| Immutable records | `namedtuple` | Memory efficient, readable |
| Preserve order with special ops | `OrderedDict` | move_to_end(), LRU cache |
| Layer configurations | `ChainMap` | Priority-based lookup |
| Custom dict behavior | `UserDict` | Reliable subclassing |
| Custom list behavior | `UserList` | Type checking, validation |
| Cache with eviction | `OrderedDict` | With popitem(last=False) |
| Sliding windows | `deque` | Rotate, maxlen features |
"""
    ,

    "cheatsheet": """# Collections Module - Cheatsheet

## Quick Import

```python
from collections import defaultdict, Counter, deque, namedtuple, OrderedDict, ChainMap, UserDict, UserList, UserString
```

---

## defaultdict

```python
from collections import defaultdict

# Create with different factories
d_int = defaultdict(int)           # Missing keys -> 0
d_list = defaultdict(list)         # Missing keys -> []
d_set = defaultdict(set)           # Missing keys -> set()
d_lambda = defaultdict(lambda: []) # Custom factory

# Usage
d_int['count'] += 1
d_list['items'].append('value')
d_set['tags'].add('python')

# Access without KeyError
value = d_int['nonexistent']  # Returns 0

# Convert to dict
result = dict(d_int)
```

---

## Counter

```python
from collections import Counter

# Create
c = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
c = Counter('abracadabra')
c = Counter({'a': 3, 'b': 1})

# Most common
c.most_common()        # [('a', 5), ('b', 2), ('r', 2), ...]
c.most_common(2)       # [('a', 5), ('b', 2)]

# Get elements by count
list(c.elements())     # ['a', 'a', 'a', 'b', 'b', 'r', ...]

# Arithmetic
c1 + c2               # Combine counts
c1 - c2               # Remove counts
c1 & c2               # Intersection (min)
c1 | c2               # Union (max)

# Update
c.update(['a', 'b', 'a'])
c.subtract(['a', 'b'])

# Zero/negative cleanup
+c                    # Remove zero/negative counts
```

---

## deque

```python
from collections import deque

# Create
d = deque([1, 2, 3])
d = deque(maxlen=100)  # Bounded (auto-remove oldest)

# Add/Remove
d.append(4)           # Add to right
d.appendleft(0)       # Add to left
d.pop()               # Remove from right
d.popleft()           # Remove from left

# Rotate
d.rotate(1)           # Rotate right by 1
d.rotate(-1)          # Rotate left by 1

# Check size
len(d)
d.maxlen              # Capacity (None if unbounded)

# Convert
list(d)
```

---

## namedtuple

```python
from collections import namedtuple

# Define
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age city')  # Space-separated
Employee = namedtuple('Employee', ['id', 'name', 'salary'], defaults=[None, None])

# Create
p = Point(10, 20)
person = Person('Alice', 30, 'NYC')

# Access
p.x, p.y              # By name
p[0], p[1]            # By index

# Methods
p._asdict()           # OrderedDict([('x', 10), ('y', 20)])
dict(p._asdict())     # {'x': 10, 'y': 20}
p._replace(x=30)      # New instance with changed field
p._fields             # ('x', 'y')
p._make([10, 20])     # Create from iterable
```

---

## OrderedDict

```python
from collections import OrderedDict

# Create
od = OrderedDict()
od = OrderedDict([('z', 1), ('a', 2)])

# Move to end
od.move_to_end('z')           # Move to end
od.move_to_end('a', last=False)  # Move to beginning

# Get and remove first
od.popitem(last=False)        # Remove first
od.popitem(last=True)         # Remove last
```

---

## ChainMap

```python
from collections import ChainMap

# Create
map1 = {'a': 1, 'b': 2}
map2 = {'b': 20, 'c': 30}
chain = ChainMap(map1, map2)

# Access (priority: map1 > map2)
chain['a']  # 1 (from map1)
chain['b']  # 2 (from map1)
chain['c']  # 30 (from map2)

# Create new layer
chain2 = chain.new_child({'x': 100})

# Access parent
chain.parents
chain.maps
```

---

## UserDict, UserList, UserString

```python
from collections import UserDict, UserList, UserString

# Subclass for custom behavior (not built-in types)
class MyDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key}")
        super().__setitem__(key, value)

class MyList(UserList):
    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise TypeError("Must be int")
        super().__setitem__(index, value)

class MyString(UserString):
    def __init__(self, seq):
        super().__init__(seq)
        self._frozen = True
```

---

## Common Patterns

### Pattern: Counting with defaultdict

```python
from collections import defaultdict

counts = defaultdict(int)
for item in items:
    counts[item] += 1
```

### Pattern: Grouping with defaultdict

```python
from collections import defaultdict

groups = defaultdict(list)
for key, value in data:
    groups[key].append(value)
```

### Pattern: Most Common Elements

```python
from collections import Counter

counter = Counter(items)
top_3 = counter.most_common(3)
```

### Pattern: Sliding Window

```python
from collections import deque

window = deque(maxlen=3)
for item in items:
    window.append(item)
    process(list(window))
```

### Pattern: LRU Cache

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

### Pattern: Configuration Layers

```python
from collections import ChainMap

defaults = {'db': 'local', 'port': 5432}
env = {'db': 'prod'}
cli = {'port': 3306}

config = ChainMap(cli, env, defaults)
```

---

## Performance Tips

| Operation | Tool | Performance |
|-----------|------|-------------|
| Count items | `Counter` | O(n) |
| Get counts | `Counter` | O(1) |
| Prepend | `deque` | O(1) |
| Prepend | `list` | O(n) ❌ |
| Access by key | `defaultdict` | O(1) |
| Multiple layers | `ChainMap` | O(n) where n = layers |
| Immutable records | `namedtuple` | Very memory efficient |
| Subclass dict | `UserDict` | Proper override behavior |

---

## Key Points

✓ **defaultdict**: Never worry about KeyError
✓ **Counter**: Count anything efficiently
✓ **deque**: O(1) operations on both ends
✓ **namedtuple**: Lightweight, immutable objects
✓ **OrderedDict**: Preserve order with special operations (LRU cache)
✓ **ChainMap**: Layer multiple dicts with priority
✓ **UserDict/UserList/UserString**: Subclass these, not built-ins

---

## When NOT to Use Collections

- Don't use `namedtuple` when you need mutable objects → Use dataclasses
- Don't use `OrderedDict` in Python 3.7+ for basic ordering → Use dict
- Don't use `ChainMap` for one-time lookups → Just merge dicts
- Don't subclass built-in dict → Use UserDict
"""
})

print(collections_theory)

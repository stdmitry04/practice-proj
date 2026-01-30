"""
Seed script for language roadmaps.
Creates the hierarchical structure of concepts for the learning roadmap.

Run with: python seed_roadmap.py
"""

import uuid
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.language import Language
from app.models.roadmap_node import RoadmapNode


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
        "theory": """# Basic Python Syntax

## Variables and Assignment
Variables in Python are dynamically typed and don't require declaration:

```python
name = "Alice"          # String
age = 30               # Integer
height = 5.8           # Float
is_student = True      # Boolean
```

## Operators
- **Arithmetic**: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulo), `**` (power)
- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical**: `and`, `or`, `not`

## Control Flow

### If/Else Statements
```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

### Loops
**For loops** iterate over sequences:
```python
for i in range(5):
    print(i)

for item in [1, 2, 3]:
    print(item)
```

**While loops** continue until condition is False:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## List Comprehensions
Concise way to create lists:
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

## Key Takeaways
- Python uses indentation for code blocks
- Variables are dynamically typed
- Comprehensions provide elegant syntax for transformations
""",
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
        "theory": """# File I/O Operations

## Opening Files
Use the `open()` function with file modes:

```python
# Read mode (default)
f = open('file.txt', 'r')

# Write mode (overwrites)
f = open('file.txt', 'w')

# Append mode
f = open('file.txt', 'a')

# Binary mode
f = open('file.dat', 'rb')
```

## The `with` Statement
Automatically closes files:

```python
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed here
```

## Reading Files
```python
# Read entire file
content = f.read()

# Read line by line
for line in f:
    print(line.strip())

# Read all lines into list
lines = f.readlines()
```

## Writing Files
```python
with open('output.txt', 'w') as f:
    f.write('Hello, World!\\n')
    f.writelines(['Line 1\\n', 'Line 2\\n'])
```

## Modern Path Handling
```python
from pathlib import Path

# Object-oriented file paths
path = Path('data/file.txt')
content = path.read_text()
path.write_text('New content')

# Check existence
if path.exists():
    print('File found')
```

## Best Practices
- Always use `with` statements for automatic cleanup
- Use `pathlib` for cross-platform path handling
- Handle encoding explicitly: `open('file.txt', encoding='utf-8')`
""",
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
        "theory": """# Data Types & Structures

## Built-in Types

### Lists (Mutable, Ordered)
```python
fruits = ['apple', 'banana', 'cherry']
fruits.append('date')
fruits[0] = 'apricot'
```

### Tuples (Immutable, Ordered)
```python
coordinates = (10, 20)
# coordinates[0] = 15  # Error!
```

### Dictionaries (Key-Value Pairs)
```python
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'NYC'
}
print(person['name'])
person['job'] = 'Engineer'
```

### Sets (Unique, Unordered)
```python
numbers = {1, 2, 3, 2, 1}  # {1, 2, 3}
numbers.add(4)
numbers.discard(2)
```

## Common Operations

### List Methods
```python
lst = [1, 2, 3]
lst.append(4)      # Add to end
lst.extend([5, 6]) # Add multiple
lst.insert(0, 0)   # Insert at index
lst.pop()          # Remove and return last
```

### Dictionary Methods
```python
d = {'a': 1, 'b': 2}
d.get('c', 0)      # Get with default
d.keys()           # Get all keys
d.values()         # Get all values
d.items()          # Get (key, value) pairs
```

### Set Operations
```python
a = {1, 2, 3}
b = {3, 4, 5}
a | b              # Union: {1, 2, 3, 4, 5}
a & b              # Intersection: {3}
a - b              # Difference: {1, 2}
```

## When to Use What
- **List**: Ordered collection, need indexing
- **Tuple**: Immutable data, function returns
- **Dict**: Key-value lookups, fast access
- **Set**: Unique items, membership testing
""",
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
        "theory": """# Error Handling

## Try/Except Blocks
Handle exceptions gracefully:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## Multiple Exceptions
```python
try:
    file = open('missing.txt')
    data = int(file.read())
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid number format")
```

## Catch All Exceptions
```python
try:
    risky_operation()
except Exception as e:
    print(f"Error occurred: {e}")
```

## Finally Block
Always executes, for cleanup:

```python
try:
    f = open('file.txt')
    process(f)
except IOError:
    print("Error reading file")
finally:
    f.close()  # Always closes
```

## Raising Exceptions
```python
def withdraw(amount):
    if amount < 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
```

## Custom Exceptions
```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Balance {balance} < {amount}"
        )

raise InsufficientFundsError(100, 150)
```

## Exception Chaining
```python
try:
    dangerous_operation()
except Exception as e:
    raise RuntimeError("Failed") from e
```

## Best Practices
- Catch specific exceptions, not broad `Exception`
- Use `finally` for cleanup code
- Don't silence exceptions without logging
- Create custom exceptions for domain errors
""",
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
        "theory": """# Advanced Functions

## Variable Arguments

### *args (Positional)
```python
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)  # 10
```

### **kwargs (Keyword)
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)
```

## Lambda Functions
Anonymous, single-expression functions:

```python
square = lambda x: x ** 2
add = lambda x, y: x + y

# Common with map/filter
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
```

## Closures
Functions that remember enclosing scope:

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
print(add_5(3))  # 8
```

## functools Module

### partial
Pre-fill function arguments:

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

square(5)  # 25
cube(2)    # 8
```

### reduce
Cumulative operations:

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
# 24
```

## Use Cases
- **Lambda**: Quick transformations in map/filter
- **Closures**: Factory functions, decorators
- **partial**: Configuration, callback simplification
""",
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
        "theory": """# Object-Oriented Programming Basics

## Defining Classes
```python
class Dog:
    # Class attribute (shared)
    species = "Canis familiaris"

    # Constructor
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"

    # Class method
    @classmethod
    def get_species(cls):
        return cls.species

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 2
```

## Creating Instances
```python
buddy = Dog("Buddy", 3)
print(buddy.name)      # "Buddy"
print(buddy.bark())    # "Buddy says woof!"
```

## Instance vs Class Attributes
```python
class Counter:
    count = 0  # Class attribute

    def __init__(self):
        Counter.count += 1
        self.id = Counter.count  # Instance

c1 = Counter()  # c1.id = 1
c2 = Counter()  # c2.id = 2
```

## The `self` Parameter
- `self` refers to the instance
- Always first parameter in instance methods
- Not passed explicitly when calling

## Property Decorators
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(temp.fahrenheit)  # 77.0
temp.fahrenheit = 86
print(temp._celsius)    # 30.0
```

## Key Principles
- **Encapsulation**: Bundle data with methods
- **Abstraction**: Hide implementation details
- Use properties for computed attributes
""",
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
        "theory": """# Regular Expressions

## Basic Patterns
```python
import re

# Literal characters
re.search('hello', 'hello world')  # Match found

# Special characters
.    # Any character
^    # Start of string
$    # End of string
*    # 0 or more
+    # 1 or more
?    # 0 or 1
{n}  # Exactly n times
```

## Common Functions

### search() - Find first match
```python
result = re.search(r'\\d+', 'Order 123 confirmed')
result.group()  # '123'
```

### match() - Match from start
```python
re.match(r'\\d+', '123abc')  # Matches
re.match(r'\\d+', 'abc123')  # None
```

### findall() - Find all matches
```python
numbers = re.findall(r'\\d+', 'Call 123 or 456')
# ['123', '456']
```

### sub() - Replace matches
```python
text = re.sub(r'\\d+', 'XXX', 'Call 123 or 456')
# 'Call XXX or XXX'
```

## Character Classes
```python
\\d   # Digit [0-9]
\\w   # Word character [a-zA-Z0-9_]
\\s   # Whitespace
\\D   # Not digit
\\W   # Not word character
\\S   # Not whitespace

[abc]     # a, b, or c
[a-z]     # Any lowercase letter
[^0-9]    # Not a digit
```

## Groups and Capturing
```python
# Capture groups with ()
pattern = r'(\\d{3})-(\\d{3})-(\\d{4})'
match = re.search(pattern, '555-123-4567')
match.group(1)  # '555'
match.group(2)  # '123'
match.groups()  # ('555', '123', '4567')

# Named groups
pattern = r'(?P<area>\\d{3})-(?P<prefix>\\d{3})'
match = re.search(pattern, '555-123-4567')
match.group('area')  # '555'
```

## Practical Examples
```python
# Email validation
email = r'^[\\w.-]+@[\\w.-]+\\.\\w+$'

# URL extraction
url = r'https?://[\\w.-]+\\.[\\w]{2,}'

# Phone number
phone = r'\\(?\\d{3}\\)?[-.\\s]?\\d{3}[-.\\s]?\\d{4}'
```

## Flags
```python
re.IGNORECASE  # Case-insensitive
re.MULTILINE   # ^ and $ match line boundaries
re.DOTALL      # . matches newlines
re.VERBOSE     # Allow comments in pattern
```
""",
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
        "theory": """# String Manipulation

## String Formatting

### f-strings (Modern)
```python
name = "Alice"
age = 30
print(f"Hello, {name}. You are {age} years old.")

# Expressions
print(f"Next year: {age + 1}")

# Formatting
pi = 3.14159
print(f"Pi: {pi:.2f}")  # "Pi: 3.14"
```

### format() Method
```python
"Hello, {}. You are {} years old.".format(name, age)
"Hello, {0}. You are {1}.".format(name, age)
"Hello, {name}. Age: {age}".format(name="Bob", age=25)
```

## String Methods

### Case Conversion
```python
s = "Hello World"
s.upper()      # "HELLO WORLD"
s.lower()      # "hello world"
s.title()      # "Hello World"
s.capitalize() # "Hello world"
s.swapcase()   # "hELLO wORLD"
```

### Searching
```python
s = "hello world"
s.startswith("hello")  # True
s.endswith("world")    # True
s.find("world")        # 6 (index)
s.index("world")       # 6 (raises error if not found)
s.count("l")           # 3
```

### Splitting and Joining
```python
# Split
text = "apple,banana,cherry"
fruits = text.split(",")
# ["apple", "banana", "cherry"]

# Join
",".join(fruits)
# "apple,banana,cherry"

# Split lines
multiline = "line1\\nline2\\nline3"
multiline.splitlines()
```

### Stripping Whitespace
```python
s = "  hello  "
s.strip()   # "hello"
s.lstrip()  # "hello  "
s.rstrip()  # "  hello"

# Remove specific characters
"...hello...".strip(".")  # "hello"
```

### Replacement
```python
s = "hello world"
s.replace("world", "python")  # "hello python"
s.replace("l", "L", 1)        # "heLlo world" (max 1)
```

## String Testing
```python
"123".isdigit()      # True
"abc".isalpha()      # True
"abc123".isalnum()   # True
"   ".isspace()      # True
"Hello".istitle()    # True
```

## Encoding/Decoding
```python
# String to bytes
text = "Hello"
encoded = text.encode('utf-8')  # b'Hello'

# Bytes to string
decoded = encoded.decode('utf-8')  # "Hello"

# Handle errors
text.encode('ascii', errors='ignore')
```

## Multiline Strings
```python
# Triple quotes
text = '''
Line 1
Line 2
Line 3
'''

# Join with newlines
lines = ["Line 1", "Line 2", "Line 3"]
"\\n".join(lines)
```

## String Interpolation Tips
```python
# Padding
f"{name:>10}"   # Right align in 10 chars
f"{name:<10}"   # Left align
f"{name:^10}"   # Center

# Number formatting
f"{value:,}"       # 1,000,000
f"{percent:.1%}"   # 50.5%
f"{number:08d}"    # 00000042 (zero-pad)
```
""",
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
        "theory": """# Collections Module

## defaultdict
Dictionary with default values:

```python
from collections import defaultdict

# Without defaultdict
word_count = {}
for word in words:
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1

# With defaultdict
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1

# Default list
groups = defaultdict(list)
groups['a'].append(1)  # No KeyError!
```

## Counter
Count occurrences:

```python
from collections import Counter

# Count elements
letters = Counter("mississippi")
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Most common
letters.most_common(2)
# [('i', 4), ('s', 4)]

# Arithmetic operations
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
c1 + c2  # Counter({'a': 4, 'b': 3})
c1 - c2  # Counter({'a': 2})
```

## deque
Double-ended queue:

```python
from collections import deque

# Fast operations at both ends
d = deque([1, 2, 3])
d.append(4)      # Right: [1,2,3,4]
d.appendleft(0)  # Left: [0,1,2,3,4]
d.pop()          # Remove from right
d.popleft()      # Remove from left

# Rotate
d = deque([1, 2, 3, 4, 5])
d.rotate(2)      # [4, 5, 1, 2, 3]
d.rotate(-1)     # [5, 1, 2, 3, 4]

# Max length (circular buffer)
d = deque(maxlen=3)
d.extend([1, 2, 3])  # [1, 2, 3]
d.append(4)          # [2, 3, 4] (1 dropped)
```

## namedtuple
Tuple with named fields:

```python
from collections import namedtuple

# Define
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age city')

# Create
p = Point(10, 20)
person = Person('Alice', 30, 'NYC')

# Access
print(p.x, p.y)        # 10 20
print(person.name)     # Alice

# Unpack like tuple
x, y = p

# Immutable
# p.x = 15  # Error!
```

## ChainMap
Combine multiple dicts:

```python
from collections import ChainMap

defaults = {'color': 'red', 'user': 'guest'}
settings = {'user': 'admin'}

# Settings override defaults
config = ChainMap(settings, defaults)
config['user']   # 'admin'
config['color']  # 'red'
```

## OrderedDict
Dict that remembers insertion order:

```python
from collections import OrderedDict

# Regular dict (3.7+) also maintains order
# but OrderedDict has extra methods

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3

# Move to end
d.move_to_end('a')
# OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Pop from beginning
d.popitem(last=False)  # ('b', 2)
```

## Use Cases
- **defaultdict**: Grouping, counting without key checks
- **Counter**: Frequency analysis, statistics
- **deque**: Queues, sliding windows, undo/redo
- **namedtuple**: Readable tuples, lightweight objects
- **ChainMap**: Configuration layers, scoped lookups
""",
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
        "theory": """# Decorators

## Basic Function Decorator
Modify or enhance functions without changing their code:

```python
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.2f}s")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
```

## Using functools.wraps
Preserve original function metadata:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## Parameterized Decorators
Decorators that accept arguments:

```python
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")
```

## Class Decorators
Modify classes:

```python
def add_str_method(cls):
    cls.__str__ = lambda self: f"{cls.__name__} instance"
    return cls

@add_str_method
class MyClass:
    pass
```

## Real-World Uses
- **Logging**: Track function calls
- **Caching**: Memoize expensive computations
- **Authentication**: Check permissions
- **Validation**: Verify inputs
- **Rate Limiting**: Control request frequency

```python
@login_required
@rate_limit(calls=100, period=3600)
def api_endpoint(request):
    return process_request(request)
```
""",
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
        "theory": """# Inheritance & Composition

## Basic Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
dog.speak()  # "Buddy says Woof!"
```

## super() Function
Call parent methods:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
```

## Multiple Inheritance
```python
class Flyable:
    def fly(self):
        return "Flying!"

class Swimmable:
    def swim(self):
        return "Swimming!"

class Duck(Flyable, Swimmable):
    pass

duck = Duck()
duck.fly()   # "Flying!"
duck.swim()  # "Swimming!"
```

## Method Resolution Order (MRO)
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

# Check MRO
D.__mro__
# (<class 'D'>, <class 'B'>, <class 'C'>,
#  <class 'A'>, <class 'object'>)

d = D()
d.method()  # "B" (searches left to right)
```

## Mixins
Add functionality without is-a relationship:

```python
class JSONMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

class TimestampMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now()

class User(JSONMixin, TimestampMixin):
    def __init__(self, name):
        super().__init__()
        self.name = name

user = User("Alice")
user.to_json()        # JSON string
user.created_at       # Timestamp
```

## Abstract Base Classes
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape()  # Error! Can't instantiate ABC
rect = Rectangle(5, 3)  # OK
```

## Composition (Favor over Inheritance)
```python
class Engine:
    def start(self):
        return "Engine started"

class Wheels:
    def roll(self):
        return "Wheels rolling"

class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = Wheels()

    def drive(self):
        self.engine.start()
        return self.wheels.roll()

car = Car()
car.drive()
```

## When to Use What

### Inheritance
- True is-a relationship
- Share behavior across related classes
- Extend framework classes

### Composition
- Has-a relationship
- Flexible, loosely coupled
- Easier to test
- **Prefer composition over inheritance**

### Mixins
- Add specific capabilities
- Multiple unrelated features
- Reusable across class hierarchies
""",
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
        "theory": """# Context Managers

## The `with` Statement
Automatically handles setup and cleanup:

```python
with open('file.txt') as f:
    content = f.read()
# File automatically closed
```

## Protocol Methods

### __enter__ and __exit__
```python
class DatabaseConnection:
    def __enter__(self):
        self.conn = create_connection()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        # Return True to suppress exceptions
        return False

with DatabaseConnection() as conn:
    conn.execute('SELECT * FROM users')
```

## Using contextlib

### @contextmanager Decorator
```python
from contextlib import contextmanager

@contextmanager
def temporary_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()
        os.remove(filename)

with temporary_file('temp.txt') as f:
    f.write('Hello')
```

### suppress
Ignore specific exceptions:

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('nonexistent.txt')
```

### redirect_stdout
Capture print output:

```python
from contextlib import redirect_stdout
import io

f = io.StringIO()
with redirect_stdout(f):
    print('Hello')
output = f.getvalue()  # 'Hello\\n'
```

## Real-World Examples

### Database Transaction
```python
@contextmanager
def transaction(db):
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise

with transaction(db) as conn:
    conn.execute('INSERT ...')
```

### Timer Context
```python
@contextmanager
def timer(name):
    start = time.time()
    yield
    print(f"{name}: {time.time()-start:.2f}s")

with timer('Processing'):
    expensive_operation()
```

## Key Benefits
- Guaranteed cleanup (even on exceptions)
- Cleaner, more readable code
- Automatic resource management
""",
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
        "theory": """# Testing Fundamentals

## unittest (Built-in)
```python
import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

    def setUp(self):
        # Runs before each test
        self.value = 10

    def tearDown(self):
        # Runs after each test
        pass

if __name__ == '__main__':
    unittest.main()
```

## pytest (Recommended)
Simpler syntax, more powerful:

```python
# test_math.py
def test_addition():
    assert 2 + 2 == 4

def test_division():
    assert 10 / 2 == 5

# Run with: pytest test_math.py
```

## Fixtures
Setup and teardown:

```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15

def test_length(sample_data):
    assert len(sample_data) == 5
```

## Parametrized Tests
Test multiple inputs:

```python
@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert input ** 2 == expected
```

## Mocking
Replace dependencies:

```python
from unittest.mock import Mock, patch

def test_api_call():
    # Mock external API
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'status': 'ok'}

        result = fetch_data()
        assert result['status'] == 'ok'
```

## Testing Exceptions
```python
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_value_error():
    with pytest.raises(ValueError, match="invalid"):
        raise ValueError("invalid input")
```

## Test Coverage
```bash
# Install coverage
pip install pytest-cov

# Run with coverage
pytest --cov=myapp tests/

# Generate HTML report
pytest --cov=myapp --cov-report=html
```

## Best Practices
- Test one thing per test
- Use descriptive test names
- Arrange-Act-Assert pattern
- Keep tests independent
- Mock external dependencies
- Aim for high coverage (>80%)

## AAA Pattern
```python
def test_user_creation():
    # Arrange
    name = "Alice"
    email = "alice@example.com"

    # Act
    user = User(name, email)

    # Assert
    assert user.name == name
    assert user.email == email
```
""",
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
        "theory": """# Generators & Iterators

## Generator Functions
Use `yield` to produce values lazily:

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)  # 5, 4, 3, 2, 1
```

## Memory Efficiency
Generators don't store all values in memory:

```python
# Bad: Creates list of 1M numbers
numbers = [x**2 for x in range(1000000)]

# Good: Generates on demand
numbers = (x**2 for x in range(1000000))
```

## Generator Expressions
Compact syntax like list comprehensions:

```python
# List comprehension
squares_list = [x**2 for x in range(10)]

# Generator expression
squares_gen = (x**2 for x in range(10))
```

## Iterator Protocol
```python
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        raise StopIteration

for i in Counter(5):
    print(i)  # 1, 2, 3, 4, 5
```

## itertools Module
Powerful iteration tools:

```python
from itertools import *

# Infinite iterators
count(10)          # 10, 11, 12, ...
cycle([1, 2, 3])   # 1, 2, 3, 1, 2, 3, ...

# Finite iterators
chain([1, 2], [3, 4])      # 1, 2, 3, 4
islice(range(10), 5)       # 0, 1, 2, 3, 4
combinations([1,2,3], 2)   # (1,2), (1,3), (2,3)
```

## Use Cases
- Processing large files line by line
- Infinite sequences
- Pipeline data transformations
- Memory-constrained environments
""",
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
        "theory": """# Type Hints

## Basic Type Annotations
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

age: int = 30
names: list[str] = ["Alice", "Bob"]
scores: dict[str, int] = {"Alice": 95}
```

## typing Module

### Optional and Union
```python
from typing import Optional, Union

# Optional[T] = Union[T, None]
def find_user(id: int) -> Optional[str]:
    return users.get(id)

# Union for multiple types
def process(data: Union[str, int]) -> str:
    return str(data)
```

### Collections
```python
from typing import List, Dict, Set, Tuple

names: List[str] = ["Alice", "Bob"]
ages: Dict[str, int] = {"Alice": 30}
unique: Set[int] = {1, 2, 3}
point: Tuple[int, int] = (10, 20)
```

### Callable
```python
from typing import Callable

def apply(
    func: Callable[[int, int], int],
    x: int,
    y: int
) -> int:
    return func(x, y)

apply(lambda a, b: a + b, 5, 3)
```

## Generic Types
```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# Type-specific stacks
int_stack: Stack[int] = Stack()
str_stack: Stack[str] = Stack()
```

## Protocol (Structural Typing)
```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

def render(obj: Drawable) -> None:
    obj.draw()

# Any object with draw() works
class Circle:
    def draw(self) -> None:
        print("Drawing circle")

render(Circle())  # OK!
```

## Type Checking with mypy
```bash
# Install mypy
pip install mypy

# Check types
mypy script.py
```

## Modern Syntax (Python 3.10+)
```python
# Union types with |
def process(data: str | int) -> str:
    return str(data)

# Built-in generics
names: list[str] = ["Alice"]
scores: dict[str, int] = {}
```

## Benefits
- Better IDE autocomplete
- Catch bugs before runtime
- Self-documenting code
- Easier refactoring
""",
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
        "theory": """# AsyncIO

## Async/Await Syntax
```python
import asyncio

async def fetch_data(url):
    # Simulate network request
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    result = await fetch_data("example.com")
    print(result)

# Run the async function
asyncio.run(main())
```

## Running Multiple Coroutines

### gather() - Run concurrently
```python
async def main():
    results = await asyncio.gather(
        fetch_data("site1.com"),
        fetch_data("site2.com"),
        fetch_data("site3.com")
    )
    # All complete in ~1 second (parallel)
```

### create_task() - Fire and forget
```python
async def main():
    task1 = asyncio.create_task(fetch_data("a.com"))
    task2 = asyncio.create_task(fetch_data("b.com"))

    # Do other work
    await some_other_work()

    # Wait for tasks
    result1 = await task1
    result2 = await task2
```

## Async Context Managers
```python
class AsyncDB:
    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *args):
        await self.disconnect()

async with AsyncDB() as db:
    await db.query("SELECT * FROM users")
```

## Async Iterators
```python
class AsyncRange:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.i < self.n:
            await asyncio.sleep(0.1)
            self.i += 1
            return self.i
        raise StopAsyncIteration

async for i in AsyncRange(5):
    print(i)
```

## Real-World Example: Web Scraping
```python
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ["site1.com", "site2.com", "site3.com"]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    return results
```

## When to Use AsyncIO
✅ I/O-bound operations (network, files)
✅ Many concurrent operations
✅ Web servers, APIs, web scraping

❌ CPU-bound operations (use multiprocessing)
❌ Simple synchronous scripts

## Key Functions
```python
asyncio.run()         # Run main coroutine
asyncio.sleep()       # Async sleep
asyncio.gather()      # Wait for multiple
asyncio.create_task() # Schedule coroutine
asyncio.wait_for()    # With timeout
```
""",
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
    # Positioned vertically to the right of the main graph, aligned with topic Y levels
    # X=1750 (right of max concept X=1540), 80px vertical spacing between nodes
    {
        "name": "Fundamentals Module Test",
        "slug": "fundamentals-module-test",
        "description": "Comprehensive test combining all fundamentals concepts",
        "position_x": 1750,
        "position_y": 60,
        "keywords": ["variables", "loops", "functions", "errors", "file-io"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "fundamentals",
        "node_type": "module_test",
        "module_order": 1,
    },
    {
        "name": "Data Structures Module Test",
        "slug": "data-structures-module-test",
        "description": "Comprehensive test combining all data structures concepts",
        "position_x": 1750,
        "position_y": 360,
        "keywords": ["strings", "regex", "collections", "dates"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "data-structures",
        "node_type": "module_test",
        "module_order": 3,
    },
    {
        "name": "Tooling Module Test",
        "slug": "tooling-module-test",
        "description": "Comprehensive test combining all tooling concepts",
        "position_x": 1750,
        "position_y": 440,
        "keywords": ["logging", "testing", "packages", "debugging"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "tooling",
        "node_type": "module_test",
        "module_order": 4,
    },
    {
        "name": "Typing Module Test",
        "slug": "typing-module-test",
        "description": "Comprehensive test combining all typing concepts",
        "position_x": 1750,
        "position_y": 520,
        "keywords": ["type-hints", "generics", "protocols"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "typing",
        "node_type": "module_test",
        "module_order": 6,
    },
    {
        "name": "OOP Module Test",
        "slug": "oop-module-test",
        "description": "Comprehensive test combining all OOP concepts",
        "position_x": 1750,
        "position_y": 600,
        "keywords": ["classes", "decorators", "inheritance", "dunder-methods", "context-managers"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "oop",
        "node_type": "module_test",
        "module_order": 2,
    },
    {
        "name": "Web Module Test",
        "slug": "web-module-test",
        "description": "Comprehensive test combining all web concepts",
        "position_x": 1750,
        "position_y": 680,
        "keywords": ["HTTP", "requests", "Flask", "FastAPI", "Django"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "web",
        "node_type": "module_test",
        "module_order": 7,
    },
    {
        "name": "Database Module Test",
        "slug": "database-module-test",
        "description": "Comprehensive test combining all database concepts",
        "position_x": 1750,
        "position_y": 760,
        "keywords": ["SQL", "sqlite", "ORM", "SQLAlchemy"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "database",
        "node_type": "module_test",
        "module_order": 8,
    },
    {
        "name": "Concurrency Module Test",
        "slug": "concurrency-module-test",
        "description": "Comprehensive test combining all concurrency concepts",
        "position_x": 1750,
        "position_y": 840,
        "keywords": ["generators", "threading", "multiprocessing", "asyncio", "GIL"],
        "parent_slug": None,
        "order_index": 0,
        "topic": "concurrency",
        "node_type": "module_test",
        "module_order": 5,
    },
    {
        "name": "Data Science Module Test",
        "slug": "data-science-module-test",
        "description": "Comprehensive test combining all data science concepts",
        "position_x": 1750,
        "position_y": 920,
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

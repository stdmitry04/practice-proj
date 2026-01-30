"""
Comprehensive theory content for data-structures nodes.
This module contains detailed, leveled educational content.
"""

import json

# Regular Expressions - Comprehensive Theory
REGEX_THEORY = json.dumps({
    "beginner": """# Regular Expressions - Beginner

## Introduction

Regular expressions (regex) are powerful tools for pattern matching and text manipulation. They allow you to search for, validate, and extract specific patterns from strings.

---

## 1. What is a Regular Expression?

A regular expression is a sequence of characters that defines a search pattern.

```python
import re

# Simple pattern matching
text = "Call me at 555-123-4567"
phone = re.search(r'\\d{3}-\\d{3}-\\d{4}', text)
if phone:
    print(phone.group())  # 555-123-4567
```

---

## 2. Basic Special Characters

### 2.1 The Dot (.)
Matches any character except newline.

```python
import re
re.findall(r'a.c', 'abc, adc, axc')  # ['abc', 'adc', 'axc']
```

### 2.2 Anchors: ^ and $
- `^` matches the start of a string
- `$` matches the end of a string

```python
import re
re.match(r'^hello', 'hello world')  # Matches
re.search(r'world$', 'hello world')  # Matches
re.match(r'^python$', 'python')      # Exact match
```

### 2.3 Quantifiers: *, +, ?
- `*` means "0 or more"
- `+` means "1 or more"
- `?` means "0 or 1"

```python
import re
re.findall(r'ab*c', 'ac, abc, abbc')   # ['ac', 'abc', 'abbc']
re.findall(r'ab+c', 'ac, abc, abbc')   # ['abc', 'abbc']
re.findall(r'ab?c', 'ac, abc, abbc')   # ['ac', 'abc']
```

### 2.4 Character Classes: []

```python
import re
re.findall(r'[aeiou]', 'hello')   # ['e', 'o']
re.findall(r'[0-9]', 'abc123')    # ['1', '2', '3']
re.findall(r'[^aeiou]', 'hello')  # ['h', 'l', 'l'] (negation)
```

---

## 3. Your First Patterns

### Email Pattern
```python
import re

def is_email(text):
    pattern = r'^[\\w.-]+@[\\w.-]+\\.[a-z]{2,}$'
    return bool(re.match(pattern, text, re.IGNORECASE))

print(is_email('john@example.com'))  # True
```

### Phone Pattern
```python
import re

def extract_phones(text):
    pattern = r'\\d{3}-\\d{3}-\\d{4}'
    return re.findall(pattern, text)

print(extract_phones('Call 555-123-4567'))  # ['555-123-4567']
```

---

## 4. Common Mistakes

### Use Raw Strings
```python
# WRONG - backslashes get interpreted
pattern = '\\d+'

# CORRECT - use raw string
pattern = r'\\d+'
```

### search() vs match()
```python
import re
text = 'hello world'
re.match(r'world', text)   # None - match() checks start only
re.search(r'world', text)  # Matches - search() finds anywhere
```
""",
    "intermediate": """# Regular Expressions - Intermediate

## 1. Core Functions

### re.search() - Find First Match
```python
import re

text = 'Phone: 555-123-4567'
match = re.search(r'\\d{3}-\\d{3}-\\d{4}', text)
if match:
    print(match.group())   # 555-123-4567
    print(match.span())    # (7, 19)
```

### re.findall() - Find All Matches
```python
import re

emails = re.findall(r'[\\w.-]+@[\\w.-]+', 'john@a.com, mary@b.com')
print(emails)  # ['john@a.com', 'mary@b.com']
```

### re.sub() - Replace Matches
```python
import re

text = 'The year is 2024'
result = re.sub(r'\\d{4}', '2025', text)
print(result)  # The year is 2025

# Using function for replacement
def upper(m):
    return m.group().upper()

result = re.sub(r'\\w+', upper, 'hello world')
print(result)  # HELLO WORLD
```

### re.split() - Split by Pattern
```python
import re

parts = re.split(r'\\s+', 'apple   banana\\tcherry')
print(parts)  # ['apple', 'banana', 'cherry']
```

---

## 2. Character Classes

```python
import re

# Built-in classes
\\d  # Digit [0-9]
\\D  # Non-digit
\\w  # Word char [a-zA-Z0-9_]
\\W  # Non-word char
\\s  # Whitespace
\\S  # Non-whitespace

# Examples
re.findall(r'\\d+', 'abc123def456')   # ['123', '456']
re.findall(r'\\w+', 'hello-world')    # ['hello', 'world']
re.findall(r'\\S+', 'hello world')    # ['hello', 'world']
```

---

## 3. Greedy vs Non-Greedy

```python
import re

text = '<div>content</div>'

# Greedy - matches as much as possible
greedy = re.search(r'<.*>', text)
print(greedy.group())  # <div>content</div>

# Non-greedy - matches as little as possible
lazy = re.search(r'<.*?>', text)
print(lazy.group())  # <div>
```

---

## 4. Groups and Capturing

### Capturing Groups
```python
import re

phone = '555-123-4567'
pattern = r'(\\d{3})-(\\d{3})-(\\d{4})'
match = re.search(pattern, phone)

print(match.group(0))   # 555-123-4567 (full match)
print(match.group(1))   # 555 (first group)
print(match.groups())   # ('555', '123', '4567')
```

### Named Groups
```python
import re

email = 'john@example.com'
pattern = r'(?P<user>[\\w.-]+)@(?P<domain>[\\w.-]+)'
match = re.search(pattern, email)

print(match.group('user'))    # john
print(match.groupdict())      # {'user': 'john', 'domain': 'example.com'}
```

### Backreferences
```python
import re

# Match repeated words
text = 'She said said hello'
pattern = r'\\b(\\w+)\\s+\\1\\b'
matches = re.findall(pattern, text)
print(matches)  # ['said']
```

---

## 5. Practical Examples

### Log Parser
```python
import re

log = '2024-01-15 14:32:45 ERROR Database failed'
pattern = r'(\\d{4}-\\d{2}-\\d{2}) (\\d{2}:\\d{2}:\\d{2}) (\\w+) (.*)'
match = re.search(pattern, log)

if match:
    date, time, level, msg = match.groups()
    print(f'{level}: {msg}')  # ERROR: Database failed
```

### Password Validator
```python
import re

def check_password(pwd):
    checks = {
        'length': len(pwd) >= 8,
        'lowercase': bool(re.search(r'[a-z]', pwd)),
        'uppercase': bool(re.search(r'[A-Z]', pwd)),
        'digit': bool(re.search(r'\\d', pwd)),
        'special': bool(re.search(r'[!@#$%^&*]', pwd)),
    }
    return all(checks.values())

print(check_password('Strong@123'))  # True
```
""",
    "advanced": """# Regular Expressions - Advanced

## 1. Performance Optimization

### Compiled Patterns
```python
import re

# Compile patterns used multiple times
EMAIL = re.compile(r'^[\\w.-]+@[\\w.-]+\\.[a-z]+$', re.IGNORECASE)
PHONE = re.compile(r'^\\d{3}-\\d{3}-\\d{4}$')

# Reuse compiled patterns
for email in emails:
    if EMAIL.match(email):
        print(f'Valid: {email}')
```

### Avoid Catastrophic Backtracking
```python
import re

# BAD - nested quantifiers cause exponential backtracking
# pattern = r'(a+)+b'  # Don't use!

# GOOD - simpler pattern
pattern = r'a+b'
```

### Optimization Tips
```python
# Be specific - avoid .* when possible
# BAD
r'<(.*)>'
# GOOD
r'<([^>]+)>'

# Use non-capturing groups when you don't need the match
# SLOWER
r'(\\d{3})-(\\d{3})-(\\d{4})'
# FASTER
r'(?:\\d{3})-(?:\\d{3})-(?:\\d{4})'
```

---

## 2. Lookahead and Lookbehind

### Positive Lookahead (?=...)
Match only if followed by pattern:

```python
import re

text = 'test.com test.org test'
pattern = r'test(?=\\.com)'
matches = re.findall(pattern, text)
print(matches)  # ['test']
```

### Negative Lookahead (?!...)
Match only if NOT followed by pattern:

```python
import re

text = 'test.com test.org test'
pattern = r'test(?!\\.com)'
matches = re.findall(pattern, text)
print(matches)  # ['test', 'test']
```

### Positive Lookbehind (?<=...)
Match only if preceded by pattern:

```python
import re

text = 'Price: $19.99 and 5 items'
pattern = r'(?<=\\$)\\d+\\.\\d+'
matches = re.findall(pattern, text)
print(matches)  # ['19.99']
```

### Negative Lookbehind (?<!...)
Match only if NOT preceded by pattern:

```python
import re

text = 'Item #123 costs $50'
pattern = r'(?<!#)\\d+'
matches = re.findall(pattern, text)
print(matches)  # ['50']
```

---

## 3. Flags and Modifiers

```python
import re

# Case-insensitive
re.findall(r'python', 'Python PYTHON', re.IGNORECASE)
# ['Python', 'PYTHON']

# Multiline - ^ and $ match line boundaries
text = 'First\\nSecond\\nThird'
re.findall(r'^\\w+', text, re.MULTILINE)
# ['First', 'Second', 'Third']

# Dotall - . matches newlines
text = 'Start\\nEnd'
re.search(r'Start.*End', text, re.DOTALL).group()
# 'Start\\nEnd'

# Verbose - allow comments
pattern = re.compile(r'''
    ^               # Start
    [\\w.-]+        # Username
    @               # At sign
    [\\w.-]+        # Domain
    $               # End
''', re.VERBOSE)
```

---

## 4. Advanced Patterns

### IPv4 Validation
```python
import re

ipv4 = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

ips = ['192.168.1.1', '256.1.1.1', '10.0.0.0']
for ip in ips:
    if re.match(ipv4, ip):
        print(f'Valid: {ip}')
```

### Dynamic Pattern Building
```python
import re

def build_pattern(domains):
    escaped = '|'.join(re.escape(d) for d in domains)
    return re.compile(rf'https?://(?:{escaped})')

pattern = build_pattern(['example.com', 'test.org'])
```
""",
    "cheatsheet": """# Regular Expressions - Cheatsheet

## Special Characters
```python
.      # Any character except newline
^      # Start of string
$      # End of string
*      # 0 or more
+      # 1 or more
?      # 0 or 1
|      # OR operator
\\      # Escape
()     # Capture group
[]     # Character class
```

## Character Classes
```python
\\d     # Digit [0-9]
\\D     # Non-digit
\\w     # Word char [a-zA-Z0-9_]
\\W     # Non-word char
\\s     # Whitespace
\\S     # Non-whitespace
[abc]  # Any of a, b, c
[^abc] # NOT a, b, c
```

## Quantifiers
```python
*      # 0 or more (greedy)
+      # 1 or more (greedy)
?      # 0 or 1 (greedy)
{n}    # Exactly n
{n,}   # At least n
{n,m}  # Between n and m
*?     # 0 or more (lazy)
+?     # 1 or more (lazy)
```

## Functions
```python
import re
re.search(pattern, text)   # Find first
re.match(pattern, text)    # Match at start
re.findall(pattern, text)  # Find all
re.sub(pattern, repl, text)  # Replace
re.split(pattern, text)    # Split
```

## Common Patterns
```python
# Email
r'^[\\w.-]+@[\\w.-]+\\.[a-z]{2,}$'

# Phone
r'^\\d{3}-\\d{3}-\\d{4}$'

# URL
r'^https?://[\\w.-]+'

# Numbers
r'\\d+'
```

## Key Points
- Use raw strings: r'pattern'
- re.compile() for reused patterns
- search() finds anywhere, match() at start
- Use (?:) for non-capturing groups
- Lookahead (?=) and lookbehind (?<=) don't consume
"""
})

# String Manipulation - Comprehensive Theory
STRING_THEORY = json.dumps({
    "beginner": """# String Manipulation - Beginner

## Introduction

Strings are sequences of characters and one of the most fundamental data types in Python. They are immutable - once created, they cannot be changed.

---

## 1. String Basics

### Creating Strings
```python
single = 'hello'
double = "hello"
triple = '''multi
line'''
raw = r'no\\escape'
```

### Immutability
```python
text = "hello"
# text[0] = 'H'  # Error! Strings are immutable

# Create a new string instead
text = 'H' + text[1:]  # "Hello"
```

---

## 2. Accessing Characters

### Indexing
```python
word = "Python"
print(word[0])   # P (first)
print(word[-1])  # n (last)
print(word[-2])  # o (second to last)
```

### Slicing
```python
text = "Programming"
print(text[0:7])   # Program
print(text[:3])    # Pro
print(text[7:])    # ming
print(text[::2])   # Pormig (every 2nd)
print(text[::-1])  # gnimmargorP (reversed)
```

---

## 3. Basic Operations

### Concatenation
```python
first = "Hello"
second = "World"
result = first + " " + second  # Hello World

# Repetition
stars = "*" * 10  # **********
```

### Membership
```python
text = "Python Programming"
print("Python" in text)      # True
print("Java" not in text)    # True
```

---

## 4. Essential Methods

### Case Conversion
```python
text = "Hello World"
print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.capitalize()) # Hello world
print(text.title())      # Hello World
```

### Finding and Checking
```python
text = "hello world"
print(text.find("world"))      # 6 (index)
print(text.startswith("hello"))  # True
print(text.endswith("world"))    # True
print(text.count("l"))           # 3
```

### Stripping
```python
text = "   hello   "
print(text.strip())   # "hello"
print(text.lstrip())  # "hello   "
print(text.rstrip())  # "   hello"
```

### Replacing
```python
text = "hello world"
print(text.replace("world", "python"))  # hello python
```

### Splitting and Joining
```python
# Split
text = "apple,banana,cherry"
parts = text.split(",")  # ['apple', 'banana', 'cherry']

# Join
result = " ".join(parts)  # "apple banana cherry"
```

---

## 5. String Formatting

### F-strings (Recommended)
```python
name = "Alice"
age = 30
print(f"Hello {name}, you are {age}")  # Hello Alice, you are 30

# Expressions
print(f"Next year: {age + 1}")  # Next year: 31

# Formatting
pi = 3.14159
print(f"Pi: {pi:.2f}")  # Pi: 3.14
```
""",
    "intermediate": """# String Manipulation - Intermediate

## 1. Advanced Formatting

### F-string Specifiers
```python
value = "test"
print(f"{value:>10}")   # '      test' (right)
print(f"{value:<10}")   # 'test      ' (left)
print(f"{value:^10}")   # '   test   ' (center)
print(f"{value:*^10}")  # '***test***' (fill)

# Numbers
num = 42
print(f"{num:05d}")     # 00042 (zero-pad)
print(f"{1000000:,}")   # 1,000,000 (comma)

# Floats
pi = 3.14159
print(f"{pi:.2f}")      # 3.14
print(f"{0.856:.1%}")   # 85.6%
```

### .format() Method
```python
"Hello {}".format("Alice")
"Hello {name}".format(name="Bob")
"{0} and {1}".format("A", "B")
```

---

## 2. Searching Methods

```python
text = "hello world hello"

# find() - returns index or -1
print(text.find("world"))    # 6
print(text.find("xyz"))      # -1

# rfind() - from right
print(text.rfind("hello"))   # 12

# index() - raises error if not found
print(text.index("world"))   # 6

# count()
print(text.count("hello"))   # 2
```

---

## 3. Splitting Operations

```python
# Basic split
"a,b,c".split(",")           # ['a', 'b', 'c']

# Split with limit
"a-b-c-d".split("-", 2)      # ['a', 'b', 'c-d']

# rsplit() - from right
"a-b-c-d".rsplit("-", 2)     # ['a-b', 'c', 'd']

# splitlines()
"a\\nb\\nc".splitlines()      # ['a', 'b', 'c']

# partition()
"user@domain.com".partition("@")  # ('user', '@', 'domain.com')
```

---

## 4. Type Checking

```python
"123".isdigit()      # True
"abc".isalpha()      # True
"abc123".isalnum()   # True
"   ".isspace()      # True
"Hello".istitle()    # True
"HELLO".isupper()    # True
"hello".islower()    # True
```

---

## 5. Encoding

```python
# String to bytes
text = "Hello"
encoded = text.encode('utf-8')  # b'Hello'

# Bytes to string
decoded = encoded.decode('utf-8')  # "Hello"

# Handle errors
text.encode('ascii', errors='ignore')
text.encode('ascii', errors='replace')
```

---

## 6. Practical Examples

### CSV Parsing
```python
line = "John,30,john@example.com"
name, age, email = line.split(",")
print(f"Name: {name}, Email: {email}")
```

### Query String Parsing
```python
query = "name=John&age=30"
params = dict(pair.split("=") for pair in query.split("&"))
print(params)  # {'name': 'John', 'age': '30'}
```

### Log Formatting
```python
from datetime import datetime

def format_log(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] [{level:>7}] {message}"

print(format_log("ERROR", "Connection failed"))
```
""",
    "advanced": """# String Manipulation - Advanced

## 1. String Internals

### String Interning
```python
# Small strings are often interned (share memory)
a = "hello"
b = "hello"
print(a is b)  # True - same object

# Dynamically created strings usually aren't
a = "".join(["hel", "lo"])
b = "hello"
print(a is b)  # False - different objects

# Force interning
import sys
a = sys.intern("hello")
b = sys.intern("hello")
print(a is b)  # True
```

---

## 2. Performance Optimization

### Concatenation Performance
```python
# BAD - O(n^2) complexity
result = ""
for i in range(1000):
    result = result + str(i)

# GOOD - O(n) complexity
parts = []
for i in range(1000):
    parts.append(str(i))
result = "".join(parts)

# BEST - list comprehension
result = "".join(str(i) for i in range(1000))
```

### StringIO for Large Strings
```python
from io import StringIO

output = StringIO()
for i in range(10000):
    output.write(f"Line {i}\\n")
result = output.getvalue()
```

---

## 3. Unicode Handling

### Normalization
```python
import unicodedata

text1 = "Café"        # é as single char
text2 = "Cafe\\u0301"  # e + combining accent

print(text1 == text2)  # False

# Normalize to compare
nfc1 = unicodedata.normalize('NFC', text1)
nfc2 = unicodedata.normalize('NFC', text2)
print(nfc1 == nfc2)  # True
```

### Character Info
```python
text = "Café"
for char in text:
    print(f"{char}: U+{ord(char):04X}")
# C: U+0043
# a: U+0061
# f: U+0066
# é: U+00E9
```

---

## 4. Advanced Formatting

### Custom __format__
```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __format__(self, spec):
        if spec.endswith('F'):
            value = (self.celsius * 9/5) + 32
            return f"{value:.{spec[:-1] or '0'}f}°F"
        return f"{self.celsius}°C"

temp = Temperature(25)
print(f"{temp:2F}")  # 77.00°F
```

### Format Spec Mini-Language
```python
# [[fill]align][sign][#][0][width][,][.precision][type]
value = 42
print(f"{value:+d}")    # +42
print(f"{value:#x}")    # 0x2a
print(f"{value:08d}")   # 00000042
print(f"{value:b}")     # 101010 (binary)
```

---

## 5. Memory-Efficient Processing

### Generator-Based Processing
```python
def process_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip().upper()

# Process without loading entire file
for line in process_lines('large_file.txt'):
    print(line)
```

### Chunked Processing
```python
def process_chunks(text, chunk_size=1000):
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        yield chunk.upper()
```
""",
    "cheatsheet": """# String Manipulation - Cheatsheet

## Creation
```python
s = 'single'
s = "double"
s = '''multi\\nline'''
s = r'raw\\string'
```

## Accessing
```python
s[0]      # First char
s[-1]     # Last char
s[1:4]    # Slice
s[::-1]   # Reverse
len(s)    # Length
```

## Methods
```python
# Case
s.upper(), s.lower()
s.capitalize(), s.title()

# Search
s.find('x'), s.index('x')
s.startswith('x'), s.endswith('x')
s.count('x')

# Modify
s.strip(), s.lstrip(), s.rstrip()
s.replace('old', 'new')

# Split/Join
s.split(',')
','.join(list)
s.splitlines()

# Check
s.isdigit(), s.isalpha()
s.isalnum(), s.isspace()
```

## Formatting
```python
# F-strings
f"{name}"           # Variable
f"{value:.2f}"      # 2 decimals
f"{value:>10}"      # Right-align
f"{value:,}"        # Comma separator

# .format()
"Hello {}".format(name)
```

## Encoding
```python
s.encode('utf-8')   # To bytes
b.decode('utf-8')   # From bytes
```

## Key Points
- Strings are immutable
- Use f-strings for formatting
- Use join() instead of += in loops
- split() and join() are inverses
"""
})

# Collections Module - Comprehensive Theory
COLLECTIONS_THEORY = json.dumps({
    "beginner": """# Collections Module - Beginner

## Introduction

The `collections` module provides specialized container datatypes that extend Python's built-in types. They solve common problems more elegantly.

---

## 1. Why Use Collections?

```python
# Problem: Counting with regular dict
word_count = {}
for word in words:
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1

# Solution: Use Counter
from collections import Counter
word_count = Counter(words)
```

---

## 2. defaultdict

A dict that never raises KeyError - it creates missing keys automatically.

```python
from collections import defaultdict

# With int factory - missing keys default to 0
counts = defaultdict(int)
for word in ['apple', 'banana', 'apple']:
    counts[word] += 1
print(counts)  # {'apple': 2, 'banana': 1}

# With list factory - missing keys default to []
groups = defaultdict(list)
groups['fruits'].append('apple')
groups['fruits'].append('banana')
print(groups)  # {'fruits': ['apple', 'banana']}

# With set factory - missing keys default to set()
tags = defaultdict(set)
tags['python'].add('programming')
tags['python'].add('language')
```

---

## 3. Counter

Count occurrences of elements in any iterable.

```python
from collections import Counter

# Count characters
letters = Counter("mississippi")
print(letters)  # {'i': 4, 's': 4, 'p': 2, 'm': 1}

# Count words
words = Counter(['apple', 'banana', 'apple', 'cherry'])
print(words['apple'])  # 2

# Most common
print(letters.most_common(2))  # [('i', 4), ('s', 4)]
```

---

## 4. deque

Double-ended queue with O(1) operations on both ends.

```python
from collections import deque

# Create
d = deque([1, 2, 3])

# Add elements
d.append(4)       # Right: [1, 2, 3, 4]
d.appendleft(0)   # Left: [0, 1, 2, 3, 4]

# Remove elements
d.pop()           # Remove from right
d.popleft()       # Remove from left - O(1)!

# Compare to list: list.pop(0) is O(n)
```

---

## 5. namedtuple

Tuple with named fields for readable code.

```python
from collections import namedtuple

# Define
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age city')

# Create
p = Point(10, 20)
person = Person('Alice', 30, 'NYC')

# Access by name
print(p.x, p.y)        # 10 20
print(person.name)     # Alice

# Still works like a tuple
x, y = p
print(list(p))  # [10, 20]
```

---

## 6. When to Use Each

| Need | Use |
|------|-----|
| Default values for missing keys | `defaultdict` |
| Count occurrences | `Counter` |
| Fast operations at both ends | `deque` |
| Tuple with named fields | `namedtuple` |
""",
    "intermediate": """# Collections Module - Intermediate

## 1. defaultdict Patterns

### Different Factory Functions
```python
from collections import defaultdict

# int: counting
counts = defaultdict(int)
counts['a'] += 1

# list: grouping
groups = defaultdict(list)
groups['key'].append('value')

# set: unique grouping
tags = defaultdict(set)
tags['key'].add('value')

# dict: nested dicts
nested = defaultdict(dict)
nested['user']['name'] = 'Alice'

# lambda: custom default
d = defaultdict(lambda: 'N/A')
print(d['missing'])  # 'N/A'
```

---

## 2. Counter Deep Dive

### Arithmetic Operations
```python
from collections import Counter

c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

print(c1 + c2)  # Counter({'a': 4, 'b': 3})
print(c1 - c2)  # Counter({'a': 2}) (no negatives)
print(c1 & c2)  # Counter({'a': 1, 'b': 1}) (min)
print(c1 | c2)  # Counter({'a': 3, 'b': 2}) (max)
```

### Useful Methods
```python
from collections import Counter

c = Counter(a=4, b=2, c=0, d=-2)

# most_common
print(c.most_common(2))  # [('a', 4), ('b', 2)]

# elements() - iterator of elements
print(list(c.elements()))  # ['a', 'a', 'a', 'a', 'b', 'b']

# total()
print(c.total())  # 4 (sum of counts)

# subtract()
c.subtract({'a': 1, 'b': 1})
print(c)  # Counter({'a': 3, 'b': 1, 'c': 0, 'd': -2})
```

---

## 3. deque Operations

### Rotation and Bounded Deques
```python
from collections import deque

# Rotate
d = deque([1, 2, 3, 4, 5])
d.rotate(2)   # [4, 5, 1, 2, 3]
d.rotate(-1)  # [5, 1, 2, 3, 4]

# Bounded deque (circular buffer)
d = deque(maxlen=3)
d.extend([1, 2, 3])  # [1, 2, 3]
d.append(4)          # [2, 3, 4] (1 dropped)
d.appendleft(0)      # [0, 2, 3] (4 dropped)
```

### Useful Methods
```python
from collections import deque

d = deque([1, 2, 3, 2, 1])

# extend both sides
d.extend([4, 5])       # Right
d.extendleft([0, -1])  # Left (reversed!)

# count and index
print(d.count(2))   # 2
print(d.index(3))   # Find first occurrence

# reverse
d.reverse()

# clear
d.clear()
```

---

## 4. namedtuple Patterns

### Advanced Usage
```python
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])
p = Person('Alice', 30, 'NYC')

# Convert to dict
print(p._asdict())  # {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# Create with replace
p2 = p._replace(age=31)
print(p2)  # Person(name='Alice', age=31, city='NYC')

# Defaults (Python 3.7+)
Person = namedtuple('Person', ['name', 'age', 'city'], defaults=['Unknown', 0, 'N/A'])
p = Person('Bob')  # Person(name='Bob', age=0, city='N/A')
```

---

## 5. Practical Examples

### Word Frequency
```python
from collections import Counter

text = "the quick brown fox jumps over the lazy dog"
words = Counter(text.lower().split())
print(words.most_common(3))
# [('the', 2), ('quick', 1), ('brown', 1)]
```

### Grouping Data
```python
from collections import defaultdict

data = [
    ('Alice', 'Math', 90),
    ('Bob', 'Math', 85),
    ('Alice', 'Science', 88),
]

by_student = defaultdict(list)
for name, subject, score in data:
    by_student[name].append((subject, score))

print(dict(by_student))
# {'Alice': [('Math', 90), ('Science', 88)], 'Bob': [('Math', 85)]}
```

### Sliding Window
```python
from collections import deque

def moving_average(values, window_size):
    window = deque(maxlen=window_size)
    for value in values:
        window.append(value)
        if len(window) == window_size:
            yield sum(window) / window_size

data = [1, 2, 3, 4, 5, 6, 7]
print(list(moving_average(data, 3)))
# [2.0, 3.0, 4.0, 5.0, 6.0]
```
""",
    "advanced": """# Collections Module - Advanced

## 1. OrderedDict

Dict that remembers insertion order (less needed since Python 3.7+, but has unique methods).

```python
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

# Move to end
od.move_to_end('a')
print(list(od.keys()))  # ['b', 'c', 'a']

# Move to beginning
od.move_to_end('c', last=False)
print(list(od.keys()))  # ['c', 'b', 'a']

# Pop from end
od.popitem()            # Removes 'a'
od.popitem(last=False)  # Removes 'c'
```

### LRU Cache Implementation
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

---

## 2. ChainMap

View multiple dicts as one without copying.

```python
from collections import ChainMap

defaults = {'color': 'red', 'size': 'medium'}
user_settings = {'color': 'blue'}

config = ChainMap(user_settings, defaults)
print(config['color'])  # 'blue' (from user_settings)
print(config['size'])   # 'medium' (from defaults)

# Updates go to first dict
config['size'] = 'large'
print(user_settings)  # {'color': 'blue', 'size': 'large'}
```

### Scoped Variables
```python
from collections import ChainMap

def make_scope(parent=None):
    if parent is None:
        return ChainMap({})
    return parent.new_child()

# Usage
global_scope = make_scope()
global_scope['x'] = 10

local_scope = make_scope(global_scope)
local_scope['y'] = 20

print(local_scope['x'])  # 10 (from parent)
print(local_scope['y'])  # 20 (local)
```

---

## 3. UserDict, UserList, UserString

Base classes for creating custom container types.

```python
from collections import UserDict

class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)

    def __getitem__(self, key):
        return super().__getitem__(key.lower())

d = CaseInsensitiveDict()
d['Name'] = 'Alice'
print(d['NAME'])  # 'Alice'
print(d['name'])  # 'Alice'
```

---

## 4. Performance Comparison

```python
import timeit
from collections import deque

# list.pop(0) vs deque.popleft()
lst = list(range(10000))
dq = deque(range(10000))

# List: O(n) for pop(0)
# timeit: lst.pop(0) ~0.1ms

# Deque: O(1) for popleft()
# timeit: dq.popleft() ~0.00001ms

# For 10000 operations:
# list.pop(0): ~100ms
# deque.popleft(): ~1ms
```

### When to Use What

| Operation | list | deque | dict | Counter |
|-----------|------|-------|------|---------|
| append | O(1) | O(1) | - | - |
| prepend | O(n) | O(1) | - | - |
| pop last | O(1) | O(1) | - | - |
| pop first | O(n) | O(1) | - | - |
| random access | O(1) | O(n) | O(1) | O(1) |
| membership | O(n) | O(n) | O(1) | O(1) |

---

## 5. Advanced Patterns

### Nested defaultdict
```python
from collections import defaultdict

def nested_dict():
    return defaultdict(nested_dict)

data = nested_dict()
data['users']['alice']['email'] = 'alice@example.com'
data['users']['bob']['email'] = 'bob@example.com'
```

### Counter for Bag/Multiset
```python
from collections import Counter

# Multiset operations
bag1 = Counter(a=3, b=2)
bag2 = Counter(a=1, b=4)

# Union (max of each)
print(bag1 | bag2)  # Counter({'b': 4, 'a': 3})

# Intersection (min of each)
print(bag1 & bag2)  # Counter({'a': 1, 'b': 2})
```
""",
    "cheatsheet": """# Collections Module - Cheatsheet

## Imports
```python
from collections import (
    defaultdict, Counter, deque,
    namedtuple, OrderedDict, ChainMap
)
```

## defaultdict
```python
d = defaultdict(int)      # Missing -> 0
d = defaultdict(list)     # Missing -> []
d = defaultdict(set)      # Missing -> set()
d = defaultdict(lambda: 'N/A')  # Custom
```

## Counter
```python
c = Counter('abracadabra')
c.most_common(2)          # Top 2
c.elements()              # Iterator
c.total()                 # Sum
c1 + c2, c1 - c2          # Arithmetic
c1 & c2, c1 | c2          # Min/max
```

## deque
```python
d = deque([1, 2, 3])
d.append(4)               # Right
d.appendleft(0)           # Left O(1)
d.pop(), d.popleft()      # Both O(1)
d.rotate(2)               # Rotate
d = deque(maxlen=3)       # Bounded
```

## namedtuple
```python
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
p.x, p.y                  # Named access
p._asdict()               # To dict
p._replace(x=5)           # New with change
```

## OrderedDict
```python
od = OrderedDict()
od.move_to_end('key')     # Move to end
od.popitem(last=False)    # Pop first
```

## ChainMap
```python
config = ChainMap(user, defaults)
config['key']             # Searches in order
config.new_child()        # New scope
```

## Key Points
- defaultdict: No more KeyError
- Counter: Counting made easy
- deque: O(1) at both ends
- namedtuple: Readable tuples
- OrderedDict: Order matters
- ChainMap: Layered dicts
"""
})

# Date & Time - Comprehensive Theory
DATETIME_THEORY = json.dumps({
    "beginner": """# Date & Time - Beginner

## Introduction

The datetime module handles dates and times in Python. Common pitfalls include timezone confusion and format string errors.

---

## 1. The datetime Module

```python
from datetime import datetime, date, time, timedelta
```

| Class | Purpose |
|-------|---------|
| `date` | Year, month, day only |
| `time` | Hour, minute, second only |
| `datetime` | Both date and time |
| `timedelta` | Duration/difference |

---

## 2. Creating Date and Time Objects

### date
```python
from datetime import date

today = date.today()
christmas = date(2024, 12, 25)

print(christmas.year)    # 2024
print(christmas.month)   # 12
print(christmas.day)     # 25
print(christmas.weekday())  # 2 (0=Monday)
```

### time
```python
from datetime import time

noon = time(12, 0, 0)
precise = time(14, 30, 45, 123456)

print(precise.hour)        # 14
print(precise.minute)      # 30
print(precise.second)      # 45
```

### datetime
```python
from datetime import datetime

now = datetime.now()
specific = datetime(2024, 12, 25, 14, 30, 45)

print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)

# Extract date or time part
just_date = now.date()
just_time = now.time()
```

---

## 3. Comparing Dates

```python
from datetime import datetime

date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12, 31)

print(date1 < date2)   # True
print(date1 == date1)  # True

# Sorting
dates = [date2, date1]
sorted_dates = sorted(dates)
```

---

## 4. Best Practices

```python
# Use datetime objects, not strings
# Bad
date_str = "2024-12-25"

# Good
date_obj = datetime(2024, 12, 25)

# Months are 1-12, not 0-11
# weekday() returns 0-6 (Monday=0)
```
""",
    "intermediate": """# Date & Time - Intermediate

## 1. Formatting with strftime()

```python
from datetime import datetime

now = datetime(2024, 12, 25, 14, 30, 45)

# Common formats
print(now.strftime('%Y-%m-%d'))           # 2024-12-25
print(now.strftime('%m/%d/%Y'))           # 12/25/2024
print(now.strftime('%A, %B %d, %Y'))      # Wednesday, December 25, 2024
print(now.strftime('%Y-%m-%d %H:%M:%S'))  # 2024-12-25 14:30:45
print(now.strftime('%I:%M %p'))           # 02:30 PM
```

### Format Codes
```python
%Y  # 4-digit year (2024)
%m  # Month (01-12)
%d  # Day (01-31)
%H  # Hour 24h (00-23)
%I  # Hour 12h (01-12)
%M  # Minute (00-59)
%S  # Second (00-59)
%A  # Full weekday (Wednesday)
%B  # Full month (December)
%p  # AM/PM
```

---

## 2. Parsing with strptime()

```python
from datetime import datetime

# Parse string to datetime
dt = datetime.strptime("2024-12-25", '%Y-%m-%d')
dt = datetime.strptime("12/25/2024", '%m/%d/%Y')
dt = datetime.strptime("2024-12-25 14:30:45", '%Y-%m-%d %H:%M:%S')

# Now use as datetime object
print(dt.year)  # 2024
```

### Flexible Parsing
```python
from datetime import datetime

def parse_date(date_str):
    formats = ['%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y']
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Cannot parse: {date_str}")
```

---

## 3. Date Arithmetic with timedelta

```python
from datetime import datetime, timedelta

now = datetime.now()

# Add time
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
in_2_hours = now + timedelta(hours=2)

# Subtract time
yesterday = now - timedelta(days=1)

# Combined
later = now + timedelta(days=5, hours=3, minutes=30)
```

### Calculating Differences
```python
from datetime import datetime

date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12, 31)

diff = date2 - date1
print(diff.days)           # 365
print(diff.total_seconds())  # 31536000.0
```

---

## 4. Common Patterns

### Age Calculation
```python
from datetime import datetime

def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

birth = datetime(2000, 5, 15)
print(calculate_age(birth))
```

### Date Range
```python
from datetime import datetime, timedelta

def date_range(start, end):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)

for dt in date_range(datetime(2024, 1, 1), datetime(2024, 1, 7)):
    print(dt.strftime('%Y-%m-%d'))
```

### Is Weekend?
```python
from datetime import datetime

def is_weekend(dt):
    return dt.weekday() >= 5  # 5=Sat, 6=Sun
```
""",
    "advanced": """# Date & Time - Advanced

## 1. Naive vs Aware Datetimes

```python
from datetime import datetime, timezone

# Naive (no timezone info)
naive = datetime.now()
print(naive.tzinfo)  # None

# Aware (has timezone info)
aware = datetime.now(timezone.utc)
print(aware.tzinfo)  # UTC

# Always use aware datetimes in production!
```

---

## 2. The zoneinfo Module (Python 3.9+)

```python
from zoneinfo import ZoneInfo
from datetime import datetime

# Create with timezone
tokyo = ZoneInfo("Asia/Tokyo")
tokyo_time = datetime(2024, 12, 25, 14, 30, tzinfo=tokyo)

# Current time in timezone
ny = ZoneInfo("America/New_York")
ny_time = datetime.now(ny)

# Convert between timezones
utc = ZoneInfo("UTC")
utc_time = tokyo_time.astimezone(utc)
```

### Common Timezones
```python
from zoneinfo import ZoneInfo

eastern = ZoneInfo("America/New_York")
pacific = ZoneInfo("America/Los_Angeles")
london = ZoneInfo("Europe/London")
tokyo = ZoneInfo("Asia/Tokyo")
utc = ZoneInfo("UTC")
```

---

## 3. Working with UTC

```python
from zoneinfo import ZoneInfo
from datetime import datetime

# Always store in UTC
utc = ZoneInfo("UTC")
stored_time = datetime.now(utc)

# Convert to ISO format for storage
iso_str = stored_time.isoformat()
# '2024-01-29T15:30:45.123456+00:00'

# Parse back
retrieved = datetime.fromisoformat(iso_str)

# Convert to local for display
ny = ZoneInfo("America/New_York")
display_time = retrieved.astimezone(ny)
```

---

## 4. DST Handling

```python
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

eastern = ZoneInfo("America/New_York")

# Spring forward (2:00 AM becomes 3:00 AM)
before = datetime(2024, 3, 10, 1, 30, tzinfo=eastern)
after = before + timedelta(hours=1)
print(after)  # 2024-03-10 03:30:00-04:00 (automatic!)
```

---

## 5. Unix Timestamps

```python
from datetime import datetime
from zoneinfo import ZoneInfo

# DateTime to timestamp
now = datetime.now(ZoneInfo("UTC"))
timestamp = now.timestamp()

# Timestamp to datetime (always use UTC!)
dt = datetime.fromtimestamp(timestamp, tz=ZoneInfo("UTC"))
```

---

## 6. Performance Tips

```python
from zoneinfo import ZoneInfo
from datetime import datetime

# Cache timezone objects
eastern = ZoneInfo("America/New_York")

# Reuse in loops
for _ in range(1000):
    now = datetime.now(eastern)  # Don't create ZoneInfo each time
```
""",
    "cheatsheet": """# Date & Time - Cheatsheet

## Imports
```python
from datetime import datetime, date, time, timedelta
from zoneinfo import ZoneInfo  # Python 3.9+
```

## Current Date/Time
```python
datetime.now()              # Local (naive)
datetime.now(ZoneInfo("UTC"))  # UTC (aware)
date.today()                # Just date
```

## Creating
```python
date(2024, 12, 25)
time(14, 30, 45)
datetime(2024, 12, 25, 14, 30)
```

## Format Codes
```python
%Y  # Year 2024
%m  # Month 01-12
%d  # Day 01-31
%H  # Hour 00-23
%M  # Minute 00-59
%S  # Second 00-59
%A  # Wednesday
%B  # December
```

## Formatting/Parsing
```python
# Format (datetime -> string)
dt.strftime('%Y-%m-%d')

# Parse (string -> datetime)
datetime.strptime("2024-12-25", '%Y-%m-%d')

# ISO format
dt.isoformat()
datetime.fromisoformat(iso_str)
```

## Arithmetic
```python
dt + timedelta(days=1)
dt - timedelta(hours=2)
diff = dt2 - dt1
diff.days, diff.total_seconds()
```

## Timezones
```python
utc = ZoneInfo("UTC")
ny = ZoneInfo("America/New_York")
dt = datetime.now(utc)
local = dt.astimezone(ny)
```

## Key Points
- Use aware datetimes in production
- Store times in UTC
- strftime = datetime -> string
- strptime = string -> datetime
- Months are 1-12, weekday 0-6
"""
})

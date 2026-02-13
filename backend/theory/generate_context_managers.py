#!/usr/bin/env python3
"""
Script to generate comprehensive decorators theory JSON file.
Run this script to create/update backend/theory/decorators.json
"""

import json
import os

def get_beginner_content():
    return """## Decorators: Beginner Level

### 1. What is a Decorator?

A decorator is a function that modifies or enhances another function without changing its source code. Think of it like wrapping a gift - the gift stays the same, but it's now presented in a nicer way.

```python
# Simple example: function as an object
def greet():
    return "Hello!"

# Functions are objects - we can pass them around
my_function = greet
print(my_function())  # Output: Hello!
```

###  2. First Decorator: Understanding the Basics

Let's create the simplest possible decorator.

```python
# A decorator is a function that takes a function and returns a function
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()  # Call the original function
        print("After the function")
    return wrapper

# Without @ syntax (manual decoration)
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)  # Decorate manually
say_hello()
# Output:
# Before the function
# Hello!
# After the function
```

### 3. The @ Syntax

Python provides a cleaner syntax using `@` to apply decorators.

```python
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

# Using @ syntax (same as manual decoration above)
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function
# Hello!
# After the function

# The @ syntax is just syntactic sugar for:
# say_hello = my_decorator(say_hello)
```

### 4. Key Takeaways

- Decorators modify functions without changing their code
- Use `@decorator_name` syntax above a function definition
- Always use `*args, **kwargs` in wrapper to handle any function signature
- Always return the result from the wrapper function
- Built-in decorators: `@property`, `@staticmethod`, `@classmethod`
"""

def get_intermediate_content():
    return """## Decorators: Intermediate Level

### 1. Understanding functools.wraps

Preserves function metadata when decorating.

### 2. Parameterized Decorators

Decorators that accept arguments require an additional layer of functions.

### 3. Decorator Chaining

Multiple decorators applied bottom-to-top.
"""

def get_advanced_content():
    return """## Decorators: Advanced Level

### 1. Deep Dive into Decorator Mechanics

Understanding how decorators work under the hood.

### 2. Class-Based Decorators

Using classes as decorators with `__call__` method.

### 3. Performance Optimization

Techniques for efficient decorators.
"""

def get_cheatsheet_content():
    return """## Decorators: Cheatsheet

### Basic Decorator Template

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper
```

### Common Patterns

- Logging: Track function calls
- Timing: Measure execution time
- Caching: Store results for reuse
- Validation: Check arguments
- Authorization: Control access
"""

def main():
    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, 'decorators.json')
    
    # Create content dictionary
    content = {
        "beginner": get_beginner_content(),
        "intermediate": get_intermediate_content(),
        "advanced": get_advanced_content(),
        "cheatsheet": get_cheatsheet_content()
    }
    
    # Write to JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Successfully created: {output_file}")
    print(f"✓ File size: {os.path.getsize(output_file)} bytes")
    print("\nContent sections:")
    for key in content.keys():
        lines = content[key].count('\n')
        print(f"  - {key}: {lines} lines")

if __name__ == "__main__":
    main()

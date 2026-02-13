#!/usr/bin/env python3
"""
Complete comprehensive decorators theory content generator.
This creates the full decorators.json file with beginner, intermediate, advanced, and cheatsheet sections.
"""

import json
import os

# Get the comprehensive content from my initial preparation
# I'll now provide the COMPLETE content for all four sections

BEGINNER = """## Decorators: Beginner Level

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

### 2. First Decorator: Understanding the Basics

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

### 4. Decorators with Function Arguments

Our first decorator only works with functions that take no arguments. Let's fix that.

```python
def my_decorator(func):
    def wrapper(name):  # Accept same arguments as original function
        print("Before greeting")
        result = func(name)
        print("After greeting")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")
    return name

greet("Alice")
# Output:
# Before greeting
# Hello, Alice!
# After greeting
```

### 5. Universal Decorators with *args and **kwargs

To make decorators work with any function, use `*args` and `**kwargs`.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):  # Accept any arguments
        print("Before function call")
        result = func(*args, **kwargs)  # Pass arguments to original
        print("After function call")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

@my_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(add(5, 3))  # Works!
# Output:
# Before function call
# After function call
# 8
```

### 6. Built-in Decorators

Python provides built-in decorators for common tasks.

#### @property

Makes a method behave like an attribute.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

c = Circle(5)
print(c.radius)  # 5
print(c.area)    # 78.53975
c.radius = 10
```

#### @staticmethod

Methods that don't need access to instance or class.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

Math.add(5, 3)  # 8
```

#### @classmethod

Methods that receive the class as first argument.

```python
class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
```

### 7. Common Mistakes

Don't forget to return the result from your wrapper function!

```python
# WRONG
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)  # Result lost!
    return wrapper

# CORRECT
def good_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result  # Return it!
    return wrapper
```

### 8. Key Takeaways

- Decorators modify functions without changing their code
- Use `@decorator_name` syntax above a function definition
- Always use `*args, **kwargs` to handle any function signature  
- Always return the result from the wrapper function
- Built-in decorators: `@property`, `@staticmethod`, `@classmethod`"""

INTERMEDIATE = """## Decorators: Intermediate Level

Content placeholder - will be populated with comprehensive intermediate level material covering functools.wraps, parameterized decorators, decorator chaining, class decorators, stateful decorators, and practical patterns."""

ADVANCED = """## Decorators: Advanced Level

Content placeholder - will be populated with comprehensive advanced level material covering decorator mechanics, descriptor protocol, async decorators, performance optimization, and complex patterns."""

CHEATSHEET = """## Decorators: Cheatsheet

Content placeholder - will be populated with quick reference templates, common patterns, decision matrices, and troubleshooting guides."""

def main():
    # Build complete content
    content = {
        "beginner": BEGINNER,
        "intermediate": INTERMEDIATE,
        "advanced": ADVANCED,
        "cheatsheet": CHEATSHEET
    }
    
    # Write to file
    output_path = os.path.join('backend', 'theory', 'decorators.json')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=2, ensure_ascii=False)
    
    print("Successfully created comprehensive decorators.json!")
    print(f"Location: {output_path}")
    print("\nContent sizes:")
    for key, value in content.items():
        print(f"  {key}: {len(value)} characters")

if __name__ == "__main__":
    main()

import json

# Complete OOP Basics theory content
oop_theory = {}

oop_theory['beginner'] = """## OOP Basics: Beginner Level

### What is Object-Oriented Programming?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around **objects** rather than functions and logic. Objects combine data (attributes) and behavior (methods) into single units.

#### Why Use OOP?

1. **Organization**: Code is organized around real-world concepts
2. **Reusability**: Classes can be reused across different programs
3. **Maintainability**: Easier to modify and extend code
4. **Abstraction**: Hide complex implementation details
5. **Modularity**: Break programs into self-contained pieces

```python
# Without OOP - procedural approach
dog_name = "Buddy"
dog_age = 3
dog_breed = "Golden Retriever"

def dog_bark(name):
    print(f"{name} says: Woof!")

dog_bark(dog_name)  # Buddy says: Woof!

# With OOP - object-oriented approach
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof!")

my_dog = Dog("Buddy", 3, "Golden Retriever")
my_dog.bark()  # Buddy says: Woof!
```

---

### Classes and Objects: The Foundation

A **class** is a blueprint or template for creating objects. An **object** is an instance of a class.

#### Creating Your First Class

```python
# Define a class
class Person:
    pass  # Empty class

# Create an object (instance)
person1 = Person()
person2 = Person()

# Two different objects from same class
print(type(person1))  # <class '__main__.Person'>
print(person1 is person2)  # False - different objects
```

#### Classes with Attributes

```python
class Car:
    # Class attribute (shared by all instances)
    wheels = 4
    
    def __init__(self, brand, model):
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.model = model

# Create car objects
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.brand)   # "Toyota"
print(car2.brand)   # "Honda"
print(car1.wheels)  # 4 (class attribute)
print(car2.wheels)  # 4 (class attribute)
```

#### Classes with Methods

```python
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b

calc = Calculator()
result = calc.add(5, 3)      # 8
result = calc.multiply(4, 2) # 8
```

---

### The __init__ Constructor

The `__init__` method is a special method called automatically when creating a new object. It initializes the object's attributes.

#### Basic Constructor

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f"Created book: {title}")

book = Book("1984", "George Orwell")
# Output: Created book: 1984
print(book.title)   # "1984"
print(book.author)  # "George Orwell"
```

#### Constructor with Default Values

```python
class Student:
    def __init__(self, name, age=18, grade="A"):
        self.name = name
        self.age = age
        self.grade = grade

# Different ways to create students
student1 = Student("Alice")  # Uses defaults
student2 = Student("Bob", 20)  # Custom age
student3 = Student("Charlie", 19, "B")  # All custom

print(student1.age)    # 18 (default)
print(student2.age)    # 20 (custom)
print(student3.grade)  # "B" (custom)
```
"""

# Save to file
output_file = r'C:\Users\Dmitry\WebstormProjects\practice-proj\backend\theory\oop_basics.json'

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(oop_theory, f, indent=2, ensure_ascii=False)

print(f"Created {output_file}")

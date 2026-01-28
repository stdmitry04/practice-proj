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
# Structure: name, slug, description, position_x, position_y, keywords, parent_slug
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
    },
]


# JavaScript roadmap node definitions (28 nodes)
JAVASCRIPT_NODES = [
    # Level 0 - Root
    {
        "name": "Types & Primitives",
        "slug": "types-primitives",
        "description": "JavaScript fundamental data types",
        "position_x": 400,
        "position_y": 0,
        "keywords": ["number", "string", "boolean", "null", "undefined", "symbol", "bigint"],
        "parent_slug": None,
        "order_index": 0,
    },
    # Level 1 (2 nodes)
    {
        "name": "Type Coercion & Quirks",
        "slug": "type-coercion",
        "description": "JavaScript type system peculiarities",
        "position_x": 280,
        "position_y": 100,
        "keywords": ["==", "===", "typeof null", "NaN", "truthy/falsy"],
        "parent_slug": "types-primitives",
        "order_index": 0,
    },
    {
        "name": "Variables & Declarations",
        "slug": "variables",
        "description": "Variable declaration and scoping",
        "position_x": 520,
        "position_y": 100,
        "keywords": ["var", "let", "const", "hoisting", "TDZ"],
        "parent_slug": "types-primitives",
        "order_index": 1,
    },
    # Level 2 (2 nodes)
    {
        "name": "Objects Deep Dive",
        "slug": "objects",
        "description": "Working with objects in JavaScript",
        "position_x": 280,
        "position_y": 200,
        "keywords": ["object literals", "property access", "Object methods"],
        "parent_slug": "type-coercion",
        "order_index": 0,
    },
    {
        "name": "Prototypes & Inheritance",
        "slug": "prototypes",
        "description": "Prototype-based inheritance",
        "position_x": 520,
        "position_y": 200,
        "keywords": ["[[Prototype]]", "__proto__", "prototype chain"],
        "parent_slug": "type-coercion",
        "order_index": 1,
    },
    # Level 3 (2 nodes)
    {
        "name": "Prototype Methods",
        "slug": "prototype-methods",
        "description": "Working with prototypes",
        "position_x": 280,
        "position_y": 300,
        "keywords": ["Object.create", "setPrototypeOf", "hasOwnProperty"],
        "parent_slug": "prototypes",
        "order_index": 0,
    },
    {
        "name": "Functions Fundamentals",
        "slug": "functions",
        "description": "Function types and patterns",
        "position_x": 520,
        "position_y": 300,
        "keywords": ["declarations", "expressions", "arrow", "default params"],
        "parent_slug": "objects",
        "order_index": 0,
    },
    # Level 4 (2 nodes)
    {
        "name": "this Binding",
        "slug": "this-binding",
        "description": "Understanding 'this' context",
        "position_x": 280,
        "position_y": 400,
        "keywords": ["implicit", "explicit", "call/apply/bind", "arrow this"],
        "parent_slug": "functions",
        "order_index": 0,
    },
    {
        "name": "Closures & Scope",
        "slug": "closures",
        "description": "Lexical scoping and closures",
        "position_x": 520,
        "position_y": 400,
        "keywords": ["lexical scope", "closure patterns", "IIFE", "module pattern"],
        "parent_slug": "functions",
        "order_index": 1,
    },
    # Level 5 (2 nodes)
    {
        "name": "Arrays In-Depth",
        "slug": "arrays",
        "description": "Array methods and manipulation",
        "position_x": 280,
        "position_y": 500,
        "keywords": ["map", "filter", "reduce", "flat", "flatMap"],
        "parent_slug": "closures",
        "order_index": 0,
    },
    {
        "name": "Iterators & Iterables",
        "slug": "iterators",
        "description": "Iteration protocols",
        "position_x": 520,
        "position_y": 500,
        "keywords": ["Symbol.iterator", "for...of", "custom iterators"],
        "parent_slug": "closures",
        "order_index": 1,
    },
    # Level 6 (2 nodes)
    {
        "name": "Maps & Sets",
        "slug": "maps-sets",
        "description": "Collection data structures",
        "position_x": 280,
        "position_y": 600,
        "keywords": ["Map", "Set", "WeakMap", "WeakSet"],
        "parent_slug": "arrays",
        "order_index": 0,
    },
    {
        "name": "Destructuring & Spread",
        "slug": "destructuring",
        "description": "Modern assignment patterns",
        "position_x": 520,
        "position_y": 600,
        "keywords": ["object/array destructuring", "rest", "spread"],
        "parent_slug": "arrays",
        "order_index": 1,
    },
    # Level 7 (2 nodes)
    {
        "name": "Classes",
        "slug": "classes",
        "description": "ES6 class syntax",
        "position_x": 280,
        "position_y": 700,
        "keywords": ["class syntax", "constructor", "methods", "getters/setters"],
        "parent_slug": "destructuring",
        "order_index": 0,
    },
    {
        "name": "Class Inheritance",
        "slug": "class-inheritance",
        "description": "Class-based inheritance",
        "position_x": 520,
        "position_y": 700,
        "keywords": ["extends", "super", "static", "private fields (#)"],
        "parent_slug": "destructuring",
        "order_index": 1,
    },
    # Level 8 (1 node)
    {
        "name": "Property Descriptors",
        "slug": "property-descriptors",
        "description": "Object property configuration",
        "position_x": 400,
        "position_y": 800,
        "keywords": ["defineProperty", "writable", "enumerable", "configurable"],
        "parent_slug": "class-inheritance",
        "order_index": 0,
    },
    # Level 9 (1 node)
    {
        "name": "Event Loop",
        "slug": "event-loop",
        "description": "JavaScript concurrency model",
        "position_x": 400,
        "position_y": 900,
        "keywords": ["call stack", "task queue", "microtask queue"],
        "parent_slug": "property-descriptors",
        "order_index": 0,
    },
    # Level 10 (1 node)
    {
        "name": "Callbacks & Timers",
        "slug": "callbacks-timers",
        "description": "Asynchronous callbacks",
        "position_x": 400,
        "position_y": 1000,
        "keywords": ["setTimeout", "setInterval", "callback patterns"],
        "parent_slug": "event-loop",
        "order_index": 0,
    },
    # Level 11 (1 node)
    {
        "name": "Promises",
        "slug": "promises",
        "description": "Promise-based async",
        "position_x": 400,
        "position_y": 1100,
        "keywords": ["Promise", "then/catch/finally", "Promise.all/race"],
        "parent_slug": "callbacks-timers",
        "order_index": 0,
    },
    # Level 12 (1 node)
    {
        "name": "Async/Await",
        "slug": "async-await",
        "description": "Modern async syntax",
        "position_x": 400,
        "position_y": 1200,
        "keywords": ["async functions", "await", "error handling"],
        "parent_slug": "promises",
        "order_index": 0,
    },
    # Level 13 (2 nodes)
    {
        "name": "Generators",
        "slug": "generators",
        "description": "Generator functions",
        "position_x": 280,
        "position_y": 1300,
        "keywords": ["function*", "yield", "iterator protocol", "async generators"],
        "parent_slug": "async-await",
        "order_index": 0,
    },
    {
        "name": "Modules",
        "slug": "modules",
        "description": "ES Module system",
        "position_x": 520,
        "position_y": 1300,
        "keywords": ["ES modules", "import/export", "dynamic import()"],
        "parent_slug": "async-await",
        "order_index": 1,
    },
    # Level 14 (2 nodes)
    {
        "name": "Symbols",
        "slug": "symbols",
        "description": "Symbol primitive type",
        "position_x": 280,
        "position_y": 1400,
        "keywords": ["Symbol()", "well-known symbols", "Symbol.iterator"],
        "parent_slug": "generators",
        "order_index": 0,
    },
    {
        "name": "Proxy & Reflect",
        "slug": "proxy-reflect",
        "description": "Metaprogramming APIs",
        "position_x": 520,
        "position_y": 1400,
        "keywords": ["Proxy traps", "Reflect methods", "meta-programming"],
        "parent_slug": "generators",
        "order_index": 1,
    },
    # Level 15 (2 nodes)
    {
        "name": "Error Handling",
        "slug": "error-handling",
        "description": "Exception handling patterns",
        "position_x": 280,
        "position_y": 1500,
        "keywords": ["try/catch/finally", "Error types", "custom errors"],
        "parent_slug": "proxy-reflect",
        "order_index": 0,
    },
    {
        "name": "Regular Expressions",
        "slug": "regex",
        "description": "Pattern matching with regex",
        "position_x": 520,
        "position_y": 1500,
        "keywords": ["regex syntax", "flags", "match", "replace", "named groups"],
        "parent_slug": "proxy-reflect",
        "order_index": 1,
    },
    # Level 16 (2 nodes)
    {
        "name": "JSON & Serialization",
        "slug": "json",
        "description": "JSON parsing and stringification",
        "position_x": 280,
        "position_y": 1600,
        "keywords": ["JSON.parse", "stringify", "replacer/reviver"],
        "parent_slug": "error-handling",
        "order_index": 0,
    },
    {
        "name": "Memory & Performance",
        "slug": "memory",
        "description": "Memory management in JS",
        "position_x": 520,
        "position_y": 1600,
        "keywords": ["garbage collection", "memory leaks", "WeakRef"],
        "parent_slug": "error-handling",
        "order_index": 1,
    },
]


# TypeScript roadmap node definitions (20 nodes)
TYPESCRIPT_NODES = [
    # Level 0 - Root
    {
        "name": "Type Annotations",
        "slug": "type-annotations",
        "description": "Basic TypeScript type syntax",
        "position_x": 400,
        "position_y": 0,
        "keywords": ["primitives", "arrays", "any", "unknown", "void", "never"],
        "parent_slug": None,
        "order_index": 0,
    },
    # Level 1 (1 node)
    {
        "name": "Type Inference",
        "slug": "type-inference",
        "description": "Automatic type detection",
        "position_x": 400,
        "position_y": 100,
        "keywords": ["inference rules", "contextual typing"],
        "parent_slug": "type-annotations",
        "order_index": 0,
    },
    # Level 2 (2 nodes)
    {
        "name": "Interfaces",
        "slug": "interfaces",
        "description": "Object type contracts",
        "position_x": 280,
        "position_y": 200,
        "keywords": ["interface syntax", "optional", "readonly", "extending"],
        "parent_slug": "type-inference",
        "order_index": 0,
    },
    {
        "name": "Type Aliases",
        "slug": "type-aliases",
        "description": "Custom type definitions",
        "position_x": 520,
        "position_y": 200,
        "keywords": ["type keyword", "vs interfaces"],
        "parent_slug": "type-inference",
        "order_index": 1,
    },
    # Level 3 (2 nodes)
    {
        "name": "Union Types",
        "slug": "union-types",
        "description": "Multiple type possibilities",
        "position_x": 280,
        "position_y": 300,
        "keywords": ["union syntax", "discriminated unions"],
        "parent_slug": "interfaces",
        "order_index": 0,
    },
    {
        "name": "Intersection Types",
        "slug": "intersection-types",
        "description": "Combining multiple types",
        "position_x": 520,
        "position_y": 300,
        "keywords": ["combining types", "interface merging"],
        "parent_slug": "interfaces",
        "order_index": 1,
    },
    # Level 4 (2 nodes)
    {
        "name": "Type Narrowing",
        "slug": "type-narrowing",
        "description": "Refining types at runtime",
        "position_x": 280,
        "position_y": 400,
        "keywords": ["typeof", "instanceof", "in", "type predicates"],
        "parent_slug": "union-types",
        "order_index": 0,
    },
    {
        "name": "Literal Types",
        "slug": "literal-types",
        "description": "Exact value types",
        "position_x": 520,
        "position_y": 400,
        "keywords": ["string/number literals", "as const", "template literals"],
        "parent_slug": "union-types",
        "order_index": 1,
    },
    # Level 5 (2 nodes)
    {
        "name": "Generics Basics",
        "slug": "generics-basics",
        "description": "Type parameters fundamentals",
        "position_x": 280,
        "position_y": 500,
        "keywords": ["generic functions", "interfaces", "classes"],
        "parent_slug": "type-narrowing",
        "order_index": 0,
    },
    {
        "name": "Generic Constraints",
        "slug": "generic-constraints",
        "description": "Limiting generic types",
        "position_x": 520,
        "position_y": 500,
        "keywords": ["extends", "keyof", "indexed access"],
        "parent_slug": "type-narrowing",
        "order_index": 1,
    },
    # Level 6 (2 nodes)
    {
        "name": "Conditional Types",
        "slug": "conditional-types",
        "description": "Type-level conditionals",
        "position_x": 280,
        "position_y": 600,
        "keywords": ["T extends U ? X : Y", "infer", "distributive"],
        "parent_slug": "generics-basics",
        "order_index": 0,
    },
    {
        "name": "Mapped Types",
        "slug": "mapped-types",
        "description": "Transforming types",
        "position_x": 520,
        "position_y": 600,
        "keywords": ["[K in keyof T]", "modifiers", "key remapping"],
        "parent_slug": "generics-basics",
        "order_index": 1,
    },
    # Level 7 (2 nodes)
    {
        "name": "Built-in Utility Types",
        "slug": "utility-types",
        "description": "Standard type helpers",
        "position_x": 280,
        "position_y": 700,
        "keywords": ["Partial", "Required", "Readonly", "Pick", "Omit", "Record"],
        "parent_slug": "mapped-types",
        "order_index": 0,
    },
    {
        "name": "Advanced Utility Types",
        "slug": "advanced-utility",
        "description": "Complex type utilities",
        "position_x": 520,
        "position_y": 700,
        "keywords": ["Exclude", "Extract", "ReturnType", "Parameters"],
        "parent_slug": "mapped-types",
        "order_index": 1,
    },
    # Level 8 (1 node)
    {
        "name": "Custom Utility Types",
        "slug": "custom-utilities",
        "description": "Building your own utilities",
        "position_x": 400,
        "position_y": 800,
        "keywords": ["recursive types", "type challenges"],
        "parent_slug": "advanced-utility",
        "order_index": 0,
    },
    # Level 9 (2 nodes)
    {
        "name": "Declaration Files",
        "slug": "declaration-files",
        "description": "Type definitions for JS",
        "position_x": 280,
        "position_y": 900,
        "keywords": [".d.ts", "declare", "ambient modules"],
        "parent_slug": "custom-utilities",
        "order_index": 0,
    },
    {
        "name": "Module Augmentation",
        "slug": "module-augmentation",
        "description": "Extending existing types",
        "position_x": 520,
        "position_y": 900,
        "keywords": ["declare module", "global augmentation"],
        "parent_slug": "custom-utilities",
        "order_index": 1,
    },
    # Level 10 (2 nodes)
    {
        "name": "Decorators",
        "slug": "decorators",
        "description": "Metadata and modification",
        "position_x": 280,
        "position_y": 1000,
        "keywords": ["experimental decorators", "metadata"],
        "parent_slug": "module-augmentation",
        "order_index": 0,
    },
    {
        "name": "Enums",
        "slug": "enums",
        "description": "Enumeration types",
        "position_x": 520,
        "position_y": 1000,
        "keywords": ["numeric", "string", "const enums"],
        "parent_slug": "module-augmentation",
        "order_index": 1,
    },
    # Level 11 (1 node)
    {
        "name": "Compiler Configuration",
        "slug": "compiler-config",
        "description": "tsconfig.json setup",
        "position_x": 400,
        "position_y": 1100,
        "keywords": ["tsconfig.json", "strict mode"],
        "parent_slug": "enums",
        "order_index": 0,
    },
]


# React roadmap node definitions (26 nodes)
REACT_NODES = [
    # Level 0 - Root
    {
        "name": "JSX & Elements",
        "slug": "jsx",
        "description": "JSX syntax fundamentals",
        "position_x": 400,
        "position_y": 0,
        "keywords": ["JSX syntax", "createElement", "fragments", "keys"],
        "parent_slug": None,
        "order_index": 0,
    },
    # Level 1 (1 node)
    {
        "name": "Components",
        "slug": "components",
        "description": "Building React components",
        "position_x": 400,
        "position_y": 100,
        "keywords": ["functional", "props", "children", "composition"],
        "parent_slug": "jsx",
        "order_index": 0,
    },
    # Level 2 (1 node)
    {
        "name": "Conditional & List Rendering",
        "slug": "conditional-rendering",
        "description": "Dynamic content rendering",
        "position_x": 400,
        "position_y": 200,
        "keywords": ["&&", "ternary", "map()", "key prop"],
        "parent_slug": "components",
        "order_index": 0,
    },
    # Level 3 (2 nodes)
    {
        "name": "useState",
        "slug": "use-state",
        "description": "Component state management",
        "position_x": 280,
        "position_y": 300,
        "keywords": ["state", "setter functions", "lazy init", "batching"],
        "parent_slug": "conditional-rendering",
        "order_index": 0,
    },
    {
        "name": "useEffect",
        "slug": "use-effect",
        "description": "Side effects in components",
        "position_x": 520,
        "position_y": 300,
        "keywords": ["effects", "cleanup", "dependencies", "strict mode"],
        "parent_slug": "conditional-rendering",
        "order_index": 1,
    },
    # Level 4 (2 nodes)
    {
        "name": "useContext",
        "slug": "use-context",
        "description": "Consuming context values",
        "position_x": 280,
        "position_y": 400,
        "keywords": ["createContext", "Provider", "consuming"],
        "parent_slug": "use-state",
        "order_index": 0,
    },
    {
        "name": "useReducer",
        "slug": "use-reducer",
        "description": "Complex state logic",
        "position_x": 520,
        "position_y": 400,
        "keywords": ["reducer pattern", "dispatch", "actions"],
        "parent_slug": "use-state",
        "order_index": 1,
    },
    # Level 5 (2 nodes)
    {
        "name": "useRef",
        "slug": "use-ref",
        "description": "Mutable refs and DOM access",
        "position_x": 280,
        "position_y": 500,
        "keywords": ["mutable refs", "DOM refs", "preserving values"],
        "parent_slug": "use-context",
        "order_index": 0,
    },
    {
        "name": "useMemo",
        "slug": "use-memo",
        "description": "Memoizing computed values",
        "position_x": 520,
        "position_y": 500,
        "keywords": ["memoizing values", "dependency array"],
        "parent_slug": "use-context",
        "order_index": 1,
    },
    # Level 6 (2 nodes)
    {
        "name": "useCallback",
        "slug": "use-callback",
        "description": "Memoizing functions",
        "position_x": 280,
        "position_y": 600,
        "keywords": ["memoizing functions", "referential equality"],
        "parent_slug": "use-memo",
        "order_index": 0,
    },
    {
        "name": "useLayoutEffect",
        "slug": "use-layout-effect",
        "description": "Synchronous DOM effects",
        "position_x": 520,
        "position_y": 600,
        "keywords": ["vs useEffect", "DOM measurements"],
        "parent_slug": "use-memo",
        "order_index": 1,
    },
    # Level 7 (2 nodes)
    {
        "name": "useImperativeHandle",
        "slug": "use-imperative-handle",
        "description": "Customizing ref exposure",
        "position_x": 280,
        "position_y": 700,
        "keywords": ["exposing methods", "forwardRef"],
        "parent_slug": "use-callback",
        "order_index": 0,
    },
    {
        "name": "useDebugValue",
        "slug": "use-debug-value",
        "description": "DevTools debugging",
        "position_x": 520,
        "position_y": 700,
        "keywords": ["custom hook debugging"],
        "parent_slug": "use-callback",
        "order_index": 1,
    },
    # Level 8 (2 nodes)
    {
        "name": "useSyncExternalStore",
        "slug": "use-sync-external-store",
        "description": "External store subscriptions",
        "position_x": 280,
        "position_y": 800,
        "keywords": ["external stores", "SSR"],
        "parent_slug": "use-imperative-handle",
        "order_index": 0,
    },
    {
        "name": "useId",
        "slug": "use-id",
        "description": "Unique ID generation",
        "position_x": 520,
        "position_y": 800,
        "keywords": ["unique IDs", "accessibility"],
        "parent_slug": "use-imperative-handle",
        "order_index": 1,
    },
    # Level 9 (2 nodes)
    {
        "name": "Custom Hooks",
        "slug": "custom-hooks",
        "description": "Extracting reusable logic",
        "position_x": 280,
        "position_y": 900,
        "keywords": ["extracting logic", "composition"],
        "parent_slug": "use-sync-external-store",
        "order_index": 0,
    },
    {
        "name": "Composition Patterns",
        "slug": "composition-patterns",
        "description": "Component design patterns",
        "position_x": 520,
        "position_y": 900,
        "keywords": ["render props", "compound components"],
        "parent_slug": "use-sync-external-store",
        "order_index": 1,
    },
    # Level 10 (2 nodes)
    {
        "name": "Context Patterns",
        "slug": "context-patterns",
        "description": "Advanced context usage",
        "position_x": 280,
        "position_y": 1000,
        "keywords": ["multiple contexts", "optimization"],
        "parent_slug": "custom-hooks",
        "order_index": 0,
    },
    {
        "name": "State Management",
        "slug": "state-management",
        "description": "Application state strategies",
        "position_x": 520,
        "position_y": 1000,
        "keywords": ["lifting state", "prop drilling"],
        "parent_slug": "custom-hooks",
        "order_index": 1,
    },
    # Level 11 (2 nodes)
    {
        "name": "React.memo",
        "slug": "react-memo",
        "description": "Component memoization",
        "position_x": 280,
        "position_y": 1100,
        "keywords": ["shallow comparison", "custom comparison"],
        "parent_slug": "context-patterns",
        "order_index": 0,
    },
    {
        "name": "Code Splitting",
        "slug": "code-splitting",
        "description": "Lazy loading components",
        "position_x": 520,
        "position_y": 1100,
        "keywords": ["React.lazy", "Suspense", "route-based"],
        "parent_slug": "context-patterns",
        "order_index": 1,
    },
    # Level 12 (1 node)
    {
        "name": "Profiling & Optimization",
        "slug": "profiling",
        "description": "Performance analysis",
        "position_x": 400,
        "position_y": 1200,
        "keywords": ["DevTools", "memoization strategies"],
        "parent_slug": "react-memo",
        "order_index": 0,
    },
    # Level 13 (2 nodes)
    {
        "name": "Error Boundaries",
        "slug": "error-boundaries",
        "description": "Error handling in React",
        "position_x": 280,
        "position_y": 1300,
        "keywords": ["getDerivedStateFromError", "fallback UI"],
        "parent_slug": "profiling",
        "order_index": 0,
    },
    {
        "name": "Portals",
        "slug": "portals",
        "description": "Rendering outside DOM hierarchy",
        "position_x": 520,
        "position_y": 1300,
        "keywords": ["createPortal", "modal patterns"],
        "parent_slug": "profiling",
        "order_index": 1,
    },
    # Level 14 (2 nodes)
    {
        "name": "Concurrent Features",
        "slug": "concurrent-features",
        "description": "React 18 concurrent rendering",
        "position_x": 280,
        "position_y": 1400,
        "keywords": ["useTransition", "useDeferredValue"],
        "parent_slug": "error-boundaries",
        "order_index": 0,
    },
    {
        "name": "Server Components",
        "slug": "server-components",
        "description": "React Server Components",
        "position_x": 520,
        "position_y": 1400,
        "keywords": ["RSC", "server vs client", "data fetching"],
        "parent_slug": "error-boundaries",
        "order_index": 1,
    },
]


# C++ roadmap node definitions (32 nodes)
CPP_NODES = [
    # Level 0 - Root
    {
        "name": "Types & Syntax",
        "slug": "types-syntax",
        "description": "C++ fundamental types and syntax",
        "position_x": 400,
        "position_y": 0,
        "keywords": ["primitives", "sizeof", "literals", "auto"],
        "parent_slug": None,
        "order_index": 0,
    },
    # Level 1 (2 nodes)
    {
        "name": "Pointers",
        "slug": "pointers",
        "description": "Pointer fundamentals",
        "position_x": 280,
        "position_y": 100,
        "keywords": ["declaration", "dereference", "address-of", "nullptr"],
        "parent_slug": "types-syntax",
        "order_index": 0,
    },
    {
        "name": "References",
        "slug": "references",
        "description": "Reference types",
        "position_x": 520,
        "position_y": 100,
        "keywords": ["lvalue references", "const references"],
        "parent_slug": "types-syntax",
        "order_index": 1,
    },
    # Level 2 (1 node)
    {
        "name": "Memory Layout",
        "slug": "memory-layout",
        "description": "Program memory organization",
        "position_x": 400,
        "position_y": 200,
        "keywords": ["stack", "heap", "static", "alignment"],
        "parent_slug": "pointers",
        "order_index": 0,
    },
    # Level 3 (2 nodes)
    {
        "name": "Dynamic Memory",
        "slug": "dynamic-memory",
        "description": "Heap allocation",
        "position_x": 280,
        "position_y": 300,
        "keywords": ["new/delete", "placement new"],
        "parent_slug": "memory-layout",
        "order_index": 0,
    },
    {
        "name": "Arrays",
        "slug": "arrays",
        "description": "C-style arrays",
        "position_x": 520,
        "position_y": 300,
        "keywords": ["C-arrays", "array decay", "pointer arithmetic"],
        "parent_slug": "memory-layout",
        "order_index": 1,
    },
    # Level 4 (1 node)
    {
        "name": "Memory Pitfalls",
        "slug": "memory-pitfalls",
        "description": "Common memory errors",
        "position_x": 400,
        "position_y": 400,
        "keywords": ["leaks", "dangling pointers", "double free"],
        "parent_slug": "dynamic-memory",
        "order_index": 0,
    },
    # Level 5 (2 nodes)
    {
        "name": "Function Basics",
        "slug": "function-basics",
        "description": "Function fundamentals",
        "position_x": 280,
        "position_y": 500,
        "keywords": ["pass by value/ref/pointer", "overloading"],
        "parent_slug": "memory-pitfalls",
        "order_index": 0,
    },
    {
        "name": "Function Pointers",
        "slug": "function-pointers",
        "description": "Pointers to functions",
        "position_x": 520,
        "position_y": 500,
        "keywords": ["syntax", "callbacks", "typedef"],
        "parent_slug": "memory-pitfalls",
        "order_index": 1,
    },
    # Level 6 (1 node)
    {
        "name": "Lambdas (C++11)",
        "slug": "lambdas",
        "description": "Lambda expressions",
        "position_x": 400,
        "position_y": 600,
        "keywords": ["lambda syntax", "captures", "mutable", "generic"],
        "parent_slug": "function-basics",
        "order_index": 0,
    },
    # Level 7 (2 nodes)
    {
        "name": "Classes",
        "slug": "classes",
        "description": "Class fundamentals",
        "position_x": 280,
        "position_y": 700,
        "keywords": ["class vs struct", "access specifiers", "this"],
        "parent_slug": "lambdas",
        "order_index": 0,
    },
    {
        "name": "Constructors",
        "slug": "constructors",
        "description": "Object initialization",
        "position_x": 520,
        "position_y": 700,
        "keywords": ["default", "parameterized", "initializer lists"],
        "parent_slug": "lambdas",
        "order_index": 1,
    },
    # Level 8 (2 nodes)
    {
        "name": "Destructors & RAII",
        "slug": "destructors-raii",
        "description": "Resource management",
        "position_x": 280,
        "position_y": 800,
        "keywords": ["destructor", "RAII", "resource management"],
        "parent_slug": "constructors",
        "order_index": 0,
    },
    {
        "name": "Copy Semantics",
        "slug": "copy-semantics",
        "description": "Copy operations",
        "position_x": 520,
        "position_y": 800,
        "keywords": ["copy constructor", "assignment", "rule of three"],
        "parent_slug": "constructors",
        "order_index": 1,
    },
    # Level 9 (2 nodes)
    {
        "name": "Move Semantics (C++11)",
        "slug": "move-semantics",
        "description": "Move operations",
        "position_x": 280,
        "position_y": 900,
        "keywords": ["rvalue refs", "std::move", "rule of five"],
        "parent_slug": "copy-semantics",
        "order_index": 0,
    },
    {
        "name": "Operator Overloading",
        "slug": "operator-overloading",
        "description": "Custom operators",
        "position_x": 520,
        "position_y": 900,
        "keywords": ["arithmetic", "comparison", "stream"],
        "parent_slug": "copy-semantics",
        "order_index": 1,
    },
    # Level 10 (2 nodes)
    {
        "name": "unique_ptr",
        "slug": "unique-ptr",
        "description": "Exclusive ownership",
        "position_x": 280,
        "position_y": 1000,
        "keywords": ["exclusive ownership", "make_unique"],
        "parent_slug": "move-semantics",
        "order_index": 0,
    },
    {
        "name": "shared_ptr & weak_ptr",
        "slug": "shared-weak-ptr",
        "description": "Shared ownership",
        "position_x": 520,
        "position_y": 1000,
        "keywords": ["reference counting", "make_shared"],
        "parent_slug": "move-semantics",
        "order_index": 1,
    },
    # Level 11 (2 nodes)
    {
        "name": "Inheritance",
        "slug": "inheritance",
        "description": "Class inheritance",
        "position_x": 280,
        "position_y": 1100,
        "keywords": ["public/protected/private", "is-a"],
        "parent_slug": "unique-ptr",
        "order_index": 0,
    },
    {
        "name": "Virtual Functions",
        "slug": "virtual-functions",
        "description": "Runtime polymorphism",
        "position_x": 520,
        "position_y": 1100,
        "keywords": ["vtable", "virtual", "override", "final"],
        "parent_slug": "unique-ptr",
        "order_index": 1,
    },
    # Level 12 (1 node)
    {
        "name": "Abstract Classes",
        "slug": "abstract-classes",
        "description": "Interfaces in C++",
        "position_x": 400,
        "position_y": 1200,
        "keywords": ["pure virtual", "interfaces"],
        "parent_slug": "virtual-functions",
        "order_index": 0,
    },
    # Level 13 (2 nodes)
    {
        "name": "Function Templates",
        "slug": "function-templates",
        "description": "Generic functions",
        "position_x": 280,
        "position_y": 1300,
        "keywords": ["template syntax", "deduction", "specialization"],
        "parent_slug": "abstract-classes",
        "order_index": 0,
    },
    {
        "name": "Class Templates",
        "slug": "class-templates",
        "description": "Generic classes",
        "position_x": 520,
        "position_y": 1300,
        "keywords": ["template classes", "partial specialization"],
        "parent_slug": "abstract-classes",
        "order_index": 1,
    },
    # Level 14 (1 node)
    {
        "name": "Variadic Templates (C++11)",
        "slug": "variadic-templates",
        "description": "Variable argument templates",
        "position_x": 400,
        "position_y": 1400,
        "keywords": ["parameter packs", "fold expressions"],
        "parent_slug": "function-templates",
        "order_index": 0,
    },
    # Level 15 (2 nodes)
    {
        "name": "Containers",
        "slug": "containers",
        "description": "STL containers",
        "position_x": 280,
        "position_y": 1500,
        "keywords": ["vector", "map", "set", "unordered"],
        "parent_slug": "variadic-templates",
        "order_index": 0,
    },
    {
        "name": "Iterators",
        "slug": "iterators",
        "description": "Iterator categories",
        "position_x": 520,
        "position_y": 1500,
        "keywords": ["categories", "begin/end", "range-based for"],
        "parent_slug": "variadic-templates",
        "order_index": 1,
    },
    # Level 16 (1 node)
    {
        "name": "Algorithms",
        "slug": "algorithms",
        "description": "STL algorithms",
        "position_x": 400,
        "position_y": 1600,
        "keywords": ["sort", "find", "transform", "accumulate"],
        "parent_slug": "containers",
        "order_index": 0,
    },
    # Level 17 (2 nodes)
    {
        "name": "Structured Bindings (C++17)",
        "slug": "structured-bindings",
        "description": "Decomposition declarations",
        "position_x": 280,
        "position_y": 1700,
        "keywords": ["auto [a, b]", "tuple unpacking"],
        "parent_slug": "algorithms",
        "order_index": 0,
    },
    {
        "name": "std::optional & variant (C++17)",
        "slug": "optional-variant",
        "description": "Sum types",
        "position_x": 520,
        "position_y": 1700,
        "keywords": ["optional", "variant", "std::visit"],
        "parent_slug": "algorithms",
        "order_index": 1,
    },
    # Level 18 (2 nodes)
    {
        "name": "Concepts (C++20)",
        "slug": "concepts",
        "description": "Template constraints",
        "position_x": 280,
        "position_y": 1800,
        "keywords": ["requires", "concept definition"],
        "parent_slug": "optional-variant",
        "order_index": 0,
    },
    {
        "name": "Ranges (C++20)",
        "slug": "ranges",
        "description": "Range library",
        "position_x": 520,
        "position_y": 1800,
        "keywords": ["range adaptors", "views"],
        "parent_slug": "optional-variant",
        "order_index": 1,
    },
    # Level 19 (1 node)
    {
        "name": "Coroutines (C++20)",
        "slug": "coroutines",
        "description": "Coroutine support",
        "position_x": 400,
        "position_y": 1900,
        "keywords": ["co_await", "co_yield", "co_return"],
        "parent_slug": "concepts",
        "order_index": 0,
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


def seed_python_roadmap():
    """Seed only the Python roadmap (for backwards compatibility)."""
    db: Session = SessionLocal()

    try:
        python_lang = ensure_language(db, "Python", "python", "python")
        seed_roadmap(db, python_lang, PYTHON_NODES)
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
        seed_python_roadmap()
    else:
        seed_all_roadmaps(force)

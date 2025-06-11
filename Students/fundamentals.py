import math

"""


1. Variables and Data Types
---------------------------
Python supports several data types: int, float, str, bool, list, tuple, dict, set.

Examples:
"""
x = 10            # int
pi = 3.14         # float
name = "Alice"    # str
is_valid = True   # bool

# List
numbers = [1, 2, 3, 4]

# Tuple
coordinates = (10, 20)

# Dictionary
person = {"name": "Bob", "age": 25}

# Set
unique_numbers = {1, 2, 3}

"""
2. Control Flow
---------------
Python uses if, elif, else for conditional statements.
"""

age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")

"""
Loops:
- for loop: iterate over sequences
- while loop: repeat while condition is True
"""

for n in numbers:
    print(n)

count = 0
while count < 3:
    print(count)
    count += 1

"""
3. Functions
------------
Functions are defined using 'def'.
"""

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

"""
4. Classes and Objects
----------------------
Python is object-oriented. Define classes using 'class'.
"""

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

dog = Dog("Buddy")
dog.bark()

"""
5. Importing Modules
--------------------
Use 'import' to use standard or external libraries.
"""

print(math.sqrt(16))

"""
6. Input and Output
-------------------
Use input() for user input and print() for output.
"""

# name = input("Enter your name: ")
# print("Hello,", name)

"""
7. Comments
-----------
Use # for single-line comments and triple quotes for multi-line comments.
"""

# This is a single-line comment

"""
This is a
multi-line comment
"""

"""
End of Python Fundamentals Overview
"""
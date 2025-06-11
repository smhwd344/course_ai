"""
Mega Project: Student Management System (Fill in the Gaps)
----------------------------------------------------------
Complete the code to build a simple student management system.
Use variables, data types, control flow, functions, classes, data structures, and input/output.
"""

# 1. Define a Student class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        # Add the grade to the grades list
        pass

    def average(self):
        # Return the average of grades, or 0 if no grades
        pass

    def __str__(self):
        # Return a string like: "Alice (Age: 20) - Avg Grade: 85.00"
        pass

# 2. Store students in a dictionary
students = {}

# 3. Main loop
while True:
    print("\nStudent Management System")
    print("1. Add student")
    print("2. Add grade")
    print("3. Show all students")
    print("4. Show student details")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        # Add a new Student to the students dictionary
        pass

    elif choice == "2":
        name = input("Enter student name: ")
        if name in students:
            grade = float(input("Enter grade: "))
            # Add the grade to the student's grades
            pass
        else:
            print("Student not found.")

    elif choice == "3":
        # Print all students
        pass

    elif choice == "4":
        name = input("Enter student name: ")
        if name in students:
            student = students[name]
            # Print student details: name, age, grades, average
            pass
        else:
            print("Student not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
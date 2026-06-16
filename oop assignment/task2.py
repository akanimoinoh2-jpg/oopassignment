# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


# Student Class (inherits from Person)
class Student(Person):
    school_name = "FutureLabs"  # Class Variable

    def __init__(self, name, age, skill):
        super().__init__(name, age)
        self.skill = skill  # Object Variable

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"I am learning {self.skill} at {Student.school_name}.")


# FutureLabs Management Class
class FutureLabs:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been added successfully.")

    def display_students(self):
        print("\n--- FutureLabs Students ---")
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Skill: {student.skill}")

    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None


# Creating Student Objects
student1 = Student("John", 20, "Python Development")
student2 = Student("Mary", 22, "Web Development")
student3 = Student("David", 25, "Data Science")

# Creating FutureLabs System
futurelabs = FutureLabs()

# Adding Students
futurelabs.add_student(student1)
futurelabs.add_student(student2)
futurelabs.add_student(student3)

# Display All Students
futurelabs.display_students()

# Search for a Student
student = futurelabs.find_student("Mary")

if student:
    print("\nStudent Found:")
    student.introduce()
else:
    print("Student not found.")
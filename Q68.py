class Person:
    def get_name(self):
        self.name = input("Enter name: ")

class Marks:
    def get_marks(self):
        self.marks = int(input("Enter marks: "))

# Multiple Inheritance
class Student(Person, Marks):
    def display(self):
        print(f"\nName: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
s = Student()
s.get_name()
s.get_marks()
s.display()

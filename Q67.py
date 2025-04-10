class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = ""

    def read_info(self):
        self.name = input("Enter student's name: ")
        self.roll_no = input("Enter roll number: ")

class DisplayStudent(Student):
    def print_info(self):
        print("\n--- Student Information ---")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)

student1 = DisplayStudent()
student1.read_info()
student1.print_info()

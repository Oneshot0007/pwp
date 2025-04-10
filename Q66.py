class Employee:
    def __init__(self):
        self.name = ""
        self.department = ""
        self.salary = 0

    def read_info(self):
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")
        self.salary = float(input("Enter salary: "))

    def print_info(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)

# Example usage
emp = Employee()
emp.read_info()
emp.print_info()

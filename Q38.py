#Create a file named name_module.py

# name_module.py
def get_full_name():
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    return fname + " " + lname


#and after  Use the module in another Python file:
# main.py

import name_module
full_name = name_module.get_full_name()
print("Full Name is:", full_name)

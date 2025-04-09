#create a file 
# company_module.py

def get_company_details():
    name = input("Enter your Company Name: ")
    address = input("Enter your Company Address: ")
    return name, address


#after create another file name main.py and import the companya_module.py


# main.py

import company_module

company_name, company_address = company_module.get_company_details()

print("\n--- Company Details ---")
print("Company Name   :", company_name)
print("Company Address:", company_address)

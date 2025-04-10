class PasswordError(Exception):
    pass

def check_password(password):
    if password != "admin123":
        raise PasswordError("Incorrect Password!")
    else:
        print("Access Granted")

# Example usage
try:
    pwd = input("Enter password: ")
    check_password(pwd)
except PasswordError as e:
    print(e)

def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n - 1)

try:
    ui = int(input("Enter a non-negative number: "))
    if ui < 0:
        print("Invalid number! Please enter a non-negative integer.")
    else:
        res = facto(ui)
        print(f"Factorial of {ui} is: {res}")
except ValueError:
    print("Invalid input! Please enter an integer.")

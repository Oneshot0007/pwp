import math

num = float(input("Enter a number: "))

if num >= 0:
    result = math.sqrt(num)
    print(f"Square root of {num} is {result:.2f}")
else:
    print("Square root is not defined for negative numbers.")

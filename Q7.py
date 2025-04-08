# 7. Write a Python function to calculate square of a number.
def cal_square(num):
  return num*num

number =int(input("Enter Number:"))
res = cal_square(number)
print(f"square of {number} is {res}")

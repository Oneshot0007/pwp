import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[7, 8], [9, 10], [11, 12]])

add = a + b


sub = a - b

mul = a * b

div = a / b

print("Matrix A:\n", a)
print("\nMatrix B:\n", b)
print("\nAddition:\n", add)
print("\nSubtraction:\n", sub)
print("\nElement-wise Multiplication:\n", mul)
print("\nElement-wise Division:\n", div)

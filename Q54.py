import math

def calculate_circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

r = float(input("Enter radius of the circle: "))
area, circumference = calculate_circle(r)

print(f"Area of circle: {area:.2f}")
print(f"Circumference of circle: {circumference:.2f}")

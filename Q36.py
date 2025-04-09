import math

def cylinder_surface_area_volume(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    volume = math.pi * radius ** 2 * height
    return surface_area, volume

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

area, vol = cylinder_surface_area_volume(r, h)
print(f"Surface Area = {area:.2f}")
print(f"Volume = {vol:.2f}")

def calculate_volume(radius):
    return (4/3) * 3.14 * radius**3

def calculate_surface_area(radius):
    return 4 * 3.14 * radius**2

radius = float(input("Enter the radius of the sphere: "))
volume = calculate_volume(radius)
surface_area = calculate_surface_area(radius)

print(f"Surface area of the sphere: {surface_area:.2f}cm^2")
print(f"Volume of the sphere: {volume:.2f}cm^3")

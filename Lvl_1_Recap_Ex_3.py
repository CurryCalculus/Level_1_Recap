total_volume = 0

while True:
    building_type = input("Enter building type (residential or commercial, or 'x' to finish): ").lower()
    if building_type == 'x':
        break

    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    depth = float(input("Enter the depth: "))

    thickness_factor = 1 if building_type == 'commercial' else 0.5
    thickness = 0.5 * thickness_factor
    volume = length * width * thickness
    total_volume += volume

    print(f"The volume of concrete required for a slab with a length of {length}m, "
          f"width of {width}m, and a depth of {depth}m is {volume:.2f} cubic meters.")

print(f"\nTotal volume of concrete required for all jobs: {total_volume:.2f} cubic meters.")

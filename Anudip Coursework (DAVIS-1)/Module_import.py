import Geometry_3D_utils as geo

from Geometry_3D_utils import cube_measurements, cuboid_measurements

# Example usage of cube_measurements
side = float(input("Enter the side length of the cube: "))
surface_area, volume = cube_measurements(side)
print(f"Cube Surface Area: {surface_area}")
print(f"Cube Volume: {volume}")


# Example usage of cuboid_measurements
length = float(input("Enter the length of the cuboid: "))
breadth = float(input("Enter the breadth of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))
surface_area, volume = cuboid_measurements(length, breadth, height)
print(f"Cuboid Surface Area: {surface_area}")
print(f"Cuboid Volume: {volume}")


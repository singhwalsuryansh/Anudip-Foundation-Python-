# Create a module that contains the functions to perform all the operation on 3D Figures (Cube, Cuboid, Sphere, Hemisphere) without using any built-in function or library. The functions should be able to calculate the surface area and volume of the respective 3D figure.


def cube_measurements(side  ):
    surface_area = 6 * side**2
    volume = side**3
    return surface_area, volume

def cuboid_measurements(length, breadth, height):

    surface_area = 2 * (length * breadth + breadth * height + height * length)
    volume = length * breadth * height
    return surface_area, volume


def sphere_measurements(radius):

    surface_area = 4 * 3.14 * radius**2
    volume = (4/3) * 3.14 * radius**3
    return surface_area, volume


def hemisphere_measurements(radius):

    surface_area = 3 * 3.14 * radius**2
    volume = (2/3) * 3.14 * radius**3
    return surface_area, volume


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


# Example usage of sphere_measurements
radius = float(input("Enter the radius of the sphere: "))
surface_area, volume = sphere_measurements(radius)
print(f"Sphere Surface Area: {surface_area}")
print(f"Sphere Volume: {volume}")


# Example usage of hemisphere_measurements
radius = float(input("Enter the radius of the hemisphere: "))
surface_area, volume = hemisphere_measurements(radius)
print(f"Hemisphere Surface Area: {surface_area}")
print(f"Hemisphere Volume: {volume}")



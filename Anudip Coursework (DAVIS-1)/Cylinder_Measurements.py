# Write a progrm to find out the Curved Surface Area, Total Surface Area and Volume of a Cylinder by creating, a user defined function. (without importing any modules)

def cylinder_measurements(radius, height):
    # Curved Surface Area
    curved_surface_area = 2 * 3.14 * radius * height
    
    # Total Surface Area
    total_surface_area = 2 * 3.14 * radius*height + 2 * 3.14 * radius**2
    
    # Volume
    volume = 3.14 * radius**2 * height
    
    return curved_surface_area, total_surface_area, volume

# Example usage:

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
curved_surface_area, total_surface_area, volume = cylinder_measurements(radius, height)
print(f"Curved Surface Area: {curved_surface_area}")
print(f"Total Surface Area: {total_surface_area}")
print(f"Volume: {volume}")

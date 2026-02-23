# Write a program to find out the Curaved Surface Area, Total Surface Area and Volume of a Cone by creating, a user defined function. (without importing any modules)

def cone_measurements(radius, height):
    # Curved Surface Area
    curved_surface_area = 3.14 * radius * (radius**2 + height**2)**0.5
    
    # Total Surface Area
    total_surface_area = curved_surface_area + 3.14 * radius**2
    
    # Volume
    volume = (1/3) * 3.14 * radius**2 * height
    
    return curved_surface_area, total_surface_area, volume

# Example usage:
radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))
curved_surface_area, total_surface_area, volume = cone_measurements(radius, height)
print(f"Curved Surface Area: {curved_surface_area}")
print(f"Total Surface Area: {total_surface_area}")
print(f"Volume: {volume}")

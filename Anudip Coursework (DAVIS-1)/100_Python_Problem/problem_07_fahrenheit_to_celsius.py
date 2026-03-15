# ============================================================
# Problem 7: Convert Temperature from Fahrenheit to Celsius
# ============================================================
# Formula: C = (F - 32) * 5/9
#
# Example:
#   Input:  212°F
#   Output: 100.0°C
# ============================================================

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# ---- Read input ----
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F = {celsius:.2f}°C")

# ============================================================
# Sample Output:
#   Enter temperature in Fahrenheit: 212
#   212.0°F = 100.00°C
# ============================================================

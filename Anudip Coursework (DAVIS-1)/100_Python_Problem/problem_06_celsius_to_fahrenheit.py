# ============================================================
# Problem 6: Convert Temperature from Celsius to Fahrenheit
# ============================================================
# Formula: F = (C * 9/5) + 32
#
# Example:
#   Input:  100°C
#   Output: 212.0°F
# ============================================================

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# ---- Read input ----
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C = {fahrenheit:.2f}°F")

# ============================================================
# Sample Output:
#   Enter temperature in Celsius: 100
#   100.0°C = 212.00°F
# ============================================================

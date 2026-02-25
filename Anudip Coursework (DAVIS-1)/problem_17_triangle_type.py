# ============================================================
# Problem 17: Determine the Type of Triangle
# ============================================================
# Types:
#   Equilateral  → all three sides equal
#   Isosceles    → exactly two sides equal
#   Scalene      → all three sides different
#   Invalid      → triangle inequality violated
#
# Triangle Inequality: sum of any two sides must be > third side
#
# Example:
#   Input:  5 5 5 → Equilateral Triangle
#   Input:  5 5 3 → Isosceles Triangle
#   Input:  3 4 5 → Scalene Triangle
# ============================================================

def triangle_type(a, b, c):
    # Check triangle validity
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid Triangle (violates triangle inequality)"

    if a == b == c:
        return "Equilateral Triangle"
    elif a == b or b == c or a == c:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

# ---- Read input ----
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

print(f"\nTriangle with sides {a}, {b}, {c}:")
print(triangle_type(a, b, c))

# ============================================================
# Sample Output:
#   Enter side a: 5
#   Enter side b: 5
#   Enter side c: 5
#   Triangle with sides 5.0, 5.0, 5.0:
#   Equilateral Triangle
# ============================================================

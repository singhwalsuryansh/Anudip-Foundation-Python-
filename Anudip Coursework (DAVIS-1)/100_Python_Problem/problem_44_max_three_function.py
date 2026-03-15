# ============================================================
# Problem 44: Find Maximum of Three Numbers Using Function
# ============================================================
# Uses a function with explicit comparisons (no built-in max()).
#
# Example:
#   Input:  4, 11, 7
#   Output: Maximum = 11
# ============================================================

def find_max(a, b, c):
    """Return the maximum of three numbers."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# ---- Read input ----
a = float(input("Enter first number:  "))
b = float(input("Enter second number: "))
c = float(input("Enter third number:  "))

print(f"\nMaximum of {a}, {b}, {c} = {find_max(a, b, c)}")

# ============================================================
# Sample Output:
#   Enter first number:  4
#   Enter second number: 11
#   Enter third number:  7
#   Maximum of 4.0, 11.0, 7.0 = 11.0
# ============================================================

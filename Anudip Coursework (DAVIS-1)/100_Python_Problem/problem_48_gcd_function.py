# ============================================================
# Problem 48: Find GCD Using Function (Euclidean Algorithm)
# ============================================================
# GCD (Greatest Common Divisor) of two numbers a and b is the
# largest number that divides both without a remainder.
#
# Example:
#   Input:  56, 98
#   Output: GCD = 14
# ============================================================

def gcd(a, b):
    """Return the GCD of a and b using the Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b   # Euclidean step
    return a

# ---- Read input ----
a = int(input("Enter first number:  "))
b = int(input("Enter second number: "))

print(f"\nGCD({a}, {b}) = {gcd(a, b)}")

# ============================================================
# Sample Output:
#   Enter first number:  56
#   Enter second number: 98
#   GCD(56, 98) = 14
# ============================================================

# ============================================================
# Problem 1: Swap Two Numbers Without Using a Third Variable
# ============================================================
# Approach: Use Python's tuple unpacking or arithmetic to swap
# without introducing a temporary variable.
#
# Example:
#   Input:  a = 5, b = 10
#   Output: After swapping: a = 10, b = 5
# ============================================================

def swap(a, b):
    # Method 1: Pythonic tuple unpacking
    a, b = b, a
    return a, b

def swap_arithmetic(a, b):
    # Method 2: Using arithmetic (addition/subtraction)
    a = a + b   # a now holds sum
    b = a - b   # b gets original a
    a = a - b   # a gets original b
    return a, b

# ---- Read input ----
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"\nBefore swapping: a = {a}, b = {b}")

a, b = swap(a, b)

print(f"After  swapping: a = {a}, b = {b}")

# ============================================================
# Sample Output:
#   Enter first number (a): 5
#   Enter second number (b): 10
#   Before swapping: a = 5, b = 10
#   After  swapping: a = 10, b = 5
# ============================================================

# ============================================================
# Problem 3: Find the Largest of Three Numbers
# ============================================================
# Approach: Compare all three using if-elif-else.
#
# Example:
#   Input:  3, 9, 6
#   Output: Largest number is: 9
# ============================================================

def largest_of_three(a, b, c):
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

print(f"Largest number is: {largest_of_three(a, b, c)}")

# ============================================================
# Sample Output:
#   Enter first number:  3
#   Enter second number: 9
#   Enter third number:  6
#   Largest number is: 9.0
# ============================================================

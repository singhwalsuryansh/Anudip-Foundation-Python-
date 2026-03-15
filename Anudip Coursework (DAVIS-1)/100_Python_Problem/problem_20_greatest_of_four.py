# ============================================================
# Problem 20: Find the Greatest of Four Numbers
# ============================================================
# Approach: Chain if-elif comparisons across all four numbers.
#
# Example:
#   Input:  3, 7, 5, 9
#   Output: Greatest number is: 9
# ============================================================

def greatest_of_four(a, b, c, d):
    if a >= b and a >= c and a >= d:
        return a
    elif b >= a and b >= c and b >= d:
        return b
    elif c >= a and c >= b and c >= d:
        return c
    else:
        return d

# ---- Read input ----
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))
d = float(input("Enter 4th number: "))

print(f"\nGreatest number is: {greatest_of_four(a, b, c, d)}")

# ============================================================
# Sample Output:
#   Enter 1st number: 3
#   Enter 2nd number: 7
#   Enter 3rd number: 5
#   Enter 4th number: 9
#   Greatest number is: 9.0
# ============================================================

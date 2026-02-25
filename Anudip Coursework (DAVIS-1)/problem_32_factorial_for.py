# ============================================================
# Problem 32: Find Factorial Using For Loop
# ============================================================
# Definition: n! = 1 × 2 × 3 × ... × n,   0! = 1
#
# Example:
#   Input:  6
#   Output: 6! = 720
# ============================================================

def factorial_for(n):
    result = 1
    for i in range(2, n + 1):   # range(2, n+1) skips multiplying by 1
        result *= i
    return result

# ---- Read input ----
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"{n}! = {factorial_for(n)}")

# ============================================================
# Sample Output:
#   Enter a non-negative integer: 6
#   6! = 720
# ============================================================

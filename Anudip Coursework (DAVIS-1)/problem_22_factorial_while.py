# ============================================================
# Problem 22: Find Factorial Using While Loop
# ============================================================
# Definition: n! = n × (n-1) × (n-2) × ... × 1
#             0! = 1 (by convention)
#
# Example:
#   Input:  5
#   Output: 5! = 120
# ============================================================

def factorial_while(n):
    if n < 0:
        return None  # factorial not defined for negatives
    result = 1
    i = 1
    while i <= n:
        result *= i   # multiply current result by i
        i += 1
    return result

# ---- Read input ----
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"{n}! = {factorial_while(n)}")

# ============================================================
# Sample Output:
#   Enter a non-negative integer: 5
#   5! = 120
# ============================================================

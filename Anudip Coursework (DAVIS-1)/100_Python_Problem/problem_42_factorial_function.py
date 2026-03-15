# ============================================================
# Problem 42: Find Factorial Using Function
# ============================================================
# Uses a dedicated function with a loop to compute n!
# 0! = 1  (base case)
#
# Example:
#   Input:  7
#   Output: 7! = 5040
# ============================================================

def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):    # multiply from 2 up to n
        result *= i
    return result

# ---- Read input ----
n = int(input("Enter a non-negative integer: "))

fact = factorial(n)
if fact is None:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"{n}! = {fact}")

# ============================================================
# Sample Output:
#   Enter a non-negative integer: 7
#   7! = 5040
# ============================================================

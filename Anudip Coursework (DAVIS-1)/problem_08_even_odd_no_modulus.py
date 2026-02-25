# ============================================================
# Problem 8: Check Whether a Number is Even or Odd
#            WITHOUT Using the Modulus Operator (%)
# ============================================================
# Approach: Use bitwise AND operator.
#           n & 1 == 0  → Even
#           n & 1 == 1  → Odd
#
# Example:
#   Input:  7
#   Output: 7 is Odd
# ============================================================

def is_even_or_odd(n):
    if n & 1 == 0:   # last bit is 0 → even
        return "Even"
    else:            # last bit is 1 → odd
        return "Odd"

# ---- Read input ----
n = int(input("Enter an integer: "))

print(f"{n} is {is_even_or_odd(n)}")

# ============================================================
# Sample Output:
#   Enter an integer: 7
#   7 is Odd
# ============================================================

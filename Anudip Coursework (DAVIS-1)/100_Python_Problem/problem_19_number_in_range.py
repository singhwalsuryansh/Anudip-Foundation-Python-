# ============================================================
# Problem 19: Check Whether a Number Lies Within a Given Range
# ============================================================
# Approach: Use comparison operators to check lower <= n <= upper
#
# Example:
#   Number=15, Range=[10, 20] → 15 is within the range [10, 20]
#   Number=25, Range=[10, 20] → 25 is outside the range [10, 20]
# ============================================================

def in_range(n, lower, upper):
    return lower <= n <= upper

# ---- Read input ----
n     = float(input("Enter a number: "))
lower = float(input("Enter lower bound: "))
upper = float(input("Enter upper bound: "))

if lower > upper:
    lower, upper = upper, lower  # swap if user entered in wrong order

if in_range(n, lower, upper):
    print(f"{n} is WITHIN the range [{lower}, {upper}]")
else:
    print(f"{n} is OUTSIDE the range [{lower}, {upper}]")

# ============================================================
# Sample Output:
#   Enter a number: 15
#   Enter lower bound: 10
#   Enter upper bound: 20
#   15.0 is WITHIN the range [10.0, 20.0]
# ============================================================

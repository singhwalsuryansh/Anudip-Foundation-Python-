# ============================================================
# Problem 50: Calculate Power Using Recursive Function
# ============================================================
# Recursive definition:
#   power(base, 0)   = 1
#   power(base, exp) = base * power(base, exp - 1)
#
# Example:
#   Input:  base=3, exp=4
#   Output: 3^4 = 81
# ============================================================

def power_recursive(base, exp):
    """Recursively compute base^exp (exp must be non-negative integer)."""
    if exp == 0:
        return 1                           # base case
    return base * power_recursive(base, exp - 1)  # recursive call

# ---- Read input ----
base = float(input("Enter base: "))
exp  = int(input("Enter exponent (non-negative integer): "))

if exp < 0:
    print("This implementation handles non-negative exponents only.")
else:
    result = power_recursive(base, exp)
    print(f"{base}^{exp} = {result}")

# ============================================================
# Sample Output:
#   Enter base: 3
#   Enter exponent (non-negative integer): 4
#   3.0^4 = 81.0
# ============================================================

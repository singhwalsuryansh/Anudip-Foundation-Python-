# ============================================================
# Problem 39: Calculate Power Without Using Exponent Operator (**)
# ============================================================
# Approach: Multiply base by itself exp times using a for loop.
#           Handle negative exponents by taking reciprocal.
#
# Example:
#   Input:  base=2, exp=8
#   Output: 2^8 = 256
# ============================================================

def power(base, exp):
    if exp == 0:
        return 1
    negative = exp < 0
    exp = abs(exp)
    result = 1
    for _ in range(exp):
        result *= base        # multiply base repeatedly
    if negative:
        return 1 / result     # handle negative exponent
    return result

# ---- Read input ----
base = float(input("Enter base: "))
exp  = int(input("Enter exponent (integer): "))

result = power(base, exp)
print(f"{base}^{exp} = {result}")

# ============================================================
# Sample Output:
#   Enter base: 2
#   Enter exponent (integer): 8
#   2.0^8 = 256
# ============================================================

# ============================================================
# Problem 9: Find the Sum of Digits of a Number
# ============================================================
# Approach: Extract each digit using modulo (%), sum them up.
#
# Example:
#   Input:  1234
#   Output: Sum of digits = 10
# ============================================================

def sum_of_digits(n):
    n = abs(n)          # handle negative numbers
    total = 0
    while n > 0:
        total += n % 10  # extract last digit
        n //= 10         # remove last digit
    return total

# ---- Read input ----
n = int(input("Enter a number: "))

print(f"Sum of digits of {n} = {sum_of_digits(n)}")

# ============================================================
# Sample Output:
#   Enter a number: 1234
#   Sum of digits of 1234 = 10
# ============================================================

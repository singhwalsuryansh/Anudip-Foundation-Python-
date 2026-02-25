# ============================================================
# Problem 45: Find Sum of Digits Using Function
# ============================================================
# Approach: Extract each digit with modulo, accumulate sum.
#
# Example:
#   Input:  9876
#   Output: Sum of digits = 30
# ============================================================

def sum_of_digits(n):
    """Return the sum of digits of integer n."""
    n = abs(n)                    # handle negative numbers
    total = 0
    while n > 0:
        total += n % 10           # extract last digit
        n //= 10                  # remove last digit
    return total

# ---- Read input ----
n = int(input("Enter an integer: "))

print(f"Sum of digits of {n} = {sum_of_digits(n)}")

# ============================================================
# Sample Output:
#   Enter an integer: 9876
#   Sum of digits of 9876 = 30
# ============================================================

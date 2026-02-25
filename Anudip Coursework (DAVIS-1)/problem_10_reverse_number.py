# ============================================================
# Problem 10: Reverse a Given Number
# ============================================================
# Approach: Extract digits one by one using modulo and build
#           the reversed number.
#
# Example:
#   Input:  12345
#   Output: Reversed: 54321
# ============================================================

def reverse_number(n):
    negative = n < 0
    n = abs(n)
    reversed_n = 0
    while n > 0:
        digit = n % 10          # extract last digit
        reversed_n = reversed_n * 10 + digit  # append digit
        n //= 10                # remove last digit
    return -reversed_n if negative else reversed_n

# ---- Read input ----
n = int(input("Enter a number: "))

print(f"Original: {n}")
print(f"Reversed: {reverse_number(n)}")

# ============================================================
# Sample Output:
#   Enter a number: 12345
#   Original: 12345
#   Reversed: 54321
# ============================================================

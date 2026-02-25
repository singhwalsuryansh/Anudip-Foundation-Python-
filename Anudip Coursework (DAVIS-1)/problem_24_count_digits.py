# ============================================================
# Problem 24: Count Digits in a Number
# ============================================================
# Approach: Divide number by 10 repeatedly until it becomes 0,
#           counting each step.
# Special Case: n = 0 has exactly 1 digit.
#
# Example:
#   Input:  98765
#   Output: Number of digits = 5
# ============================================================

def count_digits(n):
    n = abs(n)       # handle negatives
    if n == 0:
        return 1     # 0 has one digit
    count = 0
    while n > 0:
        count += 1   # count this digit
        n //= 10     # remove last digit
    return count

# ---- Read input ----
n = int(input("Enter a number: "))

print(f"Number of digits in {n} = {count_digits(n)}")

# ============================================================
# Sample Output:
#   Enter a number: 98765
#   Number of digits in 98765 = 5
# ============================================================

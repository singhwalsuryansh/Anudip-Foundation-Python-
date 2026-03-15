# ============================================================
# Problem 25: Find Sum of Even Numbers Up to N
# ============================================================
# Approach: Iterate from 2 to N in steps of 2, accumulate sum.
#
# Example:
#   Input:  10
#   Output: Sum of even numbers up to 10 = 30  (2+4+6+8+10)
# ============================================================

def sum_of_evens(n):
    total = 0
    i = 2                  # start from the first even number
    while i <= n:
        total += i
        i += 2             # jump to next even number
    return total

# ---- Read input ----
n = int(input("Enter N: "))

print(f"Sum of even numbers up to {n} = {sum_of_evens(n)}")

# ============================================================
# Sample Output:
#   Enter N: 10
#   Sum of even numbers up to 10 = 30
# ============================================================

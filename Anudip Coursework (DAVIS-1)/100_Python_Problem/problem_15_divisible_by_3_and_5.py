# ============================================================
# Problem 15: Check Whether a Number is Divisible by Both 3 and 5
# ============================================================
# Approach: Check if n % 3 == 0 AND n % 5 == 0
#           Equivalently: n % 15 == 0
#
# Example:
#   Input:  15  → Divisible by both 3 and 5
#   Input:   9  → Divisible by 3 only
#   Input:  10  → Divisible by 5 only
#   Input:   7  → Not divisible by either
# ============================================================

def check_divisibility(n):
    div3 = n % 3 == 0
    div5 = n % 5 == 0

    if div3 and div5:
        return "Divisible by both 3 and 5"
    elif div3:
        return "Divisible by 3 only"
    elif div5:
        return "Divisible by 5 only"
    else:
        return "Not divisible by 3 or 5"

# ---- Read input ----
n = int(input("Enter a number: "))

print(check_divisibility(n))

# ============================================================
# Sample Output:
#   Enter a number: 15
#   Divisible by both 3 and 5
# ============================================================

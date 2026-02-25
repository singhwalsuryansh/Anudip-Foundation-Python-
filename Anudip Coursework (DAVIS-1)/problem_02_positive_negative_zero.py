# ============================================================
# Problem 2: Check Whether a Number is Positive, Negative, or Zero
# ============================================================
# Approach: Use if-elif-else to classify the number.
#
# Example:
#   Input:  -7
#   Output: Negative
# ============================================================

def check_sign(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# ---- Read input ----
n = float(input("Enter a number: "))

result = check_sign(n)
print(f"{n} is {result}")

# ============================================================
# Sample Output:
#   Enter a number: -7
#   -7.0 is Negative
# ============================================================

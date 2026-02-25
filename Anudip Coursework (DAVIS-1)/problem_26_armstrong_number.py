# ============================================================
# Problem 26: Check Whether a Number is an Armstrong Number
# ============================================================
# Definition: An n-digit number is Armstrong if the sum of its
#             digits each raised to the power n equals the number.
# Example:    153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 ✓
#             9474 = 9^4 + 4^4 + 7^4 + 4^4 = 9474 ✓
# ============================================================

def is_armstrong(n):
    digits = str(abs(n))       # convert to string to count digits
    power = len(digits)        # number of digits determines the power
    total = sum(int(d) ** power for d in digits)
    return total == abs(n)

# ---- Read input ----
n = int(input("Enter a number: "))

if is_armstrong(n):
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is NOT an Armstrong number")

# ============================================================
# Sample Output:
#   Enter a number: 153
#   153 is an Armstrong number
# ============================================================

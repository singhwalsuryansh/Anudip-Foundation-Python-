# ============================================================
# Problem 11: Check Whether a Given Year is a Leap Year
# ============================================================
# Rules:
#   1. Divisible by 4      → potential leap year
#   2. Divisible by 100    → NOT a leap year (century rule)
#   3. Divisible by 400    → IS a leap year (override rule)
#
# Example:
#   Input:  2000  → Leap Year
#   Input:  1900  → Not a Leap Year
#   Input:  2024  → Leap Year
# ============================================================

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# ---- Read input ----
year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")

# ============================================================
# Sample Output:
#   Enter a year: 2024
#   2024 is a Leap Year
# ============================================================

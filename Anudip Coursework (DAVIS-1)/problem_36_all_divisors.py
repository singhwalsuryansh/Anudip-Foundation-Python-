# ============================================================
# Problem 36: Print All Divisors of a Number
# ============================================================
# Approach: Loop from 1 to √n; if i divides n, both i and n//i
#           are divisors.
#
# Example:
#   Input:  36
#   Output: Divisors: 1 2 3 4 6 9 12 18 36
# ============================================================

def find_divisors(n):
    divisors = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.add(i)        # i is a divisor
            divisors.add(n // i)   # so is n/i
        i += 1
    return sorted(divisors)

# ---- Read input ----
n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    divs = find_divisors(n)
    print(f"Divisors of {n}: {' '.join(map(str, divs))}")
    print(f"Total divisors: {len(divs)}")

# ============================================================
# Sample Output:
#   Enter a positive integer: 36
#   Divisors of 36: 1 2 3 4 6 9 12 18 36
#   Total divisors: 9
# ============================================================

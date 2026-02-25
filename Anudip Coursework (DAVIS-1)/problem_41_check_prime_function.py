# ============================================================
# Problem 41: Check Prime Number Using Function
# ============================================================
# A prime number has exactly 2 factors: 1 and itself.
# Optimization: Check divisibility only up to √n.
#
# Example:
#   Input:  29  → 29 is a Prime number
#   Input:  15  → 15 is NOT a Prime number
# ============================================================

def is_prime(n):
    if n < 2:
        return False                 # numbers less than 2 are not prime
    if n == 2:
        return True                  # 2 is the only even prime
    if n % 2 == 0:
        return False                 # eliminate all other evens

    # Check odd divisors from 3 up to √n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# ---- Read input ----
n = int(input("Enter a number: "))

if is_prime(n):
    print(f"{n} is a Prime number")
else:
    print(f"{n} is NOT a Prime number")

# ============================================================
# Sample Output:
#   Enter a number: 29
#   29 is a Prime number
# ============================================================

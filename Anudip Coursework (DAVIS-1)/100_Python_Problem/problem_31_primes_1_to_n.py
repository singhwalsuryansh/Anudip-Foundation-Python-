# ============================================================
# Problem 31: Print All Prime Numbers Between 1 and N
# ============================================================
# A prime number is > 1 and has no divisors other than 1 and itself.
# Optimization: Only check divisors up to sqrt(n).
#
# Example:
#   Input:  20
#   Output: 2 3 5 7 11 13 17 19
# ============================================================

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False         # eliminate even numbers
    i = 3
    while i * i <= n:       # only check up to √n
        if n % i == 0:
            return False
        i += 2               # only check odd divisors
    return True

# ---- Read input ----
n = int(input("Enter N: "))

primes = [str(i) for i in range(2, n + 1) if is_prime(i)]

if primes:
    print(f"Prime numbers from 1 to {n}:")
    print(" ".join(primes))
else:
    print(f"No prime numbers found up to {n}.")

# ============================================================
# Sample Output:
#   Enter N: 20
#   Prime numbers from 1 to 20:
#   2 3 5 7 11 13 17 19
# ============================================================

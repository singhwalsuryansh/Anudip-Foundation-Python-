# ============================================================
# Problem 29: Find GCD Using While Loop (Euclidean Algorithm)
# ============================================================
# Algorithm: GCD(a, b) = GCD(b, a % b) until b == 0
#            The last non-zero remainder is the GCD.
#
# Example:
#   Input:  48, 18
#   Output: GCD = 6
# ============================================================

def gcd_while(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b   # Euclidean step: replace a with b, b with a%b
    return a

# ---- Read input ----
a = int(input("Enter first number:  "))
b = int(input("Enter second number: "))

print(f"\nGCD of {a} and {b} = {gcd_while(a, b)}")

# ============================================================
# Sample Output:
#   Enter first number:  48
#   Enter second number: 18
#   GCD of 48 and 18 = 6
# ============================================================

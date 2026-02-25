# ============================================================
# Problem 34: Find Sum of First N Natural Numbers
# ============================================================
# Method 1 (Loop):    sum = 1 + 2 + 3 + ... + N
# Method 2 (Formula): sum = N * (N + 1) / 2
#
# Example:
#   Input:  10
#   Output: Sum = 55
# ============================================================

def sum_natural_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_natural_formula(n):
    # Gauss formula — O(1) solution
    return n * (n + 1) // 2

# ---- Read input ----
n = int(input("Enter N: "))

if n < 0:
    print("Please enter a positive integer.")
else:
    print(f"Sum of first {n} natural numbers (loop)    = {sum_natural_loop(n)}")
    print(f"Sum of first {n} natural numbers (formula) = {sum_natural_formula(n)}")

# ============================================================
# Sample Output:
#   Enter N: 10
#   Sum of first 10 natural numbers (loop)    = 55
#   Sum of first 10 natural numbers (formula) = 55
# ============================================================

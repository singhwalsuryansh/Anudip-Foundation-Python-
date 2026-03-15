# ============================================================
# Problem 37: Generate Fibonacci Series Using For Loop
# ============================================================
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#
# Example:
#   Input:  8 terms
#   Output: 0 1 1 2 3 5 8 13
# ============================================================

def fibonacci_for(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b   # update: new a = b, new b = a+b
    return series

# ---- Read input ----
n = int(input("How many Fibonacci terms? "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci_for(n)
    print("Fibonacci Series:", " ".join(map(str, result)))

# ============================================================
# Sample Output:
#   How many Fibonacci terms? 8
#   Fibonacci Series: 0 1 1 2 3 5 8 13
# ============================================================

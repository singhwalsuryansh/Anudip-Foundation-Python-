# ============================================================
# Problem 27: Generate Fibonacci Series Using While Loop
# ============================================================
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Each term = sum of the two preceding terms.
#
# Example:
#   Input:  10 terms
#   Output: 0 1 1 2 3 5 8 13 21 34
# ============================================================

def fibonacci_while(n):
    series = []
    a, b = 0, 1
    count = 0
    while count < n:
        series.append(a)
        a, b = b, a + b   # shift: new b = a+b, new a = old b
        count += 1
    return series

# ---- Read input ----
n = int(input("How many Fibonacci terms? "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci_while(n)
    print("Fibonacci Series:", " ".join(map(str, result)))

# ============================================================
# Sample Output:
#   How many Fibonacci terms? 10
#   Fibonacci Series: 0 1 1 2 3 5 8 13 21 34
# ============================================================

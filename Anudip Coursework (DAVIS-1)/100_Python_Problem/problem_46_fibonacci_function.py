# ============================================================
# Problem 46: Generate Fibonacci Series Using Function
# ============================================================
# Returns a list of the first n Fibonacci numbers.
# F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)
#
# Example:
#   Input:  12
#   Output: 0 1 1 2 3 5 8 13 21 34 55 89
# ============================================================

def generate_fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    series = [0, 1]
    for _ in range(2, n):
        series.append(series[-1] + series[-2])  # next = last + second-last
    return series

# ---- Read input ----
n = int(input("How many Fibonacci terms? "))

result = generate_fibonacci(n)
if result:
    print("Fibonacci Series:", " ".join(map(str, result)))
else:
    print("Please enter a positive integer.")

# ============================================================
# Sample Output:
#   How many Fibonacci terms? 12
#   Fibonacci Series: 0 1 1 2 3 5 8 13 21 34 55 89
# ============================================================

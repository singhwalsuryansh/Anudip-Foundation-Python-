# ============================================================
# Problem 21: Print Numbers from 1 to N Using While Loop
# ============================================================
# Approach: Initialize counter at 1, increment until N.
#
# Example:
#   Input:  5
#   Output: 1 2 3 4 5
# ============================================================

# ---- Read input ----
n = int(input("Enter N: "))

# Use while loop to print 1 to N
i = 1
result = []
while i <= n:
    result.append(str(i))
    i += 1  # increment counter

print(" ".join(result))

# ============================================================
# Sample Output:
#   Enter N: 5
#   1 2 3 4 5
# ============================================================

# ============================================================
# Problem 33: Print Star Pattern Using For Loop
# ============================================================
# Right-angled triangle pattern:
#   Row 1: *
#   Row 2: * *
#   Row 3: * * *
#   ...
#   Row N: * * * ... *
#
# Example:
#   Input:  5
#   Output:
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
# ============================================================

# ---- Read input ----
n = int(input("Enter number of rows: "))

# Outer loop controls the number of rows
for i in range(1, n + 1):
    # Inner loop prints stars for each row
    print(" ".join("*" for _ in range(i)))

# ============================================================
# Sample Output:
#   Enter number of rows: 5
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
# ============================================================

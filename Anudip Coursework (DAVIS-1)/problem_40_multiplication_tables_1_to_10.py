# ============================================================
# Problem 40: Print Multiplication Tables from 1 to 10
# ============================================================
# Nested for loops: outer loop for table number (1-10),
# inner loop for multiplier (1-10).
#
# Example Output (partial):
#   --- Table of 1 ---
#   1 x 1 = 1
#   ...
#   --- Table of 2 ---
#   2 x 1 = 2
# ============================================================

for i in range(1, 11):              # tables from 1 to 10
    print(f"\n--- Table of {i} ---")
    for j in range(1, 11):          # multipliers from 1 to 10
        print(f"{i} x {j:2d} = {i * j:3d}")

# ============================================================
# Sample Output:
#   --- Table of 1 ---
#   1 x  1 =   1
#   1 x  2 =   2
#   ...
#   --- Table of 10 ---
#   10 x  1 =  10
#   10 x 10 = 100
# ============================================================

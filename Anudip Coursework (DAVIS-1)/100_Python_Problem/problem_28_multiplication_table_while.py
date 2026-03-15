# ============================================================
# Problem 28: Print Multiplication Table Using While Loop
# ============================================================
# Example:
#   Input:  7
#   Output:
#     7 x  1 =  7
#     7 x  2 = 14
#     ...
#     7 x 10 = 70
# ============================================================

# ---- Read input ----
n = int(input("Enter a number for its multiplication table: "))

print(f"\nMultiplication Table for {n}:")
print("-" * 20)

i = 1
while i <= 10:
    print(f"{n} x {i:2d} = {n * i:3d}")  # formatted output
    i += 1

# ============================================================
# Sample Output:
#   Enter a number for its multiplication table: 7
#   Multiplication Table for 7:
#   --------------------
#   7 x  1 =   7
#   7 x  2 =  14
#   7 x  3 =  21
#   ...
#   7 x 10 =  70
# ============================================================

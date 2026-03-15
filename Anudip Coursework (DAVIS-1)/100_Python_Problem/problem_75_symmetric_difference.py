# ============================================================
# Problem 75: Find Symmetric Difference of Two Sets
# ============================================================

raw1 = input("Enter first set (space-separated):  ")
raw2 = input("Enter second set (space-separated): ")
s1 = set(map(int, raw1.split()))
s2 = set(map(int, raw2.split()))
sym_diff = s1 ^ s2         # elements in s1 or s2 but NOT both
print(f"Set 1                : {sorted(s1)}")
print(f"Set 2                : {sorted(s2)}")
print(f"Symmetric Difference : {sorted(sym_diff)}")
# Sample Output:
#   Symmetric Difference : [1, 2, 5, 6]


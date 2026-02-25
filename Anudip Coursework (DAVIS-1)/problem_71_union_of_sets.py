# ============================================================
# Problem 71: Perform Union of Two Sets
# ============================================================

raw1 = input("Enter first set (space-separated):  ")
raw2 = input("Enter second set (space-separated): ")
s1 = set(map(int, raw1.split()))
s2 = set(map(int, raw2.split()))
union = s1 | s2           # union operator
print(f"Set 1 : {sorted(s1)}")
print(f"Set 2 : {sorted(s2)}")
print(f"Union : {sorted(union)}")
# Sample Output:
#   Union : [1, 2, 3, 4, 5, 6]


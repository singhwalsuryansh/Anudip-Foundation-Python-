# ============================================================
# Problem 72: Perform Intersection of Two Sets
# ============================================================

raw1 = input("Enter first set (space-separated):  ")
raw2 = input("Enter second set (space-separated): ")
s1 = set(map(int, raw1.split()))
s2 = set(map(int, raw2.split()))
inter = s1 & s2            # intersection operator
print(f"Set 1        : {sorted(s1)}")
print(f"Set 2        : {sorted(s2)}")
print(f"Intersection : {sorted(inter)}")
# Sample Output:
#   Intersection : [3, 4]


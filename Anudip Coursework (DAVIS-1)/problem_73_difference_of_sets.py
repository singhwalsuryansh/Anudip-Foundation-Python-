# ============================================================
# Problem 73: Perform Difference of Two Sets
# ============================================================

raw1 = input("Enter first set (space-separated):  ")
raw2 = input("Enter second set (space-separated): ")
s1 = set(map(int, raw1.split()))
s2 = set(map(int, raw2.split()))
diff = s1 - s2             # elements in s1 but not in s2
print(f"Set 1      : {sorted(s1)}")
print(f"Set 2      : {sorted(s2)}")
print(f"S1 - S2    : {sorted(diff)}")
print(f"S2 - S1    : {sorted(s2 - s1)}")
# Sample Output:
#   S1 - S2 : [1, 2]


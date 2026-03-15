# ============================================================
# Problem 74: Check Whether One Set is Subset of Another
# ============================================================

raw1 = input("Enter potential subset (space-separated): ")
raw2 = input("Enter main set (space-separated):        ")
s1 = set(map(int, raw1.split()))
s2 = set(map(int, raw2.split()))
if s1.issubset(s2):
    print(f"{sorted(s1)} IS a subset of {sorted(s2)}")
else:
    print(f"{sorted(s1)} is NOT a subset of {sorted(s2)}")
# Sample Output:
#   {1, 2} IS a subset of {1, 2, 3, 4}


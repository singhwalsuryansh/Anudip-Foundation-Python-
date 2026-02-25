# ============================================================
# Problem 60: Find Common Elements Between Two Lists
# ============================================================

def common_elements(lst1, lst2):
    return [x for x in lst1 if x in lst2]

raw1 = input("Enter first list (space-separated):  ")
raw2 = input("Enter second list (space-separated): ")
lst1 = list(map(int, raw1.split()))
lst2 = list(map(int, raw2.split()))
common = common_elements(lst1, lst2)
print(f"Common elements: {common}")
# Sample Output:
#   Common elements: [3, 5]


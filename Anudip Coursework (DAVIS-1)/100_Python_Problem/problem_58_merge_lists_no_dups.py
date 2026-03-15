# ============================================================
# Problem 58: Merge Two Lists and Remove Duplicates
# ============================================================

def merge_unique(lst1, lst2):
    merged = lst1 + lst2
    seen = []
    for item in merged:
        if item not in seen:
            seen.append(item)
    return seen

raw1 = input("Enter first list (space-separated): ")
raw2 = input("Enter second list (space-separated): ")
lst1 = list(map(int, raw1.split()))
lst2 = list(map(int, raw2.split()))
print(f"Merged (no duplicates): {merge_unique(lst1, lst2)}")
# Sample Output:
#   Merged (no duplicates): [1, 2, 3, 4, 5, 6]


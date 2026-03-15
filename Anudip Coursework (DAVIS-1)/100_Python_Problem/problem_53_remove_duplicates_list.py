# ============================================================
# Problem 53: Remove Duplicate Elements from List
# ============================================================

def remove_duplicates(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

raw = input("Enter numbers separated by spaces: ")
lst = list(map(int, raw.split()))
print(f"Original : {lst}")
print(f"No Dups  : {remove_duplicates(lst)}")
# Sample Output:
#   Enter numbers: 1 2 3 2 1 4
#   No Dups  : [1, 2, 3, 4]


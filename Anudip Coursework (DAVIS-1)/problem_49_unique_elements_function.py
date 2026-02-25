# ============================================================
# Problem 49: Return Unique Elements from a List Using Function
# ============================================================
# Approach: Iterate through the list and track seen elements;
#           preserve original order (unlike using set()).
#
# Example:
#   Input:  [4, 2, 7, 2, 4, 9, 1, 7]
#   Output: Unique elements: [4, 2, 7, 9, 1]
# ============================================================

def get_unique(lst):
    """Return list of unique elements preserving insertion order."""
    seen = []
    for item in lst:
        if item not in seen:    # if not already recorded
            seen.append(item)
    return seen

# ---- Read input ----
raw = input("Enter numbers separated by spaces: ")
lst = list(map(int, raw.split()))

unique = get_unique(lst)
print(f"Original list   : {lst}")
print(f"Unique elements : {unique}")

# ============================================================
# Sample Output:
#   Enter numbers separated by spaces: 4 2 7 2 4 9 1 7
#   Original list   : [4, 2, 7, 2, 4, 9, 1, 7]
#   Unique elements : [4, 2, 7, 9, 1]
# ============================================================

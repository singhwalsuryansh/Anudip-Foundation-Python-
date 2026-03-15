# ============================================================
# Problem 70: Check Whether Tuple Elements are Unique
# ============================================================

def are_unique(t):
    seen = set()
    for item in t:
        if item in seen:
            return False
        seen.add(item)
    return True

raw = input("Enter numbers separated by spaces: ")
t = tuple(map(int, raw.split()))
if are_unique(t):
    print(f"All elements in {t} are UNIQUE")
else:
    print(f"Elements in {t} are NOT all unique")
# Sample Output:
#   All elements in (1, 2, 3, 4) are UNIQUE


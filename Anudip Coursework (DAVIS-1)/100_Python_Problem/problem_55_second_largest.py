# ============================================================
# Problem 55: Find Second Largest Number in List
# ============================================================

def second_largest(lst):
    unique = list(set(lst))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

raw = input("Enter numbers separated by spaces: ")
lst = list(map(int, raw.split()))
result = second_largest(lst)
if result is None:
    print("List must have at least 2 distinct elements.")
else:
    print(f"Second Largest: {result}")
# Sample Output:
#   Enter numbers: 3 7 1 9 4
#   Second Largest: 7


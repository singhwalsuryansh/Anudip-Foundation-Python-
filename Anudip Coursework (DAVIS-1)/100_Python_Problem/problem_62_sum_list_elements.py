# ============================================================
# Problem 62: Find Sum of List Elements
# ============================================================

def list_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

raw = input("Enter numbers separated by spaces: ")
lst = list(map(float, raw.split()))
print(f"List : {lst}")
print(f"Sum  : {list_sum(lst)}")
# Sample Output:
#   Sum : 25.0


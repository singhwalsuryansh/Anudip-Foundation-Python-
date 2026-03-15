# ============================================================
# Problem 63: Find Average of List Elements
# ============================================================

def list_average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

raw = input("Enter numbers separated by spaces: ")
lst = list(map(float, raw.split()))
print(f"List    : {lst}")
print(f"Average : {list_average(lst):.2f}")
# Sample Output:
#   Average : 5.00


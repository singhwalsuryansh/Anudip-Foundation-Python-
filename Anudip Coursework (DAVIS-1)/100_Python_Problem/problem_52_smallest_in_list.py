# ============================================================
# Problem 52: Find Smallest Element in a List
# ============================================================

def find_smallest(lst):
    smallest = lst[0]
    for num in lst[1:]:
        if num < smallest:
            smallest = num
    return smallest

raw = input("Enter numbers separated by spaces: ")
lst = list(map(float, raw.split()))
print(f"List     : {lst}")
print(f"Smallest : {find_smallest(lst)}")
# Sample Output:
#   Enter numbers separated by spaces: 3 7 1 9 4
#   Smallest : 1.0


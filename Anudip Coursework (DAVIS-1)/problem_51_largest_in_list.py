# ============================================================
# Problem 51: Find Largest Element in a List
# ============================================================

def find_largest(lst):
    largest = lst[0]              # assume first element is largest
    for num in lst[1:]:
        if num > largest:         # update if a bigger one is found
            largest = num
    return largest

# ---- Read input ----
raw = input("Enter numbers separated by spaces: ")
lst = list(map(float, raw.split()))
print(f"List    : {lst}")
print(f"Largest : {find_largest(lst)}")
# Sample Output:
#   Enter numbers separated by spaces: 3 7 1 9 4
#   List    : [3.0, 7.0, 1.0, 9.0, 4.0]
#   Largest : 9.0


# ============================================================
# Problem 54: Sort a List Without Using sort() Method (Bubble Sort)
# ============================================================

def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):                  # passes
        for j in range(n - 1 - i):          # comparisons per pass
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # swap
    return lst

raw = input("Enter numbers separated by spaces: ")
lst = list(map(int, raw.split()))
print(f"Unsorted : {lst}")
print(f"Sorted   : {bubble_sort(lst[:])}")
# Sample Output:
#   Unsorted : [5, 2, 8, 1, 9]
#   Sorted   : [1, 2, 5, 8, 9]


# ============================================================
# Problem 57: Reverse a List Without reverse() Method
# ============================================================

def reverse_list(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]  # swap
        left += 1
        right -= 1
    return lst

raw = input("Enter numbers separated by spaces: ")
lst = list(map(int, raw.split()))
print(f"Original : {lst}")
print(f"Reversed : {reverse_list(lst[:])}")
# Sample Output:
#   Original : [1, 2, 3, 4, 5]
#   Reversed : [5, 4, 3, 2, 1]


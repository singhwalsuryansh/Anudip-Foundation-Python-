# ============================================================
# Problem 61: Rotate a List by K Positions
# ============================================================

def rotate_list(lst, k):
    n = len(lst)
    k = k % n              # handle k > n
    return lst[k:] + lst[:k]

raw = input("Enter numbers separated by spaces: ")
lst = list(map(int, raw.split()))
k   = int(input("Enter K (positions to rotate left): "))
print(f"Original : {lst}")
print(f"Rotated  : {rotate_list(lst, k)}")
# Sample Output:
#   Original : [1, 2, 3, 4, 5]
#   Rotated  : [3, 4, 5, 1, 2]  (k=2)


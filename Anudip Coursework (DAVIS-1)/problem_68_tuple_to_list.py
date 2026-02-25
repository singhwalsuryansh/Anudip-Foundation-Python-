# ============================================================
# Problem 68: Convert Tuple to List
# ============================================================

raw = input("Enter numbers separated by spaces: ")
t = tuple(map(int, raw.split()))
lst = list(t)                  # direct conversion
print(f"Tuple : {t}  (type: {type(t).__name__})")
print(f"List  : {lst}  (type: {type(lst).__name__})")
# Sample Output:
#   Tuple : (1, 2, 3)  (type: tuple)
#   List  : [1, 2, 3]  (type: list)


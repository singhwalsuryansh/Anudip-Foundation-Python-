# ============================================================
# Problem 67: Find Minimum Value in a Tuple
# ============================================================

def min_in_tuple(t):
    minimum = t[0]
    for val in t[1:]:
        if val < minimum:
            minimum = val
    return minimum

raw = input("Enter numbers separated by spaces: ")
t = tuple(map(int, raw.split()))
print(f"Tuple   : {t}")
print(f"Minimum : {min_in_tuple(t)}")
# Sample Output:
#   Tuple   : (3, 7, 1, 9, 4)
#   Minimum : 1


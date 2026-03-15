# ============================================================
# Problem 66: Find Maximum Value in a Tuple
# ============================================================

def max_in_tuple(t):
    maximum = t[0]
    for val in t[1:]:
        if val > maximum:
            maximum = val
    return maximum

raw = input("Enter numbers separated by spaces: ")
t = tuple(map(int, raw.split()))
print(f"Tuple   : {t}")
print(f"Maximum : {max_in_tuple(t)}")
# Sample Output:
#   Tuple   : (3, 7, 1, 9, 4)
#   Maximum : 9


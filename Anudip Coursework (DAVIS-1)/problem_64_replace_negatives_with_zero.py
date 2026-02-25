# ============================================================
# Problem 64: Replace Negative Numbers with Zero
# ============================================================

def replace_negatives(lst):
    return [0 if x < 0 else x for x in lst]

raw = input("Enter numbers separated by spaces: ")
lst = list(map(int, raw.split()))
print(f"Original : {lst}")
print(f"Modified : {replace_negatives(lst)}")
# Sample Output:
#   Original : [3, -1, 4, -2, 5]
#   Modified : [3, 0, 4, 0, 5]


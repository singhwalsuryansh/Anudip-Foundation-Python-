# ============================================================
# Problem 65: Check Whether List is Palindrome
# ============================================================

def is_palindrome_list(lst):
    return lst == lst[::-1]

raw = input("Enter numbers separated by spaces: ")
lst = list(map(int, raw.split()))
if is_palindrome_list(lst):
    print(f"{lst} is a Palindrome list")
else:
    print(f"{lst} is NOT a Palindrome list")
# Sample Output:
#   [1, 2, 3, 2, 1] is a Palindrome list


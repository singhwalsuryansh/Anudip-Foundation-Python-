# ============================================================
# Problem 87: Check Whether String is Palindrome
# ============================================================

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left  += 1
        right -= 1
    return True

s = input("Enter a string: ")
if is_palindrome(s):
    print(f'"{s}" is a Palindrome')
else:
    print(f'"{s}" is NOT a Palindrome')
# Sample Output:
#   "madam" is a Palindrome


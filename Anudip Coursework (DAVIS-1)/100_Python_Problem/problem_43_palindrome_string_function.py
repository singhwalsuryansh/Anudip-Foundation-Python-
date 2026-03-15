# ============================================================
# Problem 43: Check Palindrome String Using Function
# ============================================================
# A palindrome reads the same forwards and backwards.
# Examples: "racecar", "madam", "level"
#
# Example:
#   Input:  "racecar"  → Palindrome
#   Input:  "hello"    → Not a Palindrome
# ============================================================

def is_palindrome(s):
    """Check if string s is a palindrome (case-insensitive)."""
    s = s.lower().replace(" ", "")   # normalize: lowercase and remove spaces
    return s == s[::-1]              # compare with its reverse

# ---- Read input ----
s = input("Enter a string: ")

if is_palindrome(s):
    print(f'"{s}" is a Palindrome')
else:
    print(f'"{s}" is NOT a Palindrome')

# ============================================================
# Sample Output:
#   Enter a string: racecar
#   "racecar" is a Palindrome
# ============================================================

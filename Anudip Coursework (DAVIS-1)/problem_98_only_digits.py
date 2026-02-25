# ============================================================
# Problem 98: Check Whether String Contains Only Digits
# ============================================================

def only_digits(s):
    if not s:
        return False
    for ch in s:
        if not ch.isdigit():
            return False
    return True

s = input("Enter a string: ")
if only_digits(s):
    print(f"'{s}' contains ONLY digits")
else:
    print(f"'{s}' does NOT contain only digits")
# Sample Output:
#   '12345' contains ONLY digits


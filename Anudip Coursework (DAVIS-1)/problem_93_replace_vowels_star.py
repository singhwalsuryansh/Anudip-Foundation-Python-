# ============================================================
# Problem 93: Replace All Vowels with *
# ============================================================

def replace_vowels(s):
    result = ""
    for ch in s:
        if ch in "aeiouAEIOU":
            result += "*"
        else:
            result += ch
    return result

s = input("Enter a string: ")
print(f"Original : {s}")
print(f"Modified : {replace_vowels(s)}")
# Sample Output:
#   Original : Hello World
#   Modified : H*ll* W*rld


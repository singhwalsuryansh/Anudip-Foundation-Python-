# ============================================================
# Problem 94: Check Whether Two Strings are Anagrams
# ============================================================

def are_anagrams(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    if len(s1) != len(s2):
        return False
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s2:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1
    return True

s1 = input("Enter first string:  ")
s2 = input("Enter second string: ")
if are_anagrams(s1, s2):
    print(f'"{s1}" and "{s2}" ARE anagrams')
else:
    print(f'"{s1}" and "{s2}" are NOT anagrams')
# Sample Output:
#   "listen" and "silent" ARE anagrams


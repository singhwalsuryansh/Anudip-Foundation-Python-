# ============================================================
# Problem 96: Find First Non-Repeating Character in String
# ============================================================

def first_non_repeating(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

s = input("Enter a string: ")
result = first_non_repeating(s)
if result:
    print(f"First non-repeating character: '{result}'")
else:
    print("All characters repeat.")
# Sample Output:
#   Enter a string: swiss
#   First non-repeating character: 'w'


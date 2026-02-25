# ============================================================
# Problem 89: Find Frequency of Each Character in String
# ============================================================

s = input("Enter a string: ")
freq = {}
for ch in s:
    if ch != ' ':                        # skip spaces (optional)
        freq[ch] = freq.get(ch, 0) + 1
print(f"String: '{s}'")
for ch, cnt in sorted(freq.items()):
    print(f"  '{ch}' → {cnt}")
# Sample Output:
#   'h' → 1, 'e' → 1, 'l' → 3, 'o' → 2


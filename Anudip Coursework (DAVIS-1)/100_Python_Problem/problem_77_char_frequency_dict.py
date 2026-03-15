# ============================================================
# Problem 77: Count Character Frequency Using Dictionary
# ============================================================

s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1    # increment count

print(f"String: '{s}'")
print("Character frequencies:")
for ch, count in sorted(freq.items()):
    print(f"  '{ch}' : {count}")
# Sample Output:
#   'a' : 2, 'b' : 1, etc.


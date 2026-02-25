# ============================================================
# Problem 97: Count Uppercase and Lowercase Letters
# ============================================================

s = input("Enter a string: ")
upper_count = 0
lower_count = 0
for ch in s:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
print(f"String         : '{s}'")
print(f"Uppercase count: {upper_count}")
print(f"Lowercase count: {lower_count}")
# Sample Output:
#   Uppercase count: 3
#   Lowercase count: 8


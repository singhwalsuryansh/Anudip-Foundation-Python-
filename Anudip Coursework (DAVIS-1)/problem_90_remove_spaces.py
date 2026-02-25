# ============================================================
# Problem 90: Remove Spaces from String
# ============================================================

s = input("Enter a string: ")
no_spaces = ""
for ch in s:
    if ch != ' ':
        no_spaces += ch
print(f"Original : '{s}'")
print(f"No spaces: '{no_spaces}'")
# Sample Output:
#   Original : 'Hello World'
#   No spaces: 'HelloWorld'


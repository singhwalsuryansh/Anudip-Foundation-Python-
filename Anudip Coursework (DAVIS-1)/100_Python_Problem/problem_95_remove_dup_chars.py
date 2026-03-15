# ============================================================
# Problem 95: Remove Duplicate Characters from String
# ============================================================

def remove_dup_chars(s):
    seen = set()
    result = ""
    for ch in s:
        if ch not in seen:
            result += ch
            seen.add(ch)
    return result

s = input("Enter a string: ")
print(f"Original : {s}")
print(f"No dups  : {remove_dup_chars(s)}")
# Sample Output:
#   Original : programming
#   No dups  : progamin


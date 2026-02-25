# ============================================================
# Problem 86: Reverse a String Without Slicing
# ============================================================

def reverse_without_slice(s):
    reversed_s = ""
    for i in range(len(s) - 1, -1, -1):   # iterate backwards by index
        reversed_s += s[i]
    return reversed_s

s = input("Enter a string: ")
print(f"Original : {s}")
print(f"Reversed : {reverse_without_slice(s)}")
# Sample Output:
#   Original : Hello
#   Reversed : olleH


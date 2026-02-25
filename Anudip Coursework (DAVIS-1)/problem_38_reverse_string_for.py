# ============================================================
# Problem 38: Reverse a String Using For Loop
# ============================================================
# Approach: Iterate from the last index to the first,
#           building the reversed string character by character.
#
# Example:
#   Input:  "Python"
#   Output: "nohtyP"
# ============================================================

def reverse_string_for(s):
    reversed_s = ""
    for i in range(len(s) - 1, -1, -1):  # iterate backwards
        reversed_s += s[i]
    return reversed_s

# ---- Read input ----
s = input("Enter a string: ")

print(f"Original : {s}")
print(f"Reversed : {reverse_string_for(s)}")

# ============================================================
# Sample Output:
#   Enter a string: Python
#   Original : Python
#   Reversed : nohtyP
# ============================================================

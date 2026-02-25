# ============================================================
# Problem 35: Count Vowels in a String
# ============================================================
# Vowels: a, e, i, o, u (case-insensitive)
#
# Example:
#   Input:  "Hello World"
#   Output: Number of vowels = 3
# ============================================================

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:    # check if character is a vowel
            count += 1
    return count

# ---- Read input ----
s = input("Enter a string: ")

vowel_count = count_vowels(s)
print(f"String: '{s}'")
print(f"Number of vowels = {vowel_count}")

# ============================================================
# Sample Output:
#   Enter a string: Hello World
#   String: 'Hello World'
#   Number of vowels = 3
# ============================================================

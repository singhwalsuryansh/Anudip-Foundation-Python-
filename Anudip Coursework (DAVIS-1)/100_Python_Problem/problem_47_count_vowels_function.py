# ============================================================
# Problem 47: Count Vowels Using Function
# ============================================================
# Counts both uppercase and lowercase vowels.
#
# Example:
#   Input:  "Programming is Fun"
#   Output: Number of vowels = 5
# ============================================================

def count_vowels(s):
    """Count the number of vowel characters in string s."""
    vowels = set("aeiouAEIOU")
    count = 0
    for ch in s:
        if ch in vowels:    # check membership in set (O(1) average)
            count += 1
    return count

# ---- Read input ----
s = input("Enter a string: ")

vc = count_vowels(s)
print(f"String: '{s}'")
print(f"Number of vowels = {vc}")

# ============================================================
# Sample Output:
#   Enter a string: Programming is Fun
#   String: 'Programming is Fun'
#   Number of vowels = 5
# ============================================================

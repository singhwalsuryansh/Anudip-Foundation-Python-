# ============================================================
# Problem 13: Check Whether a Character is Vowel or Consonant
# ============================================================
# Vowels: a, e, i, o, u (both uppercase and lowercase)
#
# Example:
#   Input:  'e'  → Vowel
#   Input:  'k'  → Consonant
# ============================================================

def vowel_or_consonant(ch):
    ch = ch.lower()
    if not ch.isalpha():
        return "Not an alphabet"
    if ch in "aeiou":
        return "Vowel"
    else:
        return "Consonant"

# ---- Read input ----
ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter a single character.")
else:
    print(f"'{ch}' is a {vowel_or_consonant(ch)}")

# ============================================================
# Sample Output:
#   Enter a character: e
#   'e' is a Vowel
# ============================================================

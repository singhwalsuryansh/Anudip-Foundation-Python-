# ============================================================
# Problem 14: Check Whether a Character is Digit or Alphabet
# ============================================================
# Approach: Use str.isdigit() and str.isalpha() methods.
#
# Example:
#   Input:  '5'  → Digit
#   Input:  'A'  → Alphabet
#   Input:  '@'  → Special Character
# ============================================================

def classify_character(ch):
    if ch.isdigit():
        return "Digit"
    elif ch.isalpha():
        return "Alphabet"
    else:
        return "Special Character"

# ---- Read input ----
ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    print(f"'{ch}' is a {classify_character(ch)}")

# ============================================================
# Sample Output:
#   Enter a character: 5
#   '5' is a Digit
# ============================================================

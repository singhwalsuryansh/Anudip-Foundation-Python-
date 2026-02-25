# ============================================================
# Problem 92: Find Longest Word in a Sentence
# ============================================================

sentence = input("Enter a sentence: ")
words = sentence.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print(f"Sentence     : '{sentence}'")
print(f"Longest word : '{longest}' ({len(longest)} characters)")
# Sample Output:
#   Longest word : 'Programming' (11 characters)


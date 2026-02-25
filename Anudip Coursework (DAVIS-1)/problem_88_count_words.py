# ============================================================
# Problem 88: Count Number of Words in a Sentence
# ============================================================

sentence = input("Enter a sentence: ")
# split() splits on any whitespace and handles multiple spaces
words = sentence.split()
print(f"Sentence  : '{sentence}'")
print(f"Word count: {len(words)}")
# Sample Output:
#   Sentence  : 'Hello World from Python'
#   Word count: 4


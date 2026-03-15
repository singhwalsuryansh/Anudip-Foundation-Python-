# ============================================================
# Problem 91: Convert String to Title Case Manually
# ============================================================

def to_title_case(s):
    words = s.split()
    result = []
    for word in words:
        if word:
            titled = word[0].upper() + word[1:].lower()
            result.append(titled)
    return " ".join(result)

s = input("Enter a string: ")
print(f"Original   : {s}")
print(f"Title Case : {to_title_case(s)}")
# Sample Output:
#   Original   : hello world from python
#   Title Case : Hello World From Python


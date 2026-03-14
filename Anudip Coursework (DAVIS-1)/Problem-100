# ============================================================
# Problem 100: Compress a String Using Character Counts
# ============================================================

def compress_string(s):
    if not s:
        return ""
    result = ""
    i = 0
    while i < len(s):
        ch = s[i]
        count = 1
        while i + count < len(s) and s[i + count] == ch:
            count += 1
        if count > 1:
            result += ch + str(count)   # e.g., 'aaa' -> 'a3'
        else:
            result += ch                # single char stays as-is
        i += count
    return result if len(result) < len(s) else s  # return shorter

s = input("Enter a string to compress: ")
compressed = compress_string(s)
print(f"Original   : {s}  (len={len(s)})")
print(f"Compressed : {compressed}  (len={len(compressed)})")
# Sample Output:
#   Original   : aabcccdddd  (len=10)
#   Compressed : a2bc3d4  (len=7)


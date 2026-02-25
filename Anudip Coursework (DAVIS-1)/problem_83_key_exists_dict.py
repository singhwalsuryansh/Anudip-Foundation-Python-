# ============================================================
# Problem 83: Check Whether Key Exists in Dictionary
# ============================================================

n = int(input("Enter number of key-value pairs: "))
d = {}
for _ in range(n):
    k = input("  Key: ")
    v = input("  Value: ")
    d[k] = v
key = input("Enter key to search: ")
if key in d:                    # 'in' operator checks keys
    print(f"Key '{key}' EXISTS with value '{d[key]}'")
else:
    print(f"Key '{key}' does NOT exist in the dictionary")


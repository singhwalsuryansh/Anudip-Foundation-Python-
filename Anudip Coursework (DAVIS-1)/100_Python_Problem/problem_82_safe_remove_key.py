# ============================================================
# Problem 82: Safely Remove a Key from Dictionary
# ============================================================

n = int(input("Enter number of key-value pairs: "))
d = {}
for _ in range(n):
    k = input("  Key: ")
    v = input("  Value: ")
    d[k] = v
print(f"Dictionary : {d}")
key = input("Enter key to remove: ")
removed = d.pop(key, None)      # pop returns None if key not found
if removed is not None:
    print(f"Removed key '{key}' (value was '{removed}')")
else:
    print(f"Key '{key}' not found in dictionary")
print(f"After removal: {d}")


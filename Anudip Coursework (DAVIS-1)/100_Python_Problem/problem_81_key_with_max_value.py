# ============================================================
# Problem 81: Find Key with Maximum Value
# ============================================================

n = int(input("Enter number of key-value pairs: "))
d = {}
for _ in range(n):
    k = input("  Key: ")
    v = int(input("  Value: "))
    d[k] = v
max_key = max(d, key=d.get)
print(f"Dictionary : {d}")
print(f"Key with max value: '{max_key}' = {d[max_key]}")


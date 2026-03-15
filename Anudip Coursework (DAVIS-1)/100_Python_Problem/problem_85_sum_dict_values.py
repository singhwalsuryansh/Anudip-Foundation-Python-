# ============================================================
# Problem 85: Find Sum of All Dictionary Values
# ============================================================

n = int(input("Enter number of key-value pairs: "))
d = {}
for _ in range(n):
    k = input("  Key: ")
    v = float(input("  Value (number): "))
    d[k] = v
total = sum(d.values())
print(f"Dictionary : {d}")
print(f"Sum of values: {total}")


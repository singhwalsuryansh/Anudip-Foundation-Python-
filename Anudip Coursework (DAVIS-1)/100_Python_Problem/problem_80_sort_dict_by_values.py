# ============================================================
# Problem 80: Sort Dictionary by Values
# ============================================================

n = int(input("Enter number of key-value pairs: "))
d = {}
for _ in range(n):
    k = input("  Key: ")
    v = int(input("  Value: "))
    d[k] = v
sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))  # sort by value
print(f"Original      : {d}")
print(f"Sorted by val : {sorted_d}")


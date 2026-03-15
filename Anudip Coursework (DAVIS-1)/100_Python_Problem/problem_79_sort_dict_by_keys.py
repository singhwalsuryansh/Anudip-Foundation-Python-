# ============================================================
# Problem 79: Sort Dictionary by Keys
# ============================================================

n = int(input("Enter number of key-value pairs: "))
d = {}
for _ in range(n):
    k = input("  Key (string): ")
    v = int(input("  Value (int): "))
    d[k] = v
sorted_d = dict(sorted(d.items()))   # sort by key alphabetically
print(f"Original : {d}")
print(f"Sorted   : {sorted_d}")
# Sample Output:
#   Original : {'banana': 2, 'apple': 5}
#   Sorted   : {'apple': 5, 'banana': 2}


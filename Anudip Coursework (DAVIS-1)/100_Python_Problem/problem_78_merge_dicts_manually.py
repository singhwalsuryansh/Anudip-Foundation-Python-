# ============================================================
# Problem 78: Merge Two Dictionaries Manually
# ============================================================

d1 = {}
d2 = {}
n1 = int(input("How many key-value pairs in dict 1? "))
for _ in range(n1):
    k = input("  Key: ")
    v = input("  Value: ")
    d1[k] = v
n2 = int(input("How many key-value pairs in dict 2? "))
for _ in range(n2):
    k = input("  Key: ")
    v = input("  Value: ")
    d2[k] = v
merged = {}
for k, v in d1.items():
    merged[k] = v
for k, v in d2.items():
    merged[k] = v     # d2 values override d1 on conflict
print(f"Dict 1 : {d1}")
print(f"Dict 2 : {d2}")
print(f"Merged : {merged}")


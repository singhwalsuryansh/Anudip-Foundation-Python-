# ============================================================
# Problem 69: Count Occurrence of Element in Tuple
# ============================================================

raw = input("Enter numbers separated by spaces: ")
t = tuple(map(int, raw.split()))
target = int(input("Enter element to count: "))
count = 0
for item in t:
    if item == target:
        count += 1
print(f"'{target}' appears {count} time(s) in {t}")
# Sample Output:
#   '3' appears 2 time(s) in (1, 3, 2, 3, 4)


# ============================================================
# Problem 84: Create Dictionary from Two Lists
# ============================================================

raw_keys   = input("Enter keys (space-separated):   ")
raw_values = input("Enter values (space-separated): ")
keys   = raw_keys.split()
values = raw_values.split()
if len(keys) != len(values):
    print("Error: keys and values must have the same length.")
else:
    d = dict(zip(keys, values))    # zip pairs elements together
    print(f"Dictionary: {d}")
# Sample Output:
#   Dictionary: {'a': '1', 'b': '2', 'c': '3'}


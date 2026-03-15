# ============================================================
# Problem 56: Count Frequency of Elements in List
# ============================================================

def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1   # increment count
    return freq

raw = input("Enter numbers separated by spaces: ")
lst = list(map(int, raw.split()))
freq = count_frequency(lst)
print("Element : Frequency")
for k, v in sorted(freq.items()):
    print(f"  {k}     :  {v}")
# Sample Output:
#   Enter numbers: 1 2 3 2 1 2
#   1 : 2,  2 : 3,  3 : 1


# ============================================================
# Problem 59: Separate Even and Odd Numbers from List
# ============================================================

def separate_even_odd(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds  = [x for x in lst if x % 2 != 0]
    return evens, odds

raw = input("Enter numbers separated by spaces: ")
lst = list(map(int, raw.split()))
evens, odds = separate_even_odd(lst)
print(f"Even numbers: {evens}")
print(f"Odd  numbers: {odds}")
# Sample Output:
#   Even numbers: [2, 4, 6]
#   Odd  numbers: [1, 3, 5]


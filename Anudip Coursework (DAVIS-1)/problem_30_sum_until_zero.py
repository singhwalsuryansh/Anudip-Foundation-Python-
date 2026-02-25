# ============================================================
# Problem 30: Accept Numbers Until 0 is Entered and Print Sum
# ============================================================
# Approach: Keep reading numbers into a while loop until the
#           user enters 0, then print the running total.
#
# Example:
#   Input:  5, 3, 8, 2, 0
#   Output: Sum = 18
# ============================================================

total = 0
count = 0

print("Enter numbers (enter 0 to stop):")

while True:
    num = float(input("Enter number: "))
    if num == 0:
        break                # exit loop when 0 is entered
    total += num
    count += 1

print(f"\nYou entered {count} number(s).")
print(f"Sum = {total:.2f}")

# ============================================================
# Sample Output:
#   Enter numbers (enter 0 to stop):
#   Enter number: 5
#   Enter number: 3
#   Enter number: 8
#   Enter number: 2
#   Enter number: 0
#   You entered 4 number(s).
#   Sum = 18.00
# ============================================================

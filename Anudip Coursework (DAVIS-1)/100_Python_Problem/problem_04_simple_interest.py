# ============================================================
# Problem 4: Calculate Simple Interest
# ============================================================
# Formula: SI = (Principal * Rate * Time) / 100
#
# Example:
#   Principal = 1000, Rate = 5%, Time = 3 years
#   SI = (1000 * 5 * 3) / 100 = 150.0
# ============================================================

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# ---- Read input ----
principal = float(input("Enter Principal amount: "))
rate      = float(input("Enter Rate of interest (%): "))
time      = float(input("Enter Time period (years): "))

si = simple_interest(principal, rate, time)
print(f"\nSimple Interest = {si:.2f}")
print(f"Total Amount    = {principal + si:.2f}")

# ============================================================
# Sample Output:
#   Enter Principal amount: 1000
#   Enter Rate of interest (%): 5
#   Enter Time period (years): 3
#   Simple Interest = 150.00
#   Total Amount    = 1150.00
# ============================================================

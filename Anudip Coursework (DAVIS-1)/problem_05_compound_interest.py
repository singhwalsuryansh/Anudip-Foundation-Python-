# ============================================================
# Problem 5: Calculate Compound Interest
# ============================================================
# Formula: A = P * (1 + r/100)^t
#          CI = A - P
#
# Example:
#   Principal = 1000, Rate = 5%, Time = 3 years
#   CI ≈ 157.63
# ============================================================

def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    ci = amount - principal
    return ci, amount

# ---- Read input ----
principal = float(input("Enter Principal amount: "))
rate      = float(input("Enter Annual Rate (%): "))
time      = float(input("Enter Time period (years): "))

ci, amount = compound_interest(principal, rate, time)
print(f"\nCompound Interest = {ci:.2f}")
print(f"Total Amount      = {amount:.2f}")

# ============================================================
# Sample Output:
#   Enter Principal amount: 1000
#   Enter Annual Rate (%): 5
#   Enter Time period (years): 3
#   Compound Interest = 157.63
#   Total Amount      = 1157.63
# ============================================================

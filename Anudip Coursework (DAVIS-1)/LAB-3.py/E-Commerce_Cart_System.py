    # E-Commerece Cart System


cart = list(map(int, input("Enter product prices separated by space: ").split()))

# Remove duplicates
cart = list(set(cart))

total = sum(cart)

# Apply discount
if total > 5000:
    total *= 0.9   # 10% discount

# Add GST
total *= 1.18

print("Unique Cart Items:", cart)
print("Final Payable Amount:", round(total, 2))


# Output:

# Enter product prices separated by space: 1000 2000 3000 1000
# Unique Cart Items: [2000, 3000, 1000]
# Final Payable Amount: 7080.0

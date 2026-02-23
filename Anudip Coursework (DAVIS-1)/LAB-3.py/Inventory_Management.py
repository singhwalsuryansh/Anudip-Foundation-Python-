stock = list(map(int, input("Enter stock quantities: ").split()))

# Remove zero stock
stock = [s for s in stock if s > 0]

# Restock
for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

total_inventory = sum(stock)

print("Updated Stock:", stock)
print("Total Inventory Count:", total_inventory)


# Output:

# Enter stock quantities: 5 0 15 8 20
# Updated Stock: [55, 15, 58, 20]
# Total Inventory Count: 148

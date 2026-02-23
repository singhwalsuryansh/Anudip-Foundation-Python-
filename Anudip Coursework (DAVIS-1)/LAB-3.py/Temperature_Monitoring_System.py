# Temperature Monitoring System

temps = list(map(int, input("Enter daily temperatures: ").split()))

print("Hottest Temperature:", max(temps))
print("Coldest Temperature:", min(temps))

extreme_days = len([t for t in temps if t > 40])

for i in range(len(temps)):
    if temps[i] > 45:
        temps[i] = "Heat Alert"

print("Updated Temperature List:", temps)
print("Number of Extreme Days (>40°C):", extreme_days)


# Output:
# Enter daily temperatures: 30 35 42 38 46  
# Hottest Temperature: 46
# Coldest Temperature: 30
# Updated Temperature List: [30, 35, 42, 38, 'Heat Alert']
# Number of Extreme Days (>40°C): 2
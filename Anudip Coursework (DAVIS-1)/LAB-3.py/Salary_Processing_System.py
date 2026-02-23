# Salary Processing System

salaries = list(map(int, input("Enter salaries separated by space: ").split()))

min_wage = int(input("Enter minimum wage: "))

# Remove below minimum wage
salaries = [s for s in salaries if s >= min_wage]

# Add bonus
for i in range(len(salaries)):
    if salaries[i] > 50000:
        salaries[i] *= 1.05

# Sort descending
salaries.sort(reverse=True)

print("Processed Salaries:", salaries)
print("Top 3 Salaries:", salaries[:3])

# Output:

# Enter salaries separated by space: 30000 45000 60000 25000 70000
# Enter minimum wage: 30000
# Processed Salaries: [73500.0, 63000.0, 45000]
# Top 3 Salaries: [73500.0, 63000.0, 45000]

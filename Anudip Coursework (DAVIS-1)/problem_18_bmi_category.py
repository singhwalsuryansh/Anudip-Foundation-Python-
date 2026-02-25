# ============================================================
# Problem 18: Calculate BMI Category
# ============================================================
# Formula: BMI = weight(kg) / height(m)^2
#
# Categories:
#   BMI < 18.5           → Underweight
#   18.5 <= BMI < 25.0   → Normal weight
#   25.0 <= BMI < 30.0   → Overweight
#   BMI >= 30.0          → Obese
#
# Example:
#   Weight = 70 kg, Height = 1.75 m
#   BMI = 22.86 → Normal weight
# ============================================================

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

# ---- Read input ----
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"\nBMI      = {bmi:.2f}")
print(f"Category = {category}")

# ============================================================
# Sample Output:
#   Enter weight in kg: 70
#   Enter height in meters: 1.75
#   BMI      = 22.86
#   Category = Normal weight
# ============================================================

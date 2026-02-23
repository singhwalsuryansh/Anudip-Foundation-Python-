print("Electricity Bill Calculator")

units = float(input("Enter units consumed: "))
senior = input("Are you a senior citizen? (yes/no): ").lower()

bill = 0

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7
else:
    bill = units * 10

if senior == "yes":
    bill *= 0.90  # 10% discount

print("Total Electricity Bill:", bill)

-----------------------------------------------------------------------------------------

print("Smart Login System")

correct_username = "admin"
correct_password = "1234"
attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts += 1
        print("Invalid Credentials. Attempts left:", 3 - attempts)

if attempts == 3:
    print("Account Locked due to 3 failed attempts.")

---------------------------------------------------------------------------------------

print("Hospital Emergency Triage")

heart_rate_abnormal = input("Is heart rate abnormal? (yes/no): ").lower()
severe_injury = input("Is there severe injury? (yes/no): ").lower()
age = int(input("Enter patient age: "))

if heart_rate_abnormal == "yes" or severe_injury == "yes":
    print("Category: Critical")
else:
    condition = input("Enter condition (moderate/normal): ").lower()
    
    if condition == "moderate" and age > 65:
        print("Category: Critical (Upgraded due to age > 65)")
    elif condition == "moderate":
        print("Category: Moderate")
    else:
        print("Category: Normal")

----------------------------------------------------------------------------------------


print("Salary Increment System")

rating = int(input("Enter performance rating (1-5): "))
experience = int(input("Enter years of experience: "))
attendance = float(input("Enter attendance percentage: "))

increment = 0

if rating >= 4 and experience >= 5 and attendance >= 90:
    increment = 20
elif rating >= 3 and experience >= 3 and attendance >= 80:
    increment = 10
else:
    increment = 5

print("Increment Percentage:", increment, "%")

------------------------------------------------------------------------------------

print("ATM Withdrawal System")

balance = float(input("Enter account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM available cash: "))

if withdraw_amount > 50000:
    print("Withdrawal Failed: Daily limit exceeded.")
elif withdraw_amount > balance:
    print("Withdrawal Failed: Insufficient account balance.")
elif withdraw_amount > atm_cash:
    print("Withdrawal Failed: ATM has insufficient cash.")
else:
    print("Withdrawal Successful.")
    print("Remaining Balance:", balance - withdraw_amount)

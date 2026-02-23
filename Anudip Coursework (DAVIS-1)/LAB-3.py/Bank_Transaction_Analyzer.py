# Bank Transaction Analyzer

transactions = list(map(int, input("Enter transactions (+deposit, -withdrawal): ").split()))

balance = sum(transactions)

withdrawals = [t for t in transactions if t < 0]
largest_withdrawal = min(withdrawals) if withdrawals else 0

large_deposits = len([t for t in transactions if t > 10000])

print("Total Balance:", balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits greater than 10000:", large_deposits)


# Output:

# Enter transactions (+deposit, -withdrawal): 5000 -2000 15000 -500 3000
# Total Balance: 21000
# Largest Withdrawal: -2000
# Deposits greater than 10000: 1

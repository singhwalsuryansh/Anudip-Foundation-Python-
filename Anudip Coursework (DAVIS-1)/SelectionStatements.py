# This program checks whether a number is positive, negative, or zero

num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")


    # This program checks whether a number is even or odd

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")



# This program checks whether a number is even or odd

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")



    # This program finds the largest of two numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)



    # This program finds the largest among three numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


    # This program checks whether a given year is a leap year

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


    # This program checks if a person is eligible to vote

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")



    # This program assigns grade based on marks

marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Result: Fail")



    # This program checks if a number is divisible by both 5 and 11

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")



# This program performs basic arithmetic operations

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")



    # This program checks whether a character is a vowel or consonant

ch = input("Enter a character: ").lower()

if ch in "aeiou":
    print("It is a Vowel")
else:
    print("It is a Consonant")




    # This program checks whether a number is a multiple of 3 or 7

num = int(input("Enter a number: "))

if num % 3 == 0 or num % 7 == 0:
    print("Number is a multiple of 3 or 7")
else:
    print("Number is not a multiple of 3 or 7")
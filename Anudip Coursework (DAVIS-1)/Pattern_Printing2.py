n = input("Enter the number of columns: ")
if int(n) < 0:
    print("Please enter a positive integer.")
else:
    for rows in range(1,int(n)+1):
        print(" " * (int(n) - rows) + "*" * rows)



        
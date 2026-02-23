n = input("Enter the number of columns: ")  
if int(n) <= 0:
    print("Please enter a positive integer.")
else:
    for i in range (1,int(n)+1):
        print(" " * (int(n) - i) + "*" * (2*i-1))

        for j in range (int(n)-1,0,-1):
            print(" " * (int(n) - j) + "*" * (2*j-1))


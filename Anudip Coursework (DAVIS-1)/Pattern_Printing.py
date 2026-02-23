'''#*
#**
#***
#****
#*****
#******

# Pattern Printing in Python
for rows in range(1,7):
    print("*" * rows)'''


#     *  
#    **
#   ***
#  ****
# *****
#******

i=input("Enter the number of rows: ")
if i<0:
    print("Please enter a positive integer.")
else:
   for rows in range(1,int(i)+1):
    print(" " * (int(i) - rows) + "*" * rows)


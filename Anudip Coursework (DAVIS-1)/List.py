# Creating a list 
my_list = [1, 2, 3, 4, 5]
print(my_list) # display the complete list


print(*my_list) # display the list elements without brackets


# Accessing list elements
print(my_list[0]) # access the first element
print(my_list[2]) # access the third element


# Modifying list elements
my_list[1] = 10 # change the second element to 10
print(my_list) # display the modified list


# Display the list elements line by line
for element in my_list:
    print(element)



    # Finding the length of the list
print("Length of the list:", len(my_list))



# Sum of all elements in the list wihout using built-in function
sum = 0
for element in my_list:
    sum = sum + element

print("Sum of all elements in the list:", sum)


# Finding the maximum element in the list without using built-in function
max_element = my_list[0] # Assume the first element is the maximum
for index in range(1, len(my_list)):
    if my_list[index] > max_element:
        max_element = my_list[index]
print("Maximum element in the list:", max_element)


# Finding the minimum element in the list without using built-in function
min_element = my_list[0] # Assume the first element is the minimum
for index in range(1, len(my_list)):
    if my_list[index] < min_element:
        min_element = my_list[index]

print("Minimum element in the list:", min_element)



# Finding the average of the list elements without using built-in function
total_sum = 0
for element in my_list:
    total_sum = total_sum + element
average = total_sum / len(my_list)
print("Average of the list elements:", average)



# Finding the product of all elements in the list without using built-in function
product = 1
for element in my_list:
    product = product * element
print("Product of all elements in the list:", product)


# Finding the number of even and odd elements in the list without using built-in function
even_count = 0
odd_count = 0
for element in my_list:
    if element % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print("Number of even elements in the list:", even_count)
print("Number of odd elements in the list:", odd_count)


# Finding the number of positive and negative elements in the list without using built-in function
positive_count = 0
negative_count = 0
for element in my_list:
    if element > 0:
        positive_count = positive_count + 1
    elif element < 0:
        negative_count = negative_count + 1
print("Number of positive elements in the list:", positive_count)
print("Number of negative elements in the list:", negative_count)



# Insert an element at a specific position in the list
my_list.insert(2, 15) # Insert 15 at index 2
print("List after insertion:", my_list)

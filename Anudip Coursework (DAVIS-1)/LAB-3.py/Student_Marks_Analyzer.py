         # STUDENT MARKS ANALYZER


marks = list(map(int, input("Enter student marks separated by space: ").split()))

# Remove invalid marks
valid_marks = [m for m in marks if 0 <= m <= 100]

if len(valid_marks) == 0:
    print("No valid marks entered.")
else:
    average = sum(valid_marks) / len(valid_marks)
    highest = max(valid_marks)
    toppers = [m for m in valid_marks if m == highest]

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "D"

    print("Valid Marks:", valid_marks)
    print("Average:", round(average, 2))
    print("Topper Marks:", toppers)
    print("Grade:", grade)


    # Output:

    # Enter student marks separated by space: 85 92 78 88 95
    # Valid Marks: [85, 92, 78, 88, 95
    # Average: 87.6
    # Topper Marks: [95]
    # Grade: A
    
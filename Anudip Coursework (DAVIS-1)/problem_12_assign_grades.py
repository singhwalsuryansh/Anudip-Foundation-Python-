# ============================================================
# Problem 12: Assign Grades Based on Marks
# ============================================================
# Grade Scale:
#   90 - 100 → A+
#   80 -  89 → A
#   70 -  79 → B
#   60 -  69 → C
#   50 -  59 → D
#    0 -  49 → F (Fail)
#
# Example:
#   Input:  85
#   Output: Grade: A
# ============================================================

def assign_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F (Fail)"

# ---- Read input ----
marks = float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter between 0 and 100.")
else:
    grade = assign_grade(marks)
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")

# ============================================================
# Sample Output:
#   Enter marks (0-100): 85
#   Marks: 85.0
#   Grade: A
# ============================================================

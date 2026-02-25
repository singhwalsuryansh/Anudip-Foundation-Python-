# ============================================================
# Problem 76: Create Student Marks Dictionary and Find Topper
# ============================================================

n = int(input("How many students? "))
marks = {}
for _ in range(n):
    name  = input("  Enter student name:  ")
    score = float(input("  Enter marks:         "))
    marks[name] = score

print("\nStudent Marks:")
for name, score in marks.items():
    print(f"  {name}: {score}")

topper = max(marks, key=marks.get)
print(f"\nTopper: {topper} with {marks[topper]} marks")
# Sample Output:
#   Topper: Alice with 95.0 marks


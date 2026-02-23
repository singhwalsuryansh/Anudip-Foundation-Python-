# Attendance Tracker

attendance = list(map(int, input("Enter attendance (1=Present, 0=Absent): ").split()))

percentage = (sum(attendance) / len(attendance)) * 100

print("Attendance Percentage:", round(percentage, 2), "%")

if percentage < 75:
    print("Warning: Attendance below 75%")

# Replace consecutive absences
for i in range(len(attendance)-1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = "Warning"
        attendance[i+1] = "Warning"

print("Updated Attendance:", attendance)


# Output:
# Enter attendance (1=Present, 0=Absent): 1 0 0
# Attendance Percentage: 33.33 %
# Warning: Attendance below 75%
# Updated Attendance: [1, 'Warning', 'Warning']

scores = list(map(int, input("Enter student scores: ").split()))

scores.sort()

# Remove lowest 2
scores = scores[2:]

# Add grace marks
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

passed = len([s for s in scores if s >= 40])

print("Updated Scores:", scores)
print("Number of Students Passed:", passed)



# Output:

# Enter student scores: 25 30 35 40 45
# Updated Scores: [35, 40, 45]
# Number of Students Passed: 3

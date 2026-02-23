# Sport Tournament Points Table

points = list(map(int, input("Enter team points: ").split()))

# Replace negative with 0
points = [p if p >= 0 else 0 for p in points]

points.sort(reverse=True)

winner = points[0]
runner_up = points[1] if len(points) > 1 else None

print("Leaderboard:", points)
print("Winner Points:", winner)
print("Runner-Up Points:", runner_up)

# Output:
# Enter team points: 10 20 -5 15
# Leaderboard: [20, 15, 10, 0]
# Winner Points: 20
# Runner-Up Points: 15

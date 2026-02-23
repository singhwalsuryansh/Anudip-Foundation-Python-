ratings = list(map(int, input("Enter ratings (1-5): ").split()))

# Remove invalid
ratings = [r for r in ratings if 1 <= r <= 5]

average = sum(ratings) / len(ratings) if ratings else 0
five_star = ratings.count(5)

ratings.sort()

print("Valid Ratings:", ratings)
print("Average Rating:", round(average, 2))
print("Number of 5-Star Ratings:", five_star)



# Output:
# Enter ratings (1-5): 5 4 3 2 1
# Valid Ratings: [1, 2, 3, 4, 5]
# Average Rating: 3.0
# Number of 5-Star Ratings: 1

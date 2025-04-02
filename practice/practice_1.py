habits = ["drink water", "read", "exercise", "code"]

total_habits = len(habits)

print(f"First habit: {habits[0]}")
print(f"Last habit: {habits[-1]}")

habits = habits + ["pray"]

print(f"You're tracking 5 daily habits. First: {habits[0]} | Last: {habits[-1]}")


# Try replacing one of the habits with a new one
habits[2] = "sleep"

# Print the updated list
print(habits)

# Try printing all habits on separate lines using print(habits[0]), etc

print(f"List of Habits: \n{habits[0]}, \n{habits[1]}, \n{habits[2]}, \n{habits[3]}")
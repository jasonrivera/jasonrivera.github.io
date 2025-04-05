habits_to_track = input("How many habits do you want to track today? ")
habits_to_track = int(habits_to_track)

habits = []

for item in range(habits_to_track):
    habit = input("Enter a habit: ")
    habits.append(habit)

print(habits)
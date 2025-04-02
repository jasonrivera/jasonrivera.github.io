habits = ["drink water", "read", "exercise", "code"]

print("Your Daily Habits: ")

for i in habits:
    print(f"- {i}")
    
    print()
    print()
    
# Add numbers to your list
print("Your Daily Habits: ")

for i, habit in enumerate(habits):
    print(f"{i + 1}. {habit}")
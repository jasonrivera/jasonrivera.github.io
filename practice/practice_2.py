habits = ["drink water", "read", "exercise", "code"]

habit_to_check = "read"

if habit_to_check in habits:
    print(f"Yep, {habit_to_check} is on your list today!")
else:
    print(f"Nope, {habit_to_check} isn't on your list today.")
    
    
    
    # Ask the user which habit to check
ask_user = input("Which habit do you want to check? ")

if ask_user in habits:
    print(f"Yep, {ask_user} is on your list today!")
else:
    print(f"Nope, {ask_user} isn't on your list today.")
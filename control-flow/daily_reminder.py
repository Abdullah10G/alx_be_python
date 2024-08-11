task = input("Enter your task description:")
priority = input("Enter the priority (high, medium, low):")
time_bound = input("Is your task is a time-bound? (yes, No):")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task.Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task.Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print( f"Reminder: '{task}' is a low priority task that requires immediate attention today! ")
        else:
            print(f"Reminder: '{task}'  is a low priority task. Consider completing it when you have free time.")     
    case _:
        print("unknown priority,Try again.")        
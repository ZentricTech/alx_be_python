# daily_reminder.py

task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unknown priority level"

if time_bound == "yes":
    # Modify reminder for time-sensitive tasks
    if priority == "low":
        # If low priority but time bound, still mention immediate attention
        reminder = f"Reminder: '{task}' is a low priority task that requires immediate attention today!"
    else:
        reminder += " that requires immediate attention today!"
else:
    if priority != "low":
        reminder += "."
    else:
        reminder += ". Consider completing it when you have free time."

print(reminder)


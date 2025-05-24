import time
import datetime
import json
import winsound

reminders = []

def load_reminders():
    try:
        with open('reminders.json', 'r') as file:
            global reminders
            reminders = json.load(file)
    except FileNotFoundError:
        reminders = []

def save_reminders():
    with open('reminders.json', 'w') as file:
        json.dump(reminders, file)

def add_reminder():
    reminder = input("Enter your reminder: ")
    time_str = input("Enter time for reminder (HH:MM, e.g., 14:30): ")
    try:
        datetime.datetime.strptime(time_str, "%H:%M")
        reminders.append({"task": reminder, "time": time_str})
        save_reminders()
        print("Reminder added.")
    except ValueError:
        print("Invalid time format. Use HH:MM (e.g., 14:30).")

def show_reminders():
    if reminders:
        print("Reminders:")
        for i, reminder in enumerate(reminders, 1):
            print(f"{i}. {reminder['task']} at {reminder['time']}")
    else:
        print("No reminders available.")

def check_reminders():
    current_time = datetime.datetime.now().strftime("%H:%M")
    for reminder in reminders:
        if reminder["time"] == current_time:
            winsound.Beep(1000, 1000)  # Play beep at 1000 Hz for 1 second

load_reminders()

while True:
    check_reminders()
    print("\nMenu:")
    print("1. Add reminder")
    print("2. Show reminders")
    print("3. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        add_reminder()
    elif choice == '2':
        show_reminders()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Try again.")
    time.sleep(60)
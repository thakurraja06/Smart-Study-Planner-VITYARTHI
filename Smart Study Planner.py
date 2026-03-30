import json
import time
from datetime import datetime

FILE = "works.json"

'''loading works'''
def load_works():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

"""works saving"""
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

'''work adding'''
def add_task():
    text = input("Enter task: ")
    time_str = input("Enter date & time (YYYY-MM-DD HH:MM): ")

    try:
        task_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    except:
        print("Invalid format")
        return

    tasks = load_works()
    tasks.append({
        "text": text,
        "time": time_str,
        "notified": False
    })

    save_tasks(tasks)
    print("Work added")

'''works veiwing'''
def view_tasks():
    tasks = load_works()
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['text']} - {task['time']}")

#Deleting of unwanted/done work
def delete_task():
    tasks = load_works()
    view_tasks()

    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
        print("Work deleted!")
    except:
        print("Invalid input")

'''system reminder'''
def check_reminders():
    tasks = load_works()
    now = datetime.now()

    for task in tasks:
        task_time = datetime.strptime(task["time"], "%Y-%m-%d %H:%M")

        if task_time <= now and not task["notified"]:
            print(f"\n Reminder: {task['text']}\n")
            task["notified"] = True

    save_tasks(tasks)

# Main-menu showing
def main():
    while True:
        check_reminders()

        print("\n Smart Study Planner")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

        time.sleep(1)

if __name__ == "__main__":
    main()

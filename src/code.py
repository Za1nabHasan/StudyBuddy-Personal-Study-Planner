#   *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#   PERSONAL STUDY PLANNER
#   VITyarthi Project: Problem Solving and Programming Semester-1
#   By: Zainab Hasan (25MIB10050)
#   Faculty: Dr. Adyasha Sahu
#   *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

FILENAME = "study_tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                name, subject, deadline, status = line.strip().split("|")
                tasks.append({
                    "name": name,
                    "subject": subject,
                    "deadline": deadline,
                    "status": status})
    except FileNotFoundError:
        pass
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            line = f"{task['name']}|{task['subject']}|{task['deadline']}|{task['status']}\n"
            file.write(line)

# Add a new task
def add_task(tasks):
    print("\n--- Add New Study Task ---")
    name = input("Task Name: ")
    subject = input("Subject: ")
    deadline = input("Deadline (DD/MM/YYYY): ")

    tasks.append({
        "name": name,
        "subject": subject,
        "deadline": deadline,
        "status": "Pending"})

    print("Task added successfully!")

# View tasks
def view_tasks(tasks):
    print("\n--- Your Study Tasks ---")
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} | {task['subject']} | {task['deadline']} | {task['status']}")

# Search tasks by subject
def search_by_subject(tasks):
    subject = input("Enter subject to search: ")
    results = [t for t in tasks if t['subject'].lower() == subject.lower()]

    print("\n--- Search Results ---")
    if results:
        for task in results:
            print(f"{task['name']} | {task['deadline']} | {task['status']}")
    else:
        print("No tasks found for this subject.")

# Search tasks by deadline
from datetime import datetime
def sort_by_deadline(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    try:
        sorted_tasks = sorted(
            tasks,
            key=lambda x: datetime.strptime(x['deadline'], "%d/%m/%Y"))

        print("\n--- Tasks Sorted by Deadline ---")
        for t in sorted_tasks:
            print(f"{t['name']} | {t['subject']} | {t['deadline']} | {t['status']}")

    except ValueError:
        print("\nError: One or more deadlines are not in DD/MM/YYYY format.")


# Mark as completed
def mark_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    num = int(input("\nEnter task number to mark as completed: "))
    if 1 <= num <= len(tasks):
        tasks[num-1]['status'] = "Completed"
        print("Congratulations! Task marked as completed! (^¬^) ")
    else:
        print("Invalid task number.")

# Count Completed vs Pending Tasks
def task_summary(tasks):
    completed = sum(t['status'] == "Completed" for t in tasks)
    pending = len(tasks) - completed
    print(f"\nCompleted Tasks: {completed}")
    print(f"Pending Tasks: {pending}")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    num = int(input("\nEnter task number to delete: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        print("Task deleted!")
    else:
        print("Invalid number.")

# Menu
def main():
    tasks = load_tasks()

    while True:
        print("============================")
        print("     STUDY PLANNER     ")
        print("============================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Search Tasks by Subject")
        print("4. Sort Tasks by Deadline")
        print("5. Mark Task Completed")
        print("6. Count Completed vs Pending Tasks")
        print("7. Delete Task")
        print("8. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            search_by_subject(tasks)
        elif choice == "4":
             sort_by_deadline(tasks)
        elif choice == "5":   
            mark_completed(tasks)
        elif choice == "6":
            task_summary(tasks)
        elif choice == "7":
            delete_task(tasks)
        elif choice == "8":
            save_tasks(tasks)
            print("Goodbye! All tasks saved.")
            break
        else:
            print("Invalid choice. Please try again.")

main()

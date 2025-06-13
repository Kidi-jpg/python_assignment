tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Added: '{task}'")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['task']}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to delete: ")) - 1
            if 0 <= num < len(tasks):
                removed = tasks.pop(num)
                print(f"Deleted: '{removed['task']}'")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a number!")

def mark_complete():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to mark complete: ")) - 1
            if 0 <= num < len(tasks):
                tasks[num]["completed"] = True
                print(f"Marked as complete: '{tasks[num]['task']}'")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a number!")


while True:
    print("\n--- To-Do List Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Complete")
    print("5. Exit")
    
    choice = input("Choose (1-5): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_complete()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again!")
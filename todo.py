tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")

if __name__ == "__main__":
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task you want to add: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task = input("Enter the task you want to remove: ")
            remove_task(task)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Simple To-Do List Program

def show_menu():
    print("\nMenu:")
    print("1. Show To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

def show_tasks(tasks):
    if not tasks:
        print("\nYour To-Do List is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']} [{'Done' if task['done'] else 'Pending'}]")

def add_task(tasks):
    task_name = input("\nEnter the task name: ")
    tasks.append({'task': task_name, 'done': False})
    print(f"Task '{task_name}' added.")

def mark_task_done(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as done: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]['done'] = True
            print(f"Task '{tasks[task_num - 1]['task']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []  # List to store tasks
    while True:
        show_menu()
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                show_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                mark_task_done(tasks)
            elif choice == 4:
                remove_task(tasks)
            elif choice == 5:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Please enter a valid option.")

if __name__ == "__main__":
    main()

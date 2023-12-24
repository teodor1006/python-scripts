import json
import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE) as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks():
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file)
    except IOError:
        print("Error saving tasks.")

def validate_task_number(task_index):
    try:
        index = int(task_index)
        return 1 <= index <= len(tasks)
    except ValueError:
        return False

def add_task():
    name = input("Enter the task name: ")
    date = input("Enter the due date (YYYY-MM-DD): ")
    try:
        # Parse the due date and add the task to the list
        tasks.append({"name": name, "due_date": datetime.datetime.strptime(date, "%Y-%m-%d").date()})
        save_tasks()
        print(f"Task '{name}' added successfully!")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def view_tasks():
    print("Tasks:")
    # Use a list comprehension to print tasks with their indices
    [print(f"{i+1}. {task['name']} (Due: {task['due_date']})") for i, task in enumerate(tasks)]

def delete_task():
    view_tasks()
    index = input("Enter the task number to delete: ")
    if validate_task_number(index):
        # Delete the selected task and save the updated list
        deleted_task = tasks.pop(int(index) - 1)
        save_tasks()
        print(f"Task '{deleted_task['name']}' deleted successfully!")
    else:
        print("Invalid task number.")

# Function to display upcoming tasks
def due_date_reminder():
    today = datetime.date.today()
    upcoming_tasks = [task for task in tasks if task['due_date'] >= today]
    print("\nUpcoming tasks:" if upcoming_tasks else "\nNo upcoming tasks.")
    [print(f"{task['name']} (Due: {task['due_date']})") for task in upcoming_tasks]

def print_menu():
    print("\nTASK SCHEDULER MENU:\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Due Date Reminder\n5. Quit")

def menu_choice(choice):
    actions = [add_task, view_tasks, delete_task, due_date_reminder, exit]
    try:
        # Execute the chosen action based on the user's input
        actions[int(choice) - 1]() if 1 <= int(choice) <= 5 else print("Invalid choice. Please choose a valid option.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid option.")

# Load tasks from the data file (if it exists)
tasks = load_tasks()

while True:
    print_menu()
    menu_choice(input("Enter your choice: "))
    if input("Do you want to continue (y/n)? ").lower() != 'y':
        break

print("Goodbye!")

     

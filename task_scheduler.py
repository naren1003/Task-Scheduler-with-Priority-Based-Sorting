from datetime import datetime

# Define a Task class to represent each task
class Task:
    def __init__(self, name, deadline, priority):
        self.name = name
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M")  # Convert deadline to datetime object
        self.priority = priority  # Priority (1 = highest priority, 3 = lowest)

    # Method to calculate the time left for the task deadline
    def time_left(self):
        return self.deadline - datetime.now()

    # Method to display the task details
    def display_task(self):
        return f"Task: {self.name}, Deadline: {self.deadline.strftime('%Y-%m-%d %H:%M')}, Priority: {self.priority}, Time Left: {self.time_left()}"

# Function to add tasks
def add_task(tasks):
    name = input("Enter the task name: ")
    deadline = input("Enter the deadline (YYYY-MM-DD HH:MM): ")
    priority = int(input("Enter the priority (1-High, 2-Medium, 3-Low): "))
    tasks.append(Task(name, deadline, priority))
    print("Task added successfully!")

# Function to sort tasks by priority and remaining time
def sort_tasks(tasks):
    # Sorting by priority first, and by remaining time if priorities are the same
    return sorted(tasks, key=lambda task: (task.priority, task.time_left()))

# Function to display all tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        print(task.display_task())

# Main program loop
def task_scheduler():
    tasks = []
    while True:
        print("\nTask Scheduler")
        print("1. Add a new task")
        print("2. View sorted tasks")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            sorted_tasks = sort_tasks(tasks)
            display_tasks(sorted_tasks)
        elif choice == '3':
            print("Exiting Task Scheduler.")
            break
        else:
            print("Invalid option. Please choose again.")

# Running the Task Scheduler
if __name__ == "__main__":
    task_scheduler()

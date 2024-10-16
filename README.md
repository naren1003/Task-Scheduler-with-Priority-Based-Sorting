# Task-Scheduler-with-Priority-Based-Sorting
Task Scheduler with Priority-Based Sorting:


A Python-based Task Scheduler that helps users organize and manage their tasks by inputting deadlines and assigning priority levels. The tasks are dynamically sorted based on priority and the remaining time until the deadline, making time management more efficient.

Features:


* Add Tasks: Input task name, deadline, and priority level (1: High, 2: Medium, 3: Low).
* Sort Tasks: Automatically sorts tasks by priority and remaining time.
* View Sorted Tasks: Displays tasks in a clear, readable format, showing how much time is left before each task's deadline.
* Dynamic Updates: As time progresses, the tasks are always sorted according to the remaining time and priority.
Technologies Used
* Python: The project is built entirely in Python.
* Datetime Module: Used to handle and manipulate deadlines.


How It Works:

Users can add tasks with a name, a deadline, and a priority level.
The program calculates how much time is left until each task's deadline.
Tasks are sorted based on priority and remaining time:
Priority 1 (High) tasks come first, followed by Priority 2 (Medium) and Priority 3 (Low) tasks.
For tasks with the same priority, those with earlier deadlines are listed first.
The tasks are displayed in an organized manner, showing the task name, deadline, priority, and time left.

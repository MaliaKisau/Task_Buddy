# Initialize empty list to store tasks
tasks = []
completed_tasks = []

def add_task(task, priority="medium"):
    """
    Add a new task to the tasks list with an optional priority level.
    
    Args:
        task (str): The task to add.
        priority (str, optional): The priority level of the task (default is "medium").
    """
    tasks.append({"task": task, "priority": priority})
    print("Task added successfully!")

def delete_task(task_index):
    """
    Delete a task from the tasks list.
    
    Args:
        task_index (int): The index of the task to delete.
    """
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

def display_tasks():
    """Display all tasks in the tasks list."""
    if tasks:
        print("Your tasks:")
        for index, task_info in enumerate(tasks, start=1):
            print(f"{index}. {task_info['task']} - Priority: {task_info['priority']}")
    else:
        print("No tasks to display.")

def mark_completed(task_index):
    """
    Mark a task as completed by moving it from tasks list to completed_tasks list.
    
    Args:
        task_index (int): The index of the task to mark as completed.
    """
    if 0 <= task_index < len(tasks):
        completed_task = tasks.pop(task_index)
        completed_tasks.append(completed_task)
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def track_progress():
    """
    Track and display progress statistics.
    """
    total_tasks = len(tasks) + len(completed_tasks)
    completed_percent = (len(completed_tasks) / total_tasks) * 100 if total_tasks > 0 else 0
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {len(completed_tasks)}")
    print(f"Completed percentage: {completed_percent:.2f}%")

# Example of how uou xan use this:
add_task("Finish report", priority="high")
add_task("Go Grocery shopping", priority="medium")
add_task("Make sure to track online purchases", priority="low")
display_tasks()
mark_completed(0)
display_tasks()
track_progress()


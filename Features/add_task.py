from Data_storage.tasks import tasks, Task


def add_new_task():
    task_id = len(tasks) + 1
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter task due date: ")
    priority = input("Enter task priority: ")

    task = Task(task_id, title, description, due_date, priority)
    tasks.append(task)
    print("Task added successfully.")
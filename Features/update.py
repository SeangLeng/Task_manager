from Data_storage.tasks import tasks
from Features.view_task import view_tasks


def update_task():
    print("----------- update task ------------")
    view_tasks()
    task_id = int(input("Enter the task ID to update: "))
    found_task = None

    for task in tasks:
        if task.task_id == task_id:
            found_task = task
            break

    if found_task:
        print("Task found. Enter new details:")
        print("Update of: "
              "\n\t1. Title"
              "\n\t2. Description"
              "\n\t3. Due Date"
              "\n\t4. Priority")
        option = int(input("Enter your choice: "))

        if option == 1:
            found_task.title = input("Enter new task title: ")
            print("Task title updated successfully.")
        elif option == 2:
            found_task.description = input("Enter new task description: ")
            print("Task description updated successfully.")
        elif option == 3:
            found_task.due_date = input("Enter new task due date: ")
            print("Task due date updated successfully.")
        elif option == 4:
            found_task.priority = input("Enter new task priority: ")
            print("Task priority updated successfully.")
        else:
            print("Invalid option.")
    else:
        print("Task not found.")

    input()
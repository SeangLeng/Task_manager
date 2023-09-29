from Data_storage.save_to_file import read_from_file
from Data_storage.tasks import tasks, Task


def view_tasks():
    loaded_task_data = read_from_file()

    if loaded_task_data:
        tasks.clear()
        for task_dict in loaded_task_data:
            task = Task(task_dict["task_id"], task_dict["title"], task_dict["description"], task_dict["due_date"], task_dict["priority"])
            tasks.append(task)
            print(f"Task {task.task_id} "
                  f"\n\ttitle: {task.title}")
            print(f"\tTask description: {task.description}")
            print(f"\tTask due_date: {task.due_date}")
            print(f"\tTask priority: {task.priority}")
    else:
        print("No tasks found or there was an error reading the task data from the file.")
    # if tasks:
    #     for task in tasks:
    #         print(f"Task ID: {task.task_id}")
    #         print(f"Title: {task.title}")
    #         print(f"Description: {task.description}")
    #         print(f"Due Date: {task.due_date}")
    #         print(f"Priority: {task.priority}")
    #         print("-------------------------")
    # else:
    #     print("No tasks found.")

    input()

from Data_storage.tasks import tasks, history_removed_task
from Features.view_task import view_tasks


def delete_task():
    print("-------------------- Delete --------------------")
    print("All your task: ")
    view_tasks()

    task_number = input("Enter the number of task to remove: ")

    if 0 <= int(task_number) <= len(tasks):
        task_removed = tasks[int(task_number)-1]
        tasks.pop(int(task_number) - 1)
        history_removed_task.append(task_removed)
        print("Successful removed task")
    else:
        print("You are not have this task!")

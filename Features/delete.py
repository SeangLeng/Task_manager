from Data_storage.tasks import tasks, history_removed_task


def delete_task():
    print("-------------------- Delete --------------------")
    task_id = int(input("Enter the task ID to delete: "))
    found_task = None

    for task in tasks:
        if task.task_id == task_id:
            found_task = task
            break

    if found_task:
        tasks.remove(found_task)
        history_removed_task.append(found_task)
        print("Task deleted successfully.")
    else:
        print("Task not found.")

import json

from Data_storage.tasks import tasks, Task


def save_to_file():
    data = {"tasks": []}
    for task in tasks:
        task_data = {
            "task_id": task.task_id,
            "title": task.title,
            "description": task.description,
            "due_date": task.due_date,
            "priority": task.priority
        }
        data["tasks"].append(task_data)

    with open("task_data.json", 'w') as file:
        json.dump(data, file)

    print("Tasks saved to file.")
    input()


def read_from_file():
    try:
        with open("task_data.json", 'r') as file:
            task_data = json.load(file)
        return task_data["tasks"]
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: Unable to read task data from file.")
        return []
from Data_storage.tasks import tasks
def view_tasks():
    if not tasks:
        print("There are no tasks, you can add the task later!")
    else:
        for i, task in enumerate(tasks):
            print(f'\nTask {i + 1}: ')
            print(f'Title: {task.title}')
            print(f'\tDescription: {task.description}')
            print(f'\tDue_date: {task.due_date}')
            print(f'\tPriority: {task.priority}')

    input()

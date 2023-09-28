from Data_storage.tasks import tasks, Task


def add_new_task():
    print("------------ Add new task ---------------")
    title = input("Enter title: ")
    description = input("\tEnter description: ")
    due_date = input("\tEnter your task date: ")
    priority = input("\tEnter your priority: ")
    task = Task(title, description, due_date, priority)
    tasks.append(task)
    print('You have been added new task in your list, congratulation!!!\n')
# Task manager mini - project
from update import update_file

task = []


class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority


def manu():
    print("------------- Task manager --------------")
    print("1. View all tasks")
    print("2. Add new task")
    print("3. Updating new task")
    print("4. Delete task")


def all_tasks():
    for i, tasks in enumerate(task):
        print(f'Task {i+1}: ')
        print(f'\n Description: {tasks.description}')
        print(f'\n Due_date: {tasks.due_date}')
        print(f'\n priority: {tasks.priority}')


def option_check(choice):
    if choice == 1:
        print("--------------- Tasks ----------------")
        if not task:
            print("There are no tasks in the scope !!!")
        else:
            for i, tasks in enumerate(task):
                print(f'Task {i + 1}: ')
                print(f'\tTitle: {tasks.title}')
                print(f'\tDescription: {tasks.description}')
                print(f'\tDue date: {tasks.due_date}')
                print(f'\tpriority: {tasks.priority}')

        input()
    elif choice == 2:
        print("------------ Add new task ---------------")
        title = input("Enter title: ")
        description = input("\tEnter description: ")
        due_date = input("\tEnter your task date: ")
        priority = input("\tEnter your priority: ")
        tasks = Task(title, description, due_date, priority)
        task.append(tasks)
        print('You have been added new task in your list, congratulation!!!')
    elif choice == 3:
        print('------------ Update ------------')


while True:
    manu()
    choice = input("To access the manu by number (1 to 3): ")
    if int(choice) <= 3:
        option_check(int(choice))
    else:
        print("There are no this option !!!")

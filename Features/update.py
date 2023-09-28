from Data_storage.tasks import tasks
from Features.view_task import view_tasks


def update_task():
    print("----------- update task ------------")
    print("Your all tasks: ")
    view_tasks()
    task_number = input("Update the your task (task number): ")
    if 0 <= int(task_number) <= len(tasks):
        print("Update of: "
              "\n\t1. Title"
              "\n\t2. description"        
              "\n\t3. due_date"
              "\n\t4. priority")
        update_chose = input("Choose update option by the number of order: ")
        if int(update_chose) <= 4:
            if update_chose in ('1', 'title'):
                print("Your title: ", tasks[int(task_number) - 1].title)
                title = input("Replace title to: ")
                tasks[int(task_number) - 1].title = title
                print("You have successful changed, title to ", title)
            elif update_chose in ('2', 'description'):
                print("Your description: ", tasks[int(task_number) - 1].description)
                description = input("Replace description to: ")
                tasks[int(task_number) - 1].description = description
                print("You have successful changed, description to ", description)
            elif update_chose in ('3', 'due_date'):
                print("Your due_date: ", tasks[int(task_number) - 1].due_date)
                due_date = input("Replace due_date to: ")
                tasks[int(task_number) - 1].due_date = due_date
                print("You have successful changed, due_date to ", due_date)
            elif update_chose in ('4', 'priority'):
                print("Your priority: ", tasks[int(task_number) - 1].priority)
                priority = input("Replace due_date to: ")
                tasks[int(task_number) - 1].priority = priority
                print("You have successful changed, due_date to ", priority)
        else:
            print("there are no this options, try again")
    else:
        print("There are no this task")

    input()
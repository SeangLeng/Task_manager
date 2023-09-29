from Data_storage.save_to_file import save_to_file
from Features.History_delete import history_delete_task
from Features.add_task import add_new_task
from Features.delete import delete_task
from Features.update import update_task
from Features.view_task import view_tasks
from Task.options import manu

while True:
    manu()
    choice = input("Choose the option as number from 1 to 4: ")
    if choice in ('1', 'view all task'):
        view_tasks()
    elif choice in ('2', 'add new task'):
        add_new_task()
    elif choice in ('3', 'updating the task'):
        update_task()
    elif choice in ('4', 'delete task'):
        delete_task()
    elif choice in ('5', 'save task'):
        # save to file
        save_to_file()
    elif choice in ('6', 'Save your data'):
        history_delete_task()
    else:
        print("Exiting... ")
        break


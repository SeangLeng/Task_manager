from Data_storage.tasks import history_removed_task, tasks


def history_delete_task():
    for i, h_task in enumerate(history_removed_task):
        print(f'\nTask {h_task.task_id}: ')
        print(f'Title: {h_task.title}')
        print(f'\tDescription: {h_task.description}')
        print(f'\tDue_date: {h_task.due_date}')
        print(f'\tPriority: {h_task.priority}')

    recovery = input("Wanna to recovery (yes / no): ")
    if recovery == 'yes':
        task_recovery = input("Recovery task number?: ")
        if 0 <= int(task_recovery) <= len(history_removed_task):
            try:
                task_recovery = history_removed_task[int(task_recovery) - 1]
                tasks.append(task_recovery)
                print("Task restored successfully !!!")
                input()
            except IndexError:
                print("There are none of this task, try again")
        else:
            print("Invalid input. Please enter a valid task number.")
    elif recovery == 'no':
        pass

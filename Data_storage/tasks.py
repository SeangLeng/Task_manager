class Task:
    def __init__(self, task_id, title, description, due_date, priority):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority


tasks = []
history_removed_task = []
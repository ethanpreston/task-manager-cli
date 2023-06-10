class Task:
    def __init__(self, task, category, due_date, status, priority, description):
        self.task = task
        self.category = category
        self.due_date = due_date
        self.status = status
        self.priority = priority
        self.description = description

    def status_str(self):
        return "complete" if self.status else "incomplete"

    def __str__(self):
        return f"{self.task}, due at {self.due_date}, with a status of " \
               f"{self.status_str()} and a priority of {self.priority}"

class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.done = False

    def mark_done(self):
        self.done = True


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)

    def show_tasks(self):
        for task in self.tasks:
            status = "Виконано" if task.done else "Не виконано"
            print(task.name, "-", status)
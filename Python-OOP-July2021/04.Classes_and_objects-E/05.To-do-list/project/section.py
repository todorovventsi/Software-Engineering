class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = 0
        for task in self.tasks:
            if task.completed:
                completed_tasks += 1
                self.tasks.remove(task)
        return f"Cleared {completed_tasks} tasks."

    def view_section(self):
        first_row = f"Section {self.name}:\n"
        next_rows = [f"{task.details()}\n" for task in self.tasks]
        return f"{first_row}{''.join(next_rows)}"

class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str) -> None:
        """Add a new task to the todo list."""
        if not task:
            raise ValueError("Task cannot be empty.")
        self.tasks.append({'task': task, 'completed': False})
    def remove_task(self, task: str) -> None:
        """Remove a task from the todo list."""
        self.tasks = [t for t in self.tasks if t['task'] != task]
    def complete_task(self, task: str) -> None:
        """Mark a task as completed."""
        for t in self.tasks:
            if t['task'] == task:
                t['completed'] = True
                break
    def filter_tasks(self, completed: bool) -> list:
        """Get all tasks with their completion status."""
        return [t for t in self.tasks if t['completed'] == completed]

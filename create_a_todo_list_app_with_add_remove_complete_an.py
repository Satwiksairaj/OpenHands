class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str) -> None:
        if not task:
            raise ValueError("Task cannot be empty")
        self.tasks.append({'task': task, 'completed': False})
    def remove_task(self, task_index: int) -> None:
        try:
            self.tasks.pop(task_index)
        except IndexError:
            raise ValueError("Task index is out of range")
    def complete_task(self, task_index: int) -> None:
        try:
            self.tasks[task_index]['completed'] = True
        except IndexError:
            raise ValueError("Task index is out of range")
    def get_tasks(self, completed: bool = None) -> list:
        if completed is None:
            return self.tasks
        return [task for task in self.tasks if task['completed'] == completed]

# Example usage:
if __name__ == '__main__':
    todo_list = TodoList()
    todo_list.add_task('Learn Python')
    todo_list.complete_task(0)
    print(todo_list.get_tasks())

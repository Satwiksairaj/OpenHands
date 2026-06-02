import pytest
from create_a_todo_list_app_with_add_remove_complete_an import TodoList

def test_add_task():
    todo = TodoList()
    todo.add_task('Task 1')
    assert len(todo.tasks) == 1
    assert todo.tasks[0]['task'] == 'Task 1'
def test_add_empty_task():
    todo = TodoList()
    with pytest.raises(ValueError, match="Task cannot be empty"):
        todo.add_task('')
def test_remove_task():
    todo = TodoList()
    todo.add_task('Task 1')
    todo.remove_task(0)
    assert len(todo.tasks) == 0
def test_get_tasks_with_filter():
    todo = TodoList()
    todo.add_task('Task 1')
    todo.add_task('Task 2')
    todo.complete_task(0)
    assert len(todo.get_tasks()) == 2  # Get all tasks
    assert len(todo.get_tasks(completed=True)) == 1  # Get completed tasks
    assert len(todo.get_tasks(completed=False)) == 1  # Get incomplete tasks
    assert len(todo.get_tasks(filter_completed=True)) == 1  # Filter tasks that are completed
    todo = TodoList()
    todo.add_task('Task 1')
    todo.add_task('Task 2')
    todo.complete_task(0)
    assert len(todo.get_tasks()) == 2  # Get all tasks
    assert len(todo.get_tasks(completed=True)) == 1  # Get completed tasks
    assert len(todo.get_tasks(completed=False)) == 1  # Get incomplete tasks

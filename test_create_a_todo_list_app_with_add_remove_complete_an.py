import pytest
from create_a_todo_list_app_with_add_remove_complete_an import Todo

def test_add_task():
    todo = Todo()
    todo.add_task("Task 1")
    assert len(todo.tasks) == 1
    assert todo.tasks[0]['task'] == "Task 1"
def test_add_empty_task():
    todo = Todo()
    with pytest.raises(ValueError, match="Task cannot be empty."):
        todo.add_task("")
def test_remove_task():
    todo = Todo()
    todo.add_task("Task 1")
    todo.remove_task("Task 1")
    assert len(todo.tasks) == 0
def test_complete_task():
    todo = Todo()
    todo.add_task("Task 1")
    todo.complete_task("Task 1")
    assert todo.tasks[0]['completed'] is True
def test_filter_tasks():
    todo = Todo()
    todo.add_task("Task 1")
    todo.add_task("Task 2")
    todo.complete_task("Task 1")
    completed_tasks = todo.filter_tasks(completed=True)
    assert len(completed_tasks) == 1
    assert completed_tasks[0]['task'] == "Task 1"

    non_completed_tasks = todo.filter_tasks(completed=False)
    assert len(non_completed_tasks) == 1
    assert non_completed_tasks[0]['task'] == "Task 2"

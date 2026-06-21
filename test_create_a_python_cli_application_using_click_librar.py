"""
test_create_a_python_cli_application_using_click_librar.py
===============
Test cases for the task manager CLI application.

Author: Autonomous Agent
"""

import os
import click
from click.testing import CliRunner
from create_a_python_cli_application_using_click_librar import cli

TASKS_FILE = 'tasks.json'

# Remove tasks.json before each test
if os.path.exists(TASKS_FILE):
    os.remove(TASKS_FILE)

def test_add_task():
    runner = CliRunner()
    result = runner.invoke(cli, ['add', 'Test Task'])
    assert result.exit_code == 0, "Failed to add task"
    assert 'Task added: Test Task' in result.output
    with open(TASKS_FILE, 'r') as f:
        tasks = json.load(f)
        assert len(tasks) == 1
        assert tasks[0]['title'] == 'Test Task'
def test_list_tasks():
    os.remove(TASKS_FILE)  # Ensure no tasks exist
    runner = CliRunner()
    runner.invoke(cli, ['add', 'Test Task'])
    result = runner.invoke(cli, ['list'])
    assert result.exit_code == 0, "Failed to list tasks"
    assert 'Test Task' in result.output
def test_delete_task():
    runner = CliRunner()
    runner.invoke(cli, ['add', 'Test Task'])
    result = runner.invoke(cli, ['delete', 'Test Task'])
    assert result.exit_code == 0, "Failed to delete task"
    assert 'Task deleted: Test Task' in result.output
    result = runner.invoke(cli, ['list'])
    assert result.exit_code == 0
    assert 'Test Task' not in result.output
"""

TASKS_FILE = 'tasks.json'

# Remove tasks.json before each test
if os.path.exists(TASKS_FILE):
    os.remove(TASKS_FILE)

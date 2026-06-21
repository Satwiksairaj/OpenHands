"""
create_a_python_cli_application_using_click_librar.py
=============
A simple CLI application for managing tasks using Click.

Usage:
    python create_a_python_cli_application_using_click_librar.py

Author: Autonomous Agent
"""

import click
import json
from typing import List, Dict

class Task:
    """Class representing a task."""
    def __init__(self, title: str) -> None:
        self.title = title

    def to_dict(self) -> dict:
        return {'title': self.title}
class TaskManager:
    """Class for managing tasks using JSON file storage. This class is responsible for managing tasks and performing CRUD operations on them using a JSON file.""""
    def load_tasks(self) -> None:
        try:
            with open(self.filename, 'r') as f:
                self.tasks = [Task(**data) for data in json.load(f)]
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            self.tasks = []
    def save_tasks(self) -> None:
        with open(self.filename, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)
    def add_task(self, title: str) -> None:
        new_task = Task(title)
        self.tasks.append(new_task)
        self.save_tasks()
    def list_tasks(self) -> None:
        for task in self.tasks:
            click.secho(task.title, fg='blue')
@click.group()
def cli():
    """Command line interface for managing tasks."""
    pass

@cli.command()
@click.argument('title')
@click.pass_context
def add(ctx, title):
    """Add a new task."""
    manager = TaskManager('tasks.json')
    manager.add_task(title)
    click.secho(f'Task has been successfully added: {title}', fg='green')

@cli.command()
@click.pass_context
def list():
    """List all tasks."""
    manager = TaskManager('tasks.json')
    manager.list_tasks()

@cli.command()
@click.argument('title')
@click.pass_context
if __name__ == '__main__':
    cli()
  
import click
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    """Load tasks from todo.json"""
    if not os.path.exists(TODO_FILE):
        return []  # Agar file nahi mili to empty list return karein
    with open(TODO_FILE, "r") as file:
        try:
            return json.load(file)  # JSON read karna
        except json.JSONDecodeError:
            return []  # Agar JSON corrupt hai to empty list

def save_tasks(tasks):
    """Save tasks to todo.json"""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})  # ⬅️ Yeh line fix ki gayi hai
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")

cli.add_command(add)

if __name__ == "__main__":
    cli()

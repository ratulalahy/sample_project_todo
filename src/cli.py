import click
from rich.console import Console
from rich.table import Table
from datetime import datetime
from src.models.task import Task
from src.commands.task_manager import TaskManager


class CLIApp:
    def __init__(self):
        self.task_manager = TaskManager()
        self.console = Console()

    def run(self):
        # This method will start the CLI application
        self.cli()

    @click.group()
    def cli(self):
        """Task Management CLI"""
        pass

    @cli.command(help="Add a new task.")
    @click.option('--title', prompt=True)
    @click.option('--description', default='')
    @click.option('--due-date', type=click.DateTime(formats=["%Y-%m-%d"]), prompt=True)
    @click.option('--course-tag', default=None, help="Associated course tag.")
    def add_task(self, title, description, due_date, course_tag):
        new_task = Task(
            id=self.task_manager.generate_id(), 
            title=title, 
            description=description, 
            due_date=due_date, 
            course_tag=course_tag
        )
        self.task_manager.add_task(new_task)
        click.echo("Task added successfully.")

    @click.command(help="List all tasks.")
    def list_tasks(self):
        """Lists all tasks"""
        tasks = self.task_manager.tasks
        if not tasks:
            self.console.print("[italic]No tasks found![/italic]")
            return

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim")
        table.add_column("Title")
        table.add_column("Due Date")
        table.add_column("Course Tag", justify="right")

        for task in tasks:
            table.add_row(
                str(task.id),
                task.title,
                task.due_date.strftime("%Y-%m-%d"),
                task.course_tag or "N/A"
            )

        self.console.print(table)



# Ensure to add this command to your CLI group if not already done
if __name__ == '__main__':
    app = CLIApp()
    app.run()

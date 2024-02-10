import pytest
from datetime import datetime
from models.task import Task
from ..src.commands.task_manager import TaskManager

class TestTaskManager:
    """Tests for the TaskManager class."""

    def test_add_task(self):
        """Test adding a task to the manager."""
        manager = TaskManager()
        task = Task(id=1, title="Add task test", description="Testing add_task", due_date=datetime.now())
        manager.add_task(task)
        assert task in manager.tasks, "TaskManager.add_task() should add a task to the tasks list"

    def test_delete_task(self):
        """Ensure a task can be deleted."""
        manager = TaskManager()
        task = Task(id=2, title="Delete task test", description="Testing delete_task", due_date=datetime.now())
        manager.add_task(task)
        manager.delete_task(0)  # Assuming the task was added as the first item
        assert task not in manager.tasks, "TaskManager.delete_task() should remove the task from the tasks list"

    def test_find_tasks_by_course_tag(self):
        """Verify tasks can be filtered by course tag."""
        manager = TaskManager()
        task1 = Task(id=3, title="Task for Course A", description="Course A task", due_date=datetime.now(), course_tag="CourseA")
        task2 = Task(id=4, title="Task for Course B", description="Course B task", due_date=datetime.now(), course_tag="CourseB")
        manager.add_task(task1)
        manager.add_task(task2)
        filtered_tasks = manager.find_tasks(course_tag="CourseA")
        assert task1 in filtered_tasks and task2 not in filtered_tasks, "TaskManager.find_tasks() should filter tasks by course tag"

    def test_prioritize_task(self):
        """Check that a task's priority can be updated."""
        manager = TaskManager()
        task = Task(id=5, title="Priority test", description="Testing prioritize_task", due_date=datetime.now())
        manager.add_task(task)
        manager.prioritize_task(0, "HIGH")  # Assuming the task was added as the first item
        assert task.priority == "HIGH", "TaskManager.prioritize_task() should update the task's priority"

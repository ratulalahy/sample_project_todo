from typing import List, Optional
from ..models.task import Task
from datetime import datetime


class TaskManager:
    def __init__(self):
        """Initialize the TaskManager with an empty list of tasks."""
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a new task to the list.
        
        Args:
            task (Task): The task object to be added.
        """
        self.tasks.append(task)

    def edit_task(self, task_id: int, **kwargs):
        """Edit an existing task based on its ID.
        
        Args:
            task_id (int): The unique identifier for the task to edit.
            **kwargs: Arbitrary keyword arguments representing task attributes to update.
        """
        task = self.tasks[task_id]
        for attr, value in kwargs.items():
            setattr(task, attr, value)

    def delete_task(self, task_id: int):
        """Delete a task by its ID.
        
        Args:
            task_id (int): The unique identifier for the task to delete.
        """
        self.tasks.pop(task_id)

    def find_tasks(self, filter_by: Optional[dict] = None) -> List[Task]:
        """Find tasks based on certain criteria.
        
        Args:
            filter_by (Optional[dict]): Dictionary of attributes to filter tasks by.

        Returns:
            List[Task]: A list of tasks that match the filter criteria.
        """
        if not filter_by:
            return self.tasks
        filtered_tasks = [task for task in self.tasks if all(getattr(task, key) == value for key, value in filter_by.items())]
        return filtered_tasks


    def set_reminder(self, task_id: int, reminder: datetime):
        """Set a reminder for a task.
        
        Args:
            task_id (int): The unique identifier for the task to set a reminder for.
            reminder (datetime): The date and time to set the reminder for.
        """
        self.tasks[task_id].reminder = reminder
        
        
    def organize_tasks_into_lists(self, list_name: str, task_ids: List[int]):
        """Organize tasks into lists.
        
        Args:
            list_name (str): The name of the list to organize the tasks into.
            task_ids (List[int]): A list of unique identifiers for the tasks to organize.
        """
        self.lists[list_name] = [self.tasks[task_id] for task_id in task_ids]
        

    def prioritize_task(self, task_id: int, priority: str) -> None:
        """Set priority level for a task."""
        raise NotImplementedError


    def review_completed_tasks(self) -> List[Task]:
        """Return a list of completed tasks."""
        raise NotImplementedError
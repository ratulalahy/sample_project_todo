from enum import Enum, auto
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

class Priority(Enum):
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()


@dataclass
class Task:
    id: int
    title: str
    description: str
    due_date: datetime
    course_tag: Optional[str] = None
    priority: Priority = Priority.MEDIUM
    completed: bool = False
    reminder: Optional[datetime] = None

    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def set_reminder(self, reminder_time: datetime) -> None:
        """Set or update the reminder time for the task."""
        self.reminder = reminder_time

    def update(self, **kwargs) -> None:
        """General method to update task properties."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def display_info(self) -> str:
        """Return a formatted string containing the task's details."""
        info_lines = [
            f"Task ID: {self.id}",
            f"Title: {self.title}",
            f"Description: {self.description}",
            f"Due Date: {self.due_date.strftime('%Y-%m-%d')}",
            f"Priority: {self.priority.name}",
            f"Completed: {'Yes' if self.completed else 'No'}"
        ]
        if self.course_tag:
            info_lines.append(f"Course Tag: {self.course_tag}")
        if self.reminder:
            info_lines.append(f"Reminder: {self.reminder.strftime('%Y-%m-%d %H:%M')}")
        return "\n".join(info_lines)

import pytest
from datetime import datetime, timedelta
from models.task import Task

class TestTask:
    """Tests for the Task model."""

    def test_mark_completed(self):
        """Ensure a task can be marked as completed."""
        task = Task(id=1, title="Complete testing", description="Write unit tests for the application", due_date=datetime.now())
        task.mark_completed()
        assert task.completed, "Task.mark_completed() should set completed to True"

    def test_set_reminder(self):
        """Verify setting a reminder updates the task appropriately."""
        task = Task(id=2, title="Set reminder", description="Test reminder functionality", due_date=datetime.now())
        reminder_time = datetime.now() + timedelta(days=1)
        task.set_reminder(reminder_time)
        assert task.reminder == reminder_time, "Task.set_reminder() should update the reminder time"

    def test_update_task_title(self):
        """Test updating the task's title."""
        task = Task(id=3, title="Old Title", description="Testing update function", due_date=datetime.now())
        new_title = "New Title"
        task.update(title=new_title)
        assert task.title == new_title, "Task.update() should update the task's title"

    def test_due_date_in_past(self):
        """Check validation for due dates in the past."""
        past_due_date = datetime.now() - timedelta(days=1)
        with pytest.raises(ValueError):
            Task(id=4, title="Past Due", description="Due date is in the past", due_date=past_due_date)

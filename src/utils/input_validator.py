from abc import ABC, abstractmethod
from typing import Any
import datetime

class BaseValidator(ABC):
    """Abstract base class for input validation."""

    @abstractmethod
    def validate(self, input) -> bool:
        """
        Validates the given input.

        Args:
            input: The input to validate.

        Returns:
            bool: True if input is valid, False otherwise.
        """
        pass

class DateValidator(BaseValidator):
    """Validates date inputs."""

    @staticmethod
    def validate(self, date_input: str) -> bool:
        """
        Validates a date string.

        Args:
            date_input (str): The date input as a string.

        Returns:
            bool: True if the date string is valid, False otherwise.
        """
        try:
            datetime.datetime.strptime(date_input, "%Y-%m-%d")
            return True
        except ValueError:
            return False

class PriorityValidator(BaseValidator):
    """Validates task priority inputs."""
    @staticmethod
    def validate(self, priority_input: str) -> bool:
        """
        Validates a priority string.

        Args:
            priority_input (str): The priority input as a string.

        Returns:
            bool: True if the priority is valid, False otherwise.
        """
        if priority_input.lower() in ['high', 'medium', 'low']:
            return True
        else:
            return False

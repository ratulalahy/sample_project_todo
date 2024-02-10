import json
from typing import List
from models.task import Task

class FileHandler:
    """Handles file operations for task data persistence."""

    @staticmethod
    def save_data_to_file(data: list, file_path: str) -> None:
        """
        Saves data to a specified file in JSON format.

        Args:
            data (list): The data to save.
            file_path (str): The path to the file where data will be saved.
        """
        pass

    @staticmethod
    def load_data_from_file(file_path: str) -> list:
        """
        Loads data from a specified file.

        Args:
            file_path (str): The path to the file from which data will be loaded.

        Returns:
            list: The data loaded from the file.
        """
        pass


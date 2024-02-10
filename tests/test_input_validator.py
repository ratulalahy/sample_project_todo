import pytest
from utils.input_validator import DateValidator, PriorityValidator
import pytest
from utils.input_validator import DateValidator, PriorityValidator

class TestBaseValidator:
    """Tests for the BaseValidator abstract class."""

    def test_validator_interface(self):
        """Test that subclasses must implement the validate method."""
        # Test to ensure that instantiating a subclass without a validate method raises an error.
        

class TestDateValidator:
    """Tests for the DateValidator class."""

    def test_date_validator_valid_input():
        """Test the DateValidator with valid input."""
        # Example of valid date strings
        valid_dates = [
            "2022-01-01",
            "1999-12-31",
            "2023-02-28",
        ]
        
        # Initialize the DateValidator
        validator = DateValidator()
        
        # Iterate through the list of valid date strings and assert the validation passes
        for date_str in valid_dates:
            assert validator.validate(date_str), f"DateValidator.validate() failed for valid date input: {date_str}"

    def test_date_validator_invalid_input():
        """Test the DateValidator with invalid input."""
        # Example of invalid date strings
        invalid_dates = [
            "2022-13-01", # invalid month
            "1999-02-29", # invalid day for non-leap year
            "not-a-date", # completely invalid format
            "2022-02-30", # invalid day
            "2022-00-20", # invalid month
            "202-01-01",  # inncorrect year format
        ]
        
        # Initialize the DateValidator
        validator = DateValidator()
        
        # Iterate through the list of invalid date strings and assert the validation fails
        for date_str in invalid_dates:
            assert not validator.validate(date_str), f"DateValidator.validate() incorrectly validated invalid date input: {date_str}"

class TestPriorityValidator:
    """Tests for the PriorityValidator class."""

    def test_priority_validator_valid_input(self):
        """Test PriorityValidator with valid input."""
        # Assuming PriorityValidator accepts "HIGH", "MEDIUM", "LOW" as valid inputs
        valid_priorities = ["HIGH", "MEDIUM", "LOW"]
        
        # Initialize the PriorityValidator
        validator = PriorityValidator()
        
        # Iterate through the list of valid priority inputs and assert the validation passes
        for priority in valid_priorities:
            assert validator.validate(priority), f"PriorityValidator.validate() failed for valid priority input: {priority}"

    def test_priority_validator_invalid_input(self):
        """Test PriorityValidator with invalid input."""
        # Examples of invalid priority inputs
        invalid_priorities = [
            "high",  # incorrect case
            "medium",# incorrect case
            "urgent",# not a predefined priority level
            "",      # empty string
            "1",     # numeric value
            "LOWEST",# not a predefined priority level
        ]
        
        # Initialize the PriorityValidator
        validator = PriorityValidator()
        
        # Iterate through the list of invalid priority inputs and assert the validation fails
        for priority in invalid_priorities:
            assert not validator.validate(priority), f"PriorityValidator.validate() incorrectly validated invalid priority input: {priority}"

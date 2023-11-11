# test_custom_datetime.py
from custom_datetime import CustomDatetime
import pytest

def test_default_instance():
    current_datetime = CustomDatetime()
    assert current_datetime.year is not None
    # Add more assertions for other properties and methods

def test_specific_instance():
    specific_datetime = CustomDatetime(year=2023, month=11, day=15, hour=12, minute=30, second=45)
    assert specific_datetime.year == 2023
    # Add more assertions for other properties and methods

# Add more test cases for different scenarios

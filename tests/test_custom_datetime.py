# test_custom_datetime.py

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from custom_datetime import CustomDatetime
import pytest

# Rest of your test code...


def test_from_iso_format():
    dt = CustomDatetime.from_iso_format("2023-11-11T12:30:00")
    assert dt.year == 2023
    assert dt.month == 11
    assert dt.day == 11
    assert dt.hour == 12
    assert dt.minute == 30
    assert dt.second == 0

def test_iso_format():
    dt = CustomDatetime(2023, 11, 11, 12, 30, 0)
    assert dt.iso_format() == "2023-11-11T12:30:00"

# Add more tests as needed

# custom_datetime.py

class CustomDatetime:
    def __init__(self, year=None, month=None, day=None, hour=0, minute=0, second=0):
        try:
            self.year = int(year)
            self.month = int(month)
            self.day = int(day)
            self.hour = int(hour)
            self.minute = int(minute)
            self.second = int(second)
        except ValueError as e:
            raise ValueError("Invalid input. Please provide valid integer values for date and time components.") from e

    @classmethod
    def from_iso_format(cls, iso_string):
        try:
            # Implement logic to create an instance from ISO 8601 format
            # Example: "2023-11-11T12:30:00"
            parts = iso_string.split("T")
            date_parts = [int(part) for part in parts[0].split("-")]
            time_parts = [int(part) for part in parts[1].split(":")]

            return cls(*date_parts, *time_parts)
        except (ValueError, IndexError) as e:
            raise ValueError("Invalid ISO 8601 format. Please provide a valid string.") from e

    def iso_format(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}T{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def human_readable_format(self):
        return f"{self.month:02d}/{self.day:02d}/{self.year:04d} {self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year must be an integer.")
        self._year = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if not isinstance(value, int) or not (1 <= value <= 12):
            raise ValueError("Month must be an integer between 1 and 12.")
        self._month = value

    # Repeat for other properties: day, hour, minute, second

    @staticmethod
    def date_validation(day, month, year):
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise ValueError("Day, month, and year must be integers.")
        if not (1 <= month <= 12 and 1 <= day <= CustomDatetime.days_in_month(month, year)):
            raise ValueError("Invalid date")
        return True

    @classmethod
    def date_difference(cls, date1, date2, unit='days'):
        delta = date1 - date2
        if unit == 'days':
            return abs(delta.days)
        elif unit == 'weeks':
            return abs(delta.days) // 7
        elif unit == 'months':
            return abs((date1.year - date2.year) * 12 + date1.month - date2.month)
        else:
            raise ValueError("Invalid unit")

    @classmethod
    def date_from_string(cls, date_string):
        try:
            # Implement logic to create date objects from date strings
            # Example: "2023-11-11"
            parts = date_string.split("-")
            year, month, day = map(int, parts)
            cls.date_validation(day, month, year)  # Validate the date
            return cls(year, month, day)
        except (ValueError, IndexError) as e:
            raise ValueError("Invalid date string. Please provide a valid string.") from e

    @staticmethod
    def format_as_iso(year, month, day, hour=0, minute=0, second=0):
        return f"{year:04d}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}"

    @staticmethod
    def format_as_human_readable(year, month, day, hour=0, minute=0, second=0):
        return f"{month:02d}/{day:02d}/{year:04d} {hour:02d}:{minute:02d}:{second:02d}"

    @staticmethod
    def convert_to_gregorian(year, month, day):
        return year, month, day

    @staticmethod
    def convert_to_julian(year, month, day):
        return year, month, day

    @staticmethod
    def weekday_calculation(year, month, day):
        if month < 3:
            month += 12
            year -= 1

        K = year % 100
        J = year // 100

        day_of_week = (day + 13 * (month + 1) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

        return (day_of_week + 5) % 7

    @staticmethod
    def days_in_month(month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month == 2:
            return 29
        else:
            return 30

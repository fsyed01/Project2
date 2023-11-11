# main.py
from my_datetime import MyDateTime

def main():
    # Example 1: Formatting
    iso_date = MyDateTime.format_as_iso(2023, 11, 11)
    print("ISO Date:", iso_date)

    human_readable_date = MyDateTime.format_as_human_readable(2023, 11, 11)
    print("Human Readable Date:", human_readable_date)

    # Example 2: Conversion
    gregorian_date = MyDateTime.convert_to_gregorian(2023, 11, 11)
    print("Gregorian Date:", gregorian_date)

    julian_date = MyDateTime.convert_to_julian(2023, 11, 11)
    print("Julian Date:", julian_date)

    # Example 3: Weekday Calculation
    weekday = MyDateTime.calculate_weekday(2023, 11, 11)
    print("Weekday:", weekday)

if __name__ == "__main__":
    main()

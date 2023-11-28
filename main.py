from custom_datetime import CustomDatetime

def main():
    # Example 1: Formatting
    iso_date = CustomDatetime.format_as_iso(2023, 11, 11)
    print("ISO Date:", iso_date)

    human_readable_date = CustomDatetime.format_as_human_readable(2023, 11, 11)
    print("Human Readable Date:", human_readable_date)

    # Example 2: Conversion
    gregorian_date = CustomDatetime.convert_to_gregorian(2023, 11, 11)
    print("Gregorian Date:", gregorian_date)

    julian_date = CustomDatetime.convert_to_julian(2023, 11, 11)
    print("Julian Date:", julian_date)

    # Example 3: Weekday Calculation
    weekday = CustomDatetime.weekday_calculation(2023, 11, 11)
    print("Weekday:", weekday)

if __name__ == "__main__":
    main()

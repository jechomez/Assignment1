#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Fall 2024
Program: assignment1.py
Author: Jerrico Gomez
The python code in this file is original work written by
Jerrico Gomez. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Description: Counts the number of weekend days (Saturdays and Sundays) 
within a given period between two valid dates.
'''

import sys

def day_of_week(date: str) -> str:
    """Gets the weekday for a specific date (YYYY-MM-DD)."""
    year, month, day = (int(x) for x in date.split('-'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}
    if month < 3:
        year -= 1
    num = (year + year // 4 - year // 100 + year // 400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    """Determines whether a given year is a leap year or not."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """Calculates and returns the maximum number of days present in a given month and year."""
    month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return 29 if month == 2 and leap_year(year) else month_days[month]

def after(date: str) -> str:
    """Calculates and returns the date of the following day in the format year-month-day."""
    year, month, day = (int(x) for x in date.split('-'))
    day += 1
    if day > mon_max(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return f"{year:04}-{month:02}-{day:02}"

def usage():
    """Displays instructions on how to use the program."""
    print("Usage:", sys.argv[0], "YYYY-MM-DD YYYY-MM-DD")
    sys.exit()
    
def valid_date(date: str) -> bool:
    """Verifies whether a given date string in the format year-month-day is valid or not."""
    try:
        year, month, day = map(int, date.split('-'))
    except ValueError:
        return False
    return 1 <= month <= 12 and 1 <= day <= mon_max(month, year) and 1000 <= year <= 9999

def day_count(start_date: str, end_date: str) -> int:
    """Calculates the number of Saturdays and Sundays occurring between a specified start date and end date."""
    weekend_count = 0
    current_date = start_date
    while current_date <= end_date:
        if day_of_week(current_date) in ["Sat", "Sun"]:
            weekend_count += 1
        current_date = after(current_date)
    return weekend_count

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    start_date, end_date = sys.argv[1], sys.argv[2]

    if not valid_date(start_date) or not valid_date(end_date):
        usage()

    # Ensure start_date is before end_date
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    weekends = day_count(start_date, end_date)
    print(f"The period between {start_date} and {end_date} includes {weekends} weekend days.")

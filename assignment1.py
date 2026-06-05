#!/usr/bin/env python3
"""
OPS445 Assignment 1 - Version A

Program: assignment1.py
Author: Vidhi Patel
Student ID: 124656240
Semester: Summer 2026

Description:
Calculates the number of weekend days (Saturdays and Sundays)
between a given start date and end date (inclusive).

Academic Honesty:
Original work; no code copied except instructor-provided code.
"""

import sys

def leap_year(year: int) -> bool:
    """Return True if the year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """Return the maximum number of days in a given month and year."""
    if month == 2:
        return 29 if leap_year(year) else 28
    days_in_month = {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    return days_in_month.get(month, 31)

def after(date: str) -> str:
    """Return the next date in YYYY-MM-DD format."""
    y, m, d = map(int, date.split('-'))
    d += 1
    if d > mon_max(m, y):
        d = 1
        m += 1
    if m > 12:
        m = 1
        y += 1
    return f"{y}-{m:02}-{d:02}"

def day_of_week(year: int, month: int, day: int) -> str:
    """Return weekday string for a given date using Sakamoto's algorithm."""
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y = year
    if month < 3:
        y -= 1
    w = (y + y//4 - y//100 + y//400 + t[month-1] + day) % 7
    return ['sun','mon','tue','wed','thu','fri','sat'][w]

def valid_date(date_str: str) -> bool:
    """Return True if date_str is a valid date in YYYY-MM-DD format."""
    parts = date_str.split('-')
    if len(parts) != 3:
        return False
    try:
        y, m, d = map(int, parts)
        # Year must be 4 digits
        if y < 1000 or y > 9999:
            return False
        if m < 1 or m > 12:
            return False
        if d < 1 or d > mon_max(m, y):
            return False
        return True
    except ValueError:
        return False

def day_count(start_date: str, end_date: str) -> int:
    """Count the number of weekend days between start_date and end_date inclusive."""
    count = 0
    current = start_date
    while current <= end_date:
        y, m, d = map(int, current.split('-'))
        if day_of_week(y, m, d) in ['sat','sun']:
            count += 1
        current = after(current)
    return count

def usage():
    """Print usage message and exit."""
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

if __name__ == "__main__":
    # Check number of arguments
    if len(sys.argv) != 3:
        usage()

    start_date, end_date = sys.argv[1], sys.argv[2]

    # Ensure both dates are valid
    if not valid_date(start_date) or not valid_date(end_date):
        usage()

    # Swap dates if start_date > end_date
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    weekends = day_count(start_date, end_date)
    print(f"The period between {start_date} and {end_date} includes {weekends} weekend days.")

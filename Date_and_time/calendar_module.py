'''
Task: Given a date in MM DD YYYY format, find and print the day of the week in capital letters.
Input: A single line with month, day, year space-separated (e.g. "08 05 2015")
Output: The day name in uppercase (e.g. "WEDNESDAY")
'''

import calendar

# Read month, day, year from input
month, day, year = map(int, input().split())

# Get the day of the week as an integer (0=Monday, 6=Sunday)
day_of_week = calendar.weekday(year, month, day)

# Convert integer to day name and print in uppercase
print(calendar.day_name[day_of_week].upper())

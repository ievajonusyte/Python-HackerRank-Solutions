#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

'''
Task: Given two timestamps in "Day DD Mon YYYY HH:MM:SS +XXXX" format,
print the absolute difference between them in seconds.
Input: First line is number of test cases T. Each test case has 2 lines (t1, t2).
Output: Absolute time difference in seconds for each test case.
'''

def time_delta(t1, t2):
    # We define a function that takes two timestamps as strings

    # We define the format template used to parse the timestamps:
    # %a - weekday name (Sun, Mon...)
    # %d - day number (01, 02...)
    # %b - abbreviated month name (Jan, May...)
    # %Y - full year (2015)
    # %H:%M:%S - hours, minutes, seconds
    # %z - timezone offset (+0530, -0700...)
    fmt = '%a %d %b %Y %H:%M:%S %z'

    # We convert the strings t1 and t2 into datetime objects using our format. strptime = "string parse time"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)

    # dt1 - dt2 - subtracts one time from the other - returns a timedelta object
    # .total_seconds() - converts the difference into seconds (e.g. 25200.0)
    # abs() - ensures the result is always a positive number
    # int() - removes the decimal point (25200.0 -> 25200)
    # str() - converts to a string, because fptr.write() requires a string
    return str(int(abs((dt1 - dt2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

'''
Task:
You are given T strings. For each string, check whether it is a valid rregex expression.
Print True if it is valid, False if it is not.

Sample Input:
2
.*\+
.*+

Sample Output:
True
False

Explanation:
.*\+ : Valid regex.
.*+: Has the error multiple repeat. Hence, it is invalid.
'''

import re

T = int(raw_input())
# Read one line of input and convert it to an integer
# raw_input() reads input as a plain string (Python 2 version of input())
# int() converts that string to a number - this is the number of test cases
for _ in range(T):
    # Loop T times - once for each test case, _ means we don't need the loop counter variable
    s = raw_input()
    # Read the next line of input and store it as string s
    try:
        re.compile(s)
        # Try to compile string s as a regular expression pattern
        # re.compile() checks if the pattern is valid regex syntax
        # It does NOT search anything - just checks if the pattern is valid
        print(True)
    except (re.error, SyntaxError):
        # If re.compile(s) failed, one of two errors is caught:
        # re.error - standard Python error for invalid regex pattern
        # SyntaxError - Python 2 raises this for some invalid patterns
        print(False)


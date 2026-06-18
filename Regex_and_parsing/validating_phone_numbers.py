"""
Validating Phone Numbers:
a valid mobile number is a ten digit number starting with 7, 8 or 9.
For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.
"""

import re

n = int(input()) # reads how many numbers will follow

for _ in range(n): # loops exactly input times
    number = input() # reads one number per loop iteration
    if re.match(r'^[789]\d{9}$', number):
        #r means raw prefix,take this string exactly as typed, no special treatment for backslashes
        #^start of string
        #[789]first digit must be 7, 8, or 9
        #/d{9}exactly 9 more digits after that
        #$end of string
        print("YES")
    else:
        print("NO")

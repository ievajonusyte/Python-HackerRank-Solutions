"""
Validating Phone Numbers
A valid mobile number is a ten digit number starting with 7, 8 or 9.
"""

import re

n = int(input()) # reads how many numbers will follow

for _ in range(n): # loops exactly input times
    number = input() # reads one number per loop iteration
    if re.match(r'^[789]\d{9}$', number):
        #^start of string,
        #[789]first digit must be 7, 8, or 9
        #/d{9}exactly 9 more digits after that
        #$end of string
        print("YES")
    else:
        print("NO")

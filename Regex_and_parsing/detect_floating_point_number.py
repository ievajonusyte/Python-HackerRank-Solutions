import re

'''
Given T strings, check if each one is a valid floating point number.
A valid float must:
- optionally start with +, - or .
- contain exactly one . symbol
- have at least 1 digit after the decimal point
- not raise any exceptions when converted with float()
Print True if valid, False otherwise.
'''

t = int(input())
for _ in range(t):
    n = input()
    print(bool(re.match(r'^[+-]?\d*\.\d+$', n)))
    
    # ^ start of string
    # [+-]? optionally starts with + or -
    # \d* zero or more digits before the dot
    # \. exactly one literal dot
    # \d+ at least one digit after the dot
    # $ end of string

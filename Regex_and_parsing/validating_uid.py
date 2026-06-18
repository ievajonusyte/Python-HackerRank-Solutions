import re

'''
Validate employee UIDs for ABCXYZ company.
A valid UID must:
- contain at least 2 uppercase letters (A-Z)
- contain at least 3 digits (0-9)
- contain only alphanumeric characters (a-z, A-Z, 0-9)
- have no repeating characters
- be exactly 10 characters long
Print "Valid" or "Invalid" for each UID.
'''

t = int(input())
for _ in range(t):
    uid = input()
    if (len(uid) == 10
            and re.search(r'[A-Z]{2,}', uid) # contain at least 2 uppercase letters 
            and re.search(r'\d{3,}', uid) # contain at least 3 digits
            and re.match(r'^[a-zA-Z0-9]+$', uid) # contain only alphanumeric characters
            and len(uid) == len(set(uid))): # no repeating characters
        print("Valid")
    else:
        print("Invalid")

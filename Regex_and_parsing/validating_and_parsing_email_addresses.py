import email.utils
import re

'''
Given n name and email address pairs, print only the pairs with valid email addresses.
A valid email address must:
- follow the format: username@domain.extension
- username starts with a letter, followed by letters, digits, ., - or _ only
- domain and extension contain only letters
- extension is 1, 2, or 3 characters long
Print valid pairs in the original format: name <email>
'''

n = int(input())
for _ in range(n):
    line = input()
    name, addr = email.utils.parseaddr(line)  # splits "DEXTER <dexter@hotmail.com>" into ("DEXTER", "dexter@hotmail.com")
    if re.match(r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', addr):
        # ^[a-zA-Z] username must start with a letter, [a-zA-Z0-9._-]* after the first letter, username can contain any mix of letters, digits, . - _., * means zero or more of these, @ symbol required between username and domain, [a-zA-Z]+ domain contains only letters, at least one. No digits or special characters allowed, \. literal dot between domain and extension. Backslash is needed because . alone in regex means "any character" - \. means specifically a dot, [a-zA-Z]{1,3}$ extension contains only letters, and must be 1, 2, or 3 characters long. $ means end of string, nothing can come after.
        print(email.utils.formataddr((name, addr)))  # formats back to "DEXTER <dexter@hotmail.com>"

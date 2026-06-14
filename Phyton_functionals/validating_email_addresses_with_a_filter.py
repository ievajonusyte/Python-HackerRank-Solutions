import re
'''
Here's the task in plain English:

Validating Email Addresses with Filter
You are given a list of email addresses. Your task is to print only the valid ones, sorted in alphabetical order.
A valid email must follow these rules:

It must follow the format: username@websitename.extension
The username can only contain letters, digits, dashes, and underscores
The website name can only contain letters and digits
The extension can only contain letters
The extension can be at most 3 characters long

Input
The first line contains an integer n - the number of email addresses. Each of the next n lines contains one email string.
Output
Print a list of valid email addresses in alphabetical order.
'''

def fun(s):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$' # return True if s is a valid email, else return False
    return bool(re.match(pattern, s))  # match returns None if no match, so wrap in bool

def filter_mail(emails):
    return list(filter(fun, emails))  # keep only emails where fun() returns True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

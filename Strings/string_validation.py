'''
Task: Check if a string contains:

Any alphanumeric characters
Any alphabetical characters
Any digits
Any lowercase characters
Any uppercase characters

Print True or False for each check.
Example:

Input: qA2
Output:

True  (has alphanumeric)
True  (has alphabetical)
True  (has digits)
True  (has lowercase)
True  (has uppercase)
'''

if __name__ == '__main__':
    s = input()
    
    #any(...) returns True if at least one element in the sequence is True, we check each character c in the string s
    
    print(any(c.isalnum() for c in s))   # Any alphanumeric? 
    print(any(c.isalpha() for c in s))   # Any alphabetical?
    print(any(c.isdigit() for c in s))   # Any digits?
    print(any(c.islower() for c in s))   # Any lowercase?
    print(any(c.isupper() for c in s))   # Any uppercase?

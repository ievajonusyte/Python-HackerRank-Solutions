'''
Verify whether a credit card numbers are valid or not. 

A valid credit card from ABCD Bank has the following characteristics:
It must start with a 4, 5 or 6.
It must contain exactly 16 digits.
It must only consist of digits (0-9).
It may have digits in groups of 4, separated by one hyphen "-".
It must NOT use any other separator like ' ', '_', etc.
It must NOT have 4 or more consecutive repeated digits.

Input Format
The first line of input contains an integer N.
The next N lines contain credit card numbers.

Constraints
0 < N < 100

Output Format
Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'.
Do not print the quotes.
'''

import re

n = int(input())
format_pattern = r'^[456]\d{3}(\d{12}|-\d{4}-\d{4}-\d{4})$' 
# start with 4, 5, or 6, then 3 more digits to finish the first group of 4, then either 12 plain digits in a row, OR three more groups of 4 digits each starting with a hyphen
repeat_pattern = r'(\d)\1{3,}'# grab one digit, then check if that exact same digit shows up 3 or more times immediately after it. So it catches things like 1111 or 99999, where a digit repeats 4+ times in a row

for _ in range(n):
    card = input()

    if re.match(format_pattern, card):
        stripped = card.replace('-', '')
        # Make a copy of the card number with all hyphens deleted. So "4253-6258-7961-5786" becomes "4253625879615786". We need this because a repeat could span across where a hyphen used to be (like ...1111-2222...), and we want to catch that too
        if re.search(repeat_pattern, stripped):
            #search the hyphen-free version anywhere for 4+ repeated digits in a row. re.search looks through the whole string (not just the start, like re.match does), since the repeat could occur anywhere in the number
            print('Invalid')
        else:
            print('Valid')
    else:
        print('Invalid')

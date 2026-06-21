'''
A valid postal code P have to fulfil both below requirements:
1. P must be a number in the range from 100000 to 999999 inclusive.
2. P must not contain more than one alternating repetitive digit pair.

Alternating repetitive digits are digits which repeat immediately after
the next digit. In other words, an alternating repetitive digit pair is
formed by two equal digits that have just a single digit between them.

For example:
121426 - Here, 1 is an alternating repetitive digit.
523563 - Here, NO digit is an alternating repetitive digit.
552523 - Here, both 2 and 5 are alternating repetitive digits.

Your task is to provide two regular expressions regex_integer_in_range and
regex_alternating_repetitive_digit_pair. Where:
regex_integer_in_range should match only integers range from 100000 to 999999 inclusive
regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.
'''

regex_integer_in_range = r"^[1-9]\d{5}$" 
# start of string, then one digit that is 1 through 9, then exactly 5 more digits, then end of string

regex_alternating_repetitive_digit_pair = r"(.)(?=.\1)" 
# grab one character, then check if there is any character right after it, followed by that same first character again

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# bool(re.match(regex_integer_in_range, P)) - tries to match the range pattern against P from the start. If it matches, this becomes True; if not, False.
# len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2 - finds every occurrence of the alternating-pair pattern in P, counts how many there are, and checks if that count is less than 2 (so 0 or 1 is fine).
# Since they are joined with and, the final printed result is True only if both conditions are true: the postal code is properly formatted and it doesn't have more than one alternating repetitive digit pair. Otherwise it prints False.

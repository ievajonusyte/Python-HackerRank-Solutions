'''
Task: You are given a string, and you have to validate whether it is a
valid Roman numeral. If it is valid, print True. Otherwise, print False.
Try to create a regular expression for a valid Roman numeral.

Input Format: a single line of input containing a string of Roman characters.

Output Format:a single line containing True or False according to the
instructions above.

Constraints: the number will be between 1 and 3999 (both included).

Sample Input:CDXXI

Sample Output:True
'''

regex_pattern = r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
# M{0,3}
# Thousands place. M can appear zero to three times (covers 1000 to 3000).

# (CM|CD|D?C{0,3})
# Hundreds place. Either CM (900), or CD (400),
# or an optional D followed by zero to three C's (covers 0, 100, 200, 300,
# 500, 600, 700, 800 depending on whether D and how many C's are present).

# (XC|XL|L?X{0,3})
# Tens place. Same shape as hundreds, but with X, L, C instead of C, D, M.

# (IX|IV|V?I{0,3})
# Ones place. Same shape again, but with I, V, X instead of X, L, C.


''' 
re.match checks the pattern against the input string starting from
the beginning. bool() converts the match object (or None) into
True or False. str() converts that boolean into the string "True"
or "False".
'''
import re
print(str(bool(re.match(regex_pattern, input()))))

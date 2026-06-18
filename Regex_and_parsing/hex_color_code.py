import re

'''
Given N lines of CSS code, find and print all valid HEX color codes.
A valid HEX color code:
- starts with #
- followed by exactly 6 or 3 hex digits (0-9, A-F, a-f), 6 checked first
- must appear after a colon (inside a CSS value, not a selector)
Print each valid code on a separate line, in order of occurrence.
'''

n = int(input()) # Reads how many CSS lines will follow and converts it to an integer
for _ in range(n): # Loops exactly n times, once per CSS line. _ is used because we don't need the loop counter
    line = input() # Reads one CSS line per iteration
    if ':' in line: # Checks if the line contains a colon. Lines without : are CSS selectors like #BED or #Cab  we skip those entirely
        value_part = line.split(':', 1)[1]  # everything after the first colon
        matches = re.findall(r'#(?:[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})(?!\w)', value_part) # Searches value_part for all valid hex color codes and returns them as a list. The regex tries 6 digits first, then 3, and rejects anything followed by a non-hex character
        for match in matches: # Loops through all found hex codes and prints each one on a separate line
            print(match)

import re

'''Task: Given a string S and a substring k, find all occurrences of k in S,
including overlapping ones. Print the start and end index of each match
as a tuple (start_index, end_index). If no match is found, print (-1, -1).
'''

S = input()
k = input()


pattern = re.compile('(?=' + k + ')')
# regex pattern to lookahead. A lookahead checks if k is
# present at a position without consuming the characters, so the next
# search position can start right after this one instead of skipping
# past the whole match. This is what allows overlapping matches to be found.

matches = list(pattern.finditer(S))
# Use finditer to scan S and find every position where the lookahead
# pattern matches. Convert the result to a list so we can check if it
# is empty and loop through it. 

if not matches:
    print((-1, -1))
else:
    for match in matches: # Go through each match that was found
        start_index = match.start() # Get the starting index of this match
        end_index = start_index + len(k) - 1 
        # Calculate the end index. Since the lookahead does not consume
        # characters, match.end() would just equal match.start(), so we
        # calculate the real end index manually by adding the length of k
        # and subtracting 1 (to get the index of the last character, not
        # one past it)
        print((start_index, end_index))  # Print the result as a tuple in the required format

#!/bin/python3

import math
import os
import random
import re
import sys

'''
The matrix script is a N X M grid of strings.
It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

To decode the script, it needs to read each column and select only the
alphanumeric characters and connect them. Neo reads the column from top to
bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the
decoded script, then replace them with a single space ' ' for better
readability.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format: the first line contains space-separated integers N (rows) and M (columns)
respectively. The next N lines contain the row elements of the matrix script.

Constraints: 0 < N, M < 100

Output Format: print the decoded matrix script.
'''


first_multiple_input = input().rstrip().split()
# Read one line of input, remove any trailing whitespace or newline, then split it into a list of separate pieces based on spaces. This line has two numbers on it, like "7 3", so it becomes ["7", "3"]

n = int(first_multiple_input[0])
# Take the first piece from that list ("7") and convert it to an integer
m = int(first_multiple_input[1])
# Take the second piece from that list ("3") and convert it to an integer

matrix = []
# Create an empty list that will hold all the rows of the matrix
for _ in range(n):# Repeat the next block n times, once for each row
    matrix_item = input() # Read one line of input. This is one row of the matrix, as a string
    matrix.append(matrix_item) # Add that row string onto the end of the matrix list

decoded = '' # Create an empty string that we'll build up character by character as we read the matrix.
for col in range(m): # Loop over every column index, starting from 0 up to m-1, going left to right.
    for row in range(n): # For each column, loop over every row index, starting from 0 up to n-1, going top to bottom.
        decoded += matrix[row][col] # Grab the single character sitting at this row and this column, and stick it onto the end of decoded. Because column is the outer loop and row is the inner loop, this reads all the characters down one full column before moving to the next column.

result = re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', decoded)
# Search through decoded and replace any stretch of symbols or spaces with a single space, but only when that stretch has a letter or digit right before it and a letter or digit right after it. 
print(result) # Print the final decoded message.
    

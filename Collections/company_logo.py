#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter # # Counter is a special dictionary that counts things automatically
# e.g. Counter("aabbb") - {'a':2, 'b':3}

'''
Task: Given a string, find the 3 most common characters. 
Print each with its count, sorted by count descending. If counts are equal, sort alphabetically.
'''

if __name__ == '__main__':
    s = input() # read the input string from user
    
    counts = Counter(s)
    # count how many times each character appears in s

    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    # counts.items() gives pairs of (character, count)
    # e.g. [('a',2), ('b',3), ('c',2), ('d',1), ('e',1)]
    #
    # sorted() sorts that list using the key function
    #
    # lambda x: (-x[1], x[0]) means:
    #   x[1] = the count  -  -x[1] means sort by count DESCENDING (bigger first)
    #   x[0] = the char   - sort alphabetically if counts are equal
    #
    # result: [('b',3), ('a',2), ('c',2), ('d',1), ('e',1)]
    #          b first (count 3), then a before c (same count, alphabetical)
    for char, count in sorted_chars[:3]:
        # [:3] means take only the first 3 items from the sorted list
        # loop through each (character, count) pair
        print(char, count)
        # print character and its count separated by space
        # output:
        # b 3
        # a 2
        # c 2

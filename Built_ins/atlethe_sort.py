#!/bin/python3

import math
import os
import random
import re
import sys

'''
Task summary: You have a table of N athletes, each with M attributes (age, height, weight, etc.).
Sort the entire table by the K-th column (0-indexed), and print the result.
Tie rule: if two athletes have the same value in column K, keep the one that appeared first in the input first.

Example: K=1 means sort by the 2nd column (age). Every row moves together you're just reordering the rows, not the values within a row.
'''

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0]) # number of athletes (rows)
    m = int(nm[1]) # number of attributes (columns)
    arr = []
    
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input()) # column index to sort by
    arr = sorted(arr, key=lambda row: row[k])
    
    # key= tells Python what value to use when comparing rows 
    # lambda row: row[k] means: for each row, grab the element at index k
    # sorted() if two rows have the same value at index k, they stay in their original order 
    
    for row in arr:
        print(*row) # print(*row)* unpacks the list, so [5, 24, 176] prints as 5 24 176 

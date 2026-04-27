#!/bin/python3

import math
import os
import random
import re
import sys

# Task: Given an integer n, perform the following conditional actions:
# - If n is odd, print Weird
# - If n is even and in the inclusive range of 2 to 5, print Not Weird
# - If n is even and in the inclusive range of 6 to 20, print Weird
# - If n is even and greater than 20, print Not Weird

if __name__ == '__main__':
    n = int(input().strip())
# check if n is odd
    if n % 2 != 0:
        print("Weird")
    else:
        # n is even
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:  # greater than 20
            print("Not Weird")

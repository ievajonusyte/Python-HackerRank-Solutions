'''
Task:
Given an integer, n, and n space-separated integers as input, create a tuple,t, of those n integers. 
Then compute and print the result of hash(t).
Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
Input Format
The first line contains an integer,n , denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t.

Output Format

Print the result of hash(t).

HackerRanks judge for this task expects Python 2 output, so the code is written in Python 2.
Why does Python 2 pass but Python 3 doesn't?
hash() works differently in each version:

Python 2 — always gives the same result → 3713081631934410656
Python 3 — result is random every run (for security reasons)
'''



n = int(input())
integer_list = map(int, raw_input().split()) # raw_input() is Python 2's version of input()
t = tuple(integer_list) # converts [1, 2] into a tuple (1, 2)
print(hash(t))

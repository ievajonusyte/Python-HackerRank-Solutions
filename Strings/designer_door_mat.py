'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N X.M (N is an odd natural number, and M is 3 times N .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
---------.|.---------  = Row 1 (21 characters wide)
------.|..|..|.------  = Row 2 (21 characters wide)
---.|..|..|..|..|.---  = Row 3 (21 characters wide)
-------WELCOME-------  = Row 4 (21 characters wide)
---.|..|..|..|..|.---  = Row 5 (21 characters wide)
------.|..|..|.------  = Row 6 (21 characters wide)
---------.|.---------  = Row 7 (21 characters wide)

7 rows total (N=7)
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

Input Format:
A single line containing the space separated values of N and M.

Constraints:
5 < N < 101
15 < M < 303
'''

n, m = map(int, input().split())

# Top half - growing pattern
for i in range(n // 2):
    pattern = ".|." * (2 * i + 1) # 2*i + 1 because we want odd numbers: 1, 3, 5, 7, 9...
    print(pattern.center(m, '-'))

# Middle - WELCOME
print("WELCOME".center(m, '-'))

# Bottom half - shrinking pattern (mirror of top)
for i in range(n // 2 - 1, -1, -1): # i goes 2, 1, 0 backwards
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(m, '-'))

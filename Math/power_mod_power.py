'''
Task: Given 3 integers (a, b, m), print two lines - pow(a,b) then pow(a,b,m)
Input: 3 numbers, each on a separate line
Constraints: a, b between 1-10, m between 2-1000
Output: Two lines - plain power, then power mod m
'''

a = int(input())
b = int(input())
m = int(input())
print(pow(a, b))
print(pow(a, b, m))

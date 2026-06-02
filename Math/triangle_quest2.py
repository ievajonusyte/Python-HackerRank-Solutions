'''
The task is to print a palindromic triangle of size N
N: row 1 is 1, row 2 is 121, row 3 is 12321, and so on up to N

For ex. N=5
1
121
12321
1234321
123454321
'''

for i in range(1,int(input())+1):
    print(((10**i//9)**2))

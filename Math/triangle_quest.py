'''
The task is to print a numeric triangle with N−1, N−1 rows, where row 1 is 1, row 2 is 22, row 3 is 333, and so on up to N-1. 
You must do it with only one loop and one print statement, using arithmetic only, and no strings.
So for input 5, the output should be:
1
22
333
4444
'''

for i in range(1,int(input())): 
    print((10**i // 9) * i)
    
#10**i // 9 makes 1, 11, 111, 1111, ...
#Multiplying by i turns that into 1, 22, 333, 4444

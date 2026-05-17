'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
'''
def swap_case(s):
    return s.swapcase() # built-in Python method that swaps all cases
   
    
if __name__ == '__main__':
    s = input() # read user input
    result = swap_case(s) # call the function, store result
    print(result)

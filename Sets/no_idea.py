'''
Read n and m.
Read the array of n integers.
Read set A.
Read set B.
Start happiness = 0.
For each element x in array:
If x in A, increase happiness.
Else if x in B, decrease happiness.
Print happiness at the end.
'''

n, m = map(int, input().split()) # reads one full line as a string, breaks the string into pieces by spaces, converts each piece to an int, unpacks that pair into two variables
arr = list(map(int, input().split())) # input().split() reads a line like 1 5 3 to [1, 5, 3], .map(int, ...) converts each to integers (1, 5, 3), .list(...) turns that into a list [1, 5, 3], .arr now holds all n integers from the array in order
A = set(map(int, input().split())) # set of numbers you like
B = set(map(int, input().split())) # set of numbers you dislike

happiness = 0 # starts your happiness score at 0
for x in arr: # goes through each element of the array one by one
    if x in A:
        happiness += 1 # Checks whether the current number is in the like set A. If yes, happiness += 1 increases happiness by 1
    elif x in B:
        happiness -= 1 # Only checked if the first if was false. If the number is in the dislike set B, happiness -= 1 decreases happiness by 1

print(happiness)

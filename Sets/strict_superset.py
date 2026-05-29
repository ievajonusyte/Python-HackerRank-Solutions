'''
Superset is the opposite of subset. If A is a superset of B, it means B is a subset of A  A contains everything in B.
A = 1, 2, 3, 4, 5
B = 1, 2, 3
A is superset of B? YES  A contains all of B

What is a STRICT Superset?
A is a strict superset of B if:
A contains all elements of B 
A has at least one extra element that B does NOT have 
A = 1, 3, 4
B = 1, 3     A is STRICT superset (4 is extra)
B = 1, 3, 4  A is NOT strict superset (they are equal)
B = 1, 3, 5  A is NOT strict superset (5 not in A)

The Problem:
You have one big set A
You have N other sets
Check if A is a strict superset of ALL N sets
If yes print True, otherwise print False
'''

A = set(map(int, input().split())) # Read set A
n = int(input()) # Read how many other sets

result = all(A > set(map(int, input().split())) for _ in range(n))
'''
input().split() Read line and cut into piecesmap
(int, ...) Convert strings to numbers
set(...) Make it a set
A > other Check strict superset
for _ in range(n) Repeat n times
all(...) True only if everything is True
'''

print(result)

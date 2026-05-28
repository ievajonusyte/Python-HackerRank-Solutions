'''
Task: Set Mutations
You have a set A and N other sets that perform mutation operations on A.
Goal: Execute all operations on set A, then print the sum of elements in A.

Operations:
.update()Adds all elements from other set into A
.intersection_update()Keeps only common elements in A
.symmetric_difference_update() Keeps elements in either but not both
.difference_update() Removes elements from A that are in other set
'''

n = int(input())  # how many elements in A
A = set(map(int, input().split())) # create set A , input().split()reads numbers as a list ['1','2','3'...], map(int, ...) converts to integers[1, 2, 3...], set(...) converts to a set {1, 2, 3...}

N = int(input())  # how many operations to perform
for _ in range(N): # repeat N times
    op, length = input().split() # read operation name & size
    other = set(map(int, input().split())) # read the other set
    
    if op == "update":
        A.update(other) # A = A + other
    elif op == "intersection_update":
        A.intersection_update(other) # A = only common elements
    elif op == "symmetric_difference_update":
        A.symmetric_difference_update(other) # A = elements NOT in both
    elif op == "difference_update":
        A.difference_update(other)  # A = remove other from A

print(sum(A))  # add all remaining elements in A

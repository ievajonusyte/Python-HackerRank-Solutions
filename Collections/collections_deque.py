from collections import deque

'''
Task: Perform append, pop, popleft, appendleft operations on a deque and print the final result.
'''

n = int(input())
d = deque()

for _ in range(n):
    line = input().split()
    op = line[0]
    if op == 'append':
        d.append(int(line[1]))
    elif op == 'appendleft':
        d.appendleft(int(line[1]))
    elif op == 'pop':
        d.pop()
    elif op == 'popleft':
        d.popleft()

print(*d) # unpacks the deque and prints elements space separated

from collections import defaultdict

'''
Given n words in group A and m words in group B.
For each word in B, print all positions (1-indexed) where it appears in A.
If not found, print -1.
'''
n, m = map(int, input().split()) # Read n (group A size) and m (group B size)

index = defaultdict(list) # Empty dictionary where every new key auto-gets an empty list
for i in range(n):
    word = input()
    index[word].append(i + 1)
# Read n words one by one. For each word, record its position (1-indexed) into the index

for _ in range(m):
    word = input()
    # Read each group B query word one by one
    if word in index:
        print(*index[word])
    else:
        print(-1)
        # Look it up in the index. If found, print all positions, if not found, print -1

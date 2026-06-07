from collections import OrderedDict

'''
Task: You get a list of words. Some words repeat.
Print:
how many unique words there are
how many times each unique word appears, in the order they first showed up

From the example:

bcdef, abcdefg, bcde, bcdef
unique words: 3 (bcdef, abcdefg, bcde)
bcdef appeared 2 times, abcdefg 1 time, bcde 1 time
output: 3 then 2 1 1
'''

n = int(input()) # Read how many words are coming
od = OrderedDict() # Create empty OrderedDict to store word

for _ in range(n):
    word = input() # Loop n times, read one word each time
    if word in od:
        od[word] += 1
    else:
        od[word] = 1
    # If word already exists, add 1 to its count, if new word, set count to 1

print(len(od)) # Print how many unique words there are
print(*od.values()) # od.values() gives all counts in first-appearance order, * unpacks them so they print space-separated like 2 1 1

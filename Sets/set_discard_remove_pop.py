'''
The Problem:

Start with a set of integers
Execute N commands: pop, remove, or discard
Print the sum of remaining elements

Three Operations:
.pop()

Removes and returns an arbitrary element
Raises KeyError if set is empty
No parameter needed

.remove(x)

Removes the specific element x
Raises KeyError if x doesn't exist
Use when you're certain the element exists

.discard(x)

Removes the specific element x
Does NOT raise error if x doesn't exist (fails silently)
Safer alternative to .remove()

Example:
Starting set: {1, 2, 3, 4, 5, 6, 7, 8, 9}
Command          Action                    Set After
-------          ------                    ---------
pop              Remove arbitrary (e.g. 1) {2, 3, 4, 5, 6, 7, 8, 9}
remove 9         Remove 9                  {2, 3, 4, 5, 6, 7, 8}
discard 9        Try remove 9 (not there)  {2, 3, 4, 5, 6, 7, 8}
discard 8        Remove 8                  {2, 3, 4, 5, 6, 7}
remove 7         Remove 7                  {2, 3, 4, 5, 6}
pop              Remove arbitrary (e.g. 2) {3, 4, 5, 6}
discard 6        Remove 6                  {3, 4, 5}
remove 5         Remove 5                  {3, 4}
pop              Remove arbitrary (e.g. 3) {4}
discard 5        Try remove 5 (not there)  {4}

Final sum: 4
'''

n = int(input()) # read the first line, convert to integral
s = set(map(int, input().split())) # reads, splits by spaces, converts each string to integer, creates a set

num_commands = int(input()) # reads number of commands

for _ in range(num_commands): # loop through commands, _ is used because we don't need the loop counter value
    command = input().split() 
    
    if command[0] == 'pop':
        s.pop() # if command is "pop", remove an arbitrary element from set, no parameter needed
    elif command[0] == 'remove'
        s.remove(int(command[1])) # if command is "remove X"  converts it to integer, remove that specific element from the set, raises error if element doesn't exist
    elif command[0] == 'discard':
        s.discard(int(command[1])) # if command is "discard X" converts string to integer,remove that specific element from the set, no error if element doesn't exist

print(sum(s)) # adds all remaining elements in the set, prints the result

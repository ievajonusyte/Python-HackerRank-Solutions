'''
A hotel has tourists. The tourists consist of:
One Captain gets a private room alone
Several families each family has exactly K members, and all members of a family share one room
Mr. Anant has a list of all room numbers (one number per person).

Your job is to find the Captain's room number.
'''

n = int(input()) # Read K
rooms = list(map(int, input().split())) # Read all room numbers as a list

print((sum(set(rooms)) * n - sum(rooms)) // (n - 1)) # sum(set(rooms)) * n fake total if captain also had K people, - sum(rooms) subtract real total, // (n-1) divide to isolate captain's room

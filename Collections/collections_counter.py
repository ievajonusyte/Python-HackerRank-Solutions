from collections import Counter
'''
Raghu has a shop with X shoes of various sizes.
N customers each want a specific size and will pay a price for it.
If the size is available, sell it and earn the money. Sum total earnings.
'''

X = int(input()) # Read the number of shoes
shoes = Counter(map(int, input().split())) # Read all shoe sizes as integers, then Counter counts how many of each size exist

N = int(input()) # Read how many customers there are
earned = 0 # Running total of money earned, starts at 0

for _ in range(N): # Loop N times, once per customer
    size, price = map(int, input().split()) # Each customer line has two numbers; their desired size and how much they'll pay
    if shoes[size] > 0: # Check if that size is still in stock. Counter returns 0 for missing keys automatically, so no KeyError risk
        earned += price
        shoes[size] -= 1
    #If in stock: add the price to earnings, remove one shoe of that size from stock
print(earned) # Print the total


from collections import OrderedDict

'''
Task: You have a list of items with prices. 
Print each unique item name and its net_price,in order of first occurrence.
'''

n = int(input()) # Read number of items
od = OrderedDict() # Create an empty OrderedDict to store item name - total price

for _ in range(n):
    line = input().split() # Loop n times, read each line and split into a list
    price = int(line[-1]) # Last element is always the price. line[-1] = '12', convert to int
    name = ' '.join(line[:-1]) # Everything except the last element is the name. line[:-1] = ['BANANA', 'FRIES'], join back with space
    if name in od:
        od[name] += price
    else:
        od[name] = price
    # If item already exists, add to its total, if new, create it with current price
for name, price in od.items():
    print(name, price)
    # Loop through OrderedDict and print each item with its total price, in the order they first appeared

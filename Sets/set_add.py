'''
The Problem:
Rupal has N country stamps
Some countries appear multiple times (duplicates)
We need to count only the distinct countries
The Solution:

Read Input: Get the total number of stamps (N = 7)
Create a Set: countries = set() - an empty set to store unique country names

Sets automatically prevent duplicates!

Add Countries: Use .add() method in a loop

countries.add(country) adds each country to the set
If a country already exists (like "UK" or "France"), the set ignores the duplicate

Count Distinct: len(countries) gives us the number of unique countries

Example:
Input:
7
UK
China
USA
France
New Zealand
UK          ← duplicate
France      ← duplicate

Set after all additions: {'UK', 'China', 'USA', 'France', 'New Zealand'}
Output: 5
'''

# Read the number of stamps
n = int(input())

# Create an empty set to store distinct countries
countries = set()

# Read each country name and add to set
for _ in range(n):
    country = input()
    countries.add(country)

# Print the count of distinct countries
print(len(countries))

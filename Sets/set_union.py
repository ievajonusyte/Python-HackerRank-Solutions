'''
Task:
Students at District College subscribe to English and/or French newspapers.
Goal: Find the total number of unique students who have subscribed to at least one newspaper.

Input:
Two sets of student roll numbers (English subscribers & French subscribers)
A student can appear in both sets

Output: Count of students who have at least one subscription (no duplicates)
'''



n = int(input()) 
english = set(map(int, input().split())) # Read n and the English subscribers into a set
b = int(input())
french = set(map(int, input().split())) # Read b and the French subscribers into a set

print(len(english.union(french))) # Use .union() to combine both sets (duplicates are automatically removed), print the length of the union

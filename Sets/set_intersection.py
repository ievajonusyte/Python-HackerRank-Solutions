'''
Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to both newspapers.
'''


n = int(input())
english = set(map(int, input().split())) # Read n and the English subscribers into a set
b = int(input())
french = set(map(int, input().split())) # Read b and the French subscribers into a set

print(len(english.intersection(french))) # Use .intersection() to find number of students who have subscribed to both newspapers, print the length of the union 

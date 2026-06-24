import numpy
'''
Your task is to print an array of size N X M with its main diagonal elements as 1s and 0s everywhere else.
'''

numpy.set_printoptions(legacy='1.13') # HackerRank's expections

n, m = map(int, input().split()) # reads the line and converts both numbers to integers

print(numpy.eye(n, m)) # builds an NxM array with 1s along the main diagonal and 0s everywhere else

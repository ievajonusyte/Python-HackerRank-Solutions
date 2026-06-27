import numpy
'''
You are given two arrays: A and B.
Your task is to compute their inner and outer product.

Input Format
The first line contains the space separated elements of array A.
The second line contains the space separated elements of array B.

Output Format
First, print the inner product.
Second, print the outer product.
'''


A = numpy.array(input().split(), dtype=int)
B = numpy.array(input().split(), dtype=int)

print (numpy.inner(A, B))
print (numpy.outer(A, B))

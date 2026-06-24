import numpy
'''
You need to convert the input list to a float array, then reverse it using slicing.
'''
def arrays(arr):
    a = numpy.array(arr, float)
    return a[::-1]#  reverses the array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

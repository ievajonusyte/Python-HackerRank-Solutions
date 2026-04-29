
'''
You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k  is not equal to n. Here, 0<=i<=x;0<=j<=y;0<=k<=z.
Please use list comprehensions rather than multiple loops, as a learning exercise.
'''


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input()) # This is what determines which sum to exclud

result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
# for i in range(x + 1) - generates i from 0 to x (inclusive)
# for j in range(y + 1) - generates j from 0 to y (inclusive)
# for k in range(z + 1) - generates k from 0 to z (inclusive)
# if i + j + k != n - filters out coordinates where the sum equals n
# [[i, j, k] ...] - creates a list of coordinate lists

print(result)

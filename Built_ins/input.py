'''
Task: Verify if a polynomial P(z) equals k.

Input:
  - Line 1: z and k (space-separated integers)
  - Line 2: polynomial P as a string (with variable x)

Output:
  - Print True if P(z) = k, otherwise False
'''

# Read z and k from first line
z, k = map(int, input().split())

# Read the polynomial P as a string
P = input()

# Replace x with the value of z, wrapped in parentheses for safety
# This avoids operator precedence issues
P = P.replace('x', '(' + str(z) + ')')

# Evaluate the polynomial using eval()
result = eval(P)

# Check if P(z) equals k and print the result
if result == k:
    print(True)
else:
    print(False)

'''
Task: Check if all integers are positive AND at least one is palindromic.

Input:
  - Line 1: N (count of integers)
  - Line 2: N space-separated integers

Output:
  - Print True if both conditions met, False otherwise

Conditions:
  1. All integers must be positive (greater than 0)
  2. At least one integer must be palindromic
  
Example:

List: 12, 9, 61, 5, 14
All positive? Yes 
Palindromic ones? 9 and 5 (single digits are palindromic) 
Output: True
'''

input() # Read N, but don't store it, just consume the input
numbers = list(map(int, input().split())) # Read and store the list of numbers
print(all(x > 0 for x in numbers) and any(str(x) == str(x)[::-1] for x in numbers)) 
# Check both conditions and print the result in one line

'''
Task:
You are given T test cases. For each test case, you receive two values a and b.
Perform integer division a // b and print the result.
If b is zero, catch the ZeroDivisionError and print the error message.
If a or b cannot be converted to an integer, catch the ValueError and print the error message.
'''

T = int(input()) # Read the number of test cases

for _ in range(T): # Loop T times 
    try:
        a, b = map(int, input().split()) # Try to read two values and convert both to integers
        print(a // b) # If successful, print integer division result
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)

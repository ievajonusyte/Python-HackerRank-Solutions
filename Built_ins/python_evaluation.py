'''
Task:You are given an expression in a line. 
Read that line as a string variable, such as var, and print the result using eval(var).
'''

# Read the expression as a string
expression = input()

# eval() executes the string as Python code
# If the expression is "print(2 + 3)", eval will execute it and print 5
eval(expression)

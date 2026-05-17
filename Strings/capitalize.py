'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
For example, alison heck should be capitalised correctly as Alison Heck.
'''

def solve(s):
    for i in s.split():                  # split "alison heck" - ["alison", "heck"]
        s = s.replace(i, i.capitalize()) # "alison" - "Alison", "heck" - "Heck"
    return s                             # return "Alison Heck"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')   # opens their output file
    s = input()                                   # reads your input
    result = solve(s)                             # calls YOUR function
    fptr.write(result + '\n')                     # writes result to their file
    fptr.close()                                  # closes the file

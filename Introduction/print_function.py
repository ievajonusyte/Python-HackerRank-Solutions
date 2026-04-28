# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following:
# Note that "" represents the consecutive values in between.
# Example n=5
# Print the string 12345.

# Input Format
# The first line contains an integer n.
#Constraints 1<= n <=150



if __name__ == '__main__':
    n = int(input()) # Reads a number from the user
    print(*range(1,1+n), sep='') # Creates a sequence of numbers from 1 to n, The * unpacks the list,  sep='' means print numbers with no space between them

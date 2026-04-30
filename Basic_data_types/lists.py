'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list.

Input Format:
The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands listed above.

Constraints:
The elements added to the list must be integers.
'''




if __name__ == '__main__':
    N = int(input()) # input() reads a line of text from the user,int() converts that text to an integer, N stores the number in variable N
    lst = [] # Creates an empty list [],stores it in variable lst,this is our working list that we'll modify with commands
    
    for _ in range(N): # Loops N times (the underscore _ means "we don't care about the loop counter")
        command = input().split() # input() reads one line from the user (e.g., "insert 1 3"), .split(), splits the line by spaces into a list of words, Example: "insert 1 3" becomes ['insert', '1', '3'], command stores this list
        
        if command[0] == 'insert': # check if command[0] is 'insert'
            i = int(command[1]) # command[1] - gets the second word(the position index)
            e = int(command[2]) # command[2] - gets the third word(the element to insert)
            lst.insert(i, e) # do this code. Inserts element e at position i. Example: [1, 2].insert(1, 3) - [1, 3, 2]   
               
        elif command[0] == 'print':  # Check if command[0] is 'print'
            print(lst) # Shows the list to the user
        elif command[0] == 'remove': # Check if command[0] is 'remove'
            e = int(command[1]) # e = the VALUE to remove
            lst.remove(e) # Do this code, removes the first occurrence of the VALUE e
        elif command[0] == 'append': # Check if command[0] is 'append'
            e = int(command[1]) # e = the VALUE to 'append'
            lst.append(e) # Do this code .append(e) - Adds element to the end of the list
        elif command[0] == 'sort': # Check if command[0] is 'sort'
            lst.sort() # Do this code .sort() sorts the list in ascending order. Example: [3, 1, 2].sort() - [1, 2, 3]
        elif command[0] == 'pop': # Do this code. Checks if command[0] is 'pop'
            lst.pop() #  Do this code .pop(). Removes the last element. Example: [1, 2, 3].pop() - list becomes [1, 2]
        elif command[0] == 'reverse': # Check if command[0] is 'reverse'
            lst.reverse() # Do this code .reverse(). Reverses the order of elements. Example: [1, 2, 3].reverse() - [3, 2, 1]
            
        #List methods - insert(), append(), remove(), sort(), pop(), reverse()

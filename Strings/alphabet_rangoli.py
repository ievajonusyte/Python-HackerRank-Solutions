'''
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------

Function Description

Complete the rangoli function in the editor below.
rangoli has the following parameters:
int size: the size of the rangoli

Returns
string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)

Input Format
Only one line of input containing size, the size of the rangoli.

Constraints
0 < size < 27
'''


def print_rangoli(size):
    import string
    
    if size == 1:
        print('a')
        return
    # Edge case, because with 1 its only one letter a, you dont need to run remaining code
  
    letters = string.ascii_lowercase[:size]
    lines = []
    # string.ascii_lowercase = abcdefghijklmnopqrstuvwxyz, :size = string slicing - it takes the first size characters, lines = [] creates an empty list that will store each row of the rangoli
    
    # Build each line
    for i in range(size):
        # For row i, we go from letter at (size-1) down to (i), then back up to (size-1)
        # Left side: from size-1 down to i+1
        left = [letters[j] for j in range(size-1, size-1-i, -1)]
        # Center: letter at i
        center = [letters[size-1-i]]
        # Right side: from i+1 up to size-1
        right = [letters[j] for j in range(size-i, size)]
        
        # Combine all parts
        row = left + center + right
        line = '-'.join(row)
        lines.append(line)
    
    # Create the full pattern (top + bottom mirror) 
    # lines[-2] means "second from last item", [::-1] means "reverse the list", lines[-2::-1] means "take everything from the second-to-last item to the beginning, reversed"
    all_lines = lines + lines[-2::-1]
    
    # Width is the length of the middle line (widest)
    width = len(all_lines[size-1])
    
    # Print centered
    for line in all_lines:
        print(line.center(width, '-'))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

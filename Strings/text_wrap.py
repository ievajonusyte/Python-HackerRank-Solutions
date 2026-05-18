import textwrap

'''
Task: Wrap a string into a paragraph of width w.
Looking at the example:

Input: ABCDEFGHIJKLIMNOQRSTUVWXYZ with width 4
Output:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

So we need to break the string into chunks of width w.

'''

def wrap(string, max_width):
    return textwrap.fill(string, max_width) # textwrap.fill(string, max_width) automatically wraps the text to the specified width and returns it with newlines

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

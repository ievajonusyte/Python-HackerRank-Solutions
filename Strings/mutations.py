'''
Strings are immutable (cannot be changed directly).
Approach: slice the string and join it back.
Example:
string = "abracadabra"
position = 5, character = 'k'
string[:5] → "abraca"  +  "k"  +  string[6:] → "dabra"
result = "abrackdabra"
'''


def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:] 
    # cut out old character at position, insert new one
 
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

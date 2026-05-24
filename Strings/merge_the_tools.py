'''
Problem Summary:

Split string s into n/k substrings of length k
Each substring should have k consecutive characters
Remove any character that appears multiple times (keep only characters that appear exactly once)
Print each resulting substring on a new line

Example walkthrough:

s = 'AABCADDE', k = 3
Substrings: 'AAB', 'BCA', 'DDE'
After removing duplicates:

'AAB' → 'B' (A appears twice)
'BCA' → 'BCA' (all unique)
'DDE' → '' (D appears twice, E removed due to prior occurrence)

I will use slicing, string[start:end]
start: where to begin (inclusive)
end: where to stop (exclusive - doesn't include this position)
s = 'ABCDEFGH'
k = 3

# First substring (i=0):
s[0*3 : 1*3]  →  s[0:3]  →  'ABC'

# Second substring (i=1):
s[1*3 : 2*3]  →  s[3:6]  →  'DEF'

# Third substring (i=2):
s[2*3 : 3*3]  →  s[6:9]  →  'GH'
'''

def merge_the_tools(string, k):
    # Split string into n/k substrings of length k
    num_substrings = len(string) // k
    
    for i in range(num_substrings):
        # Extract substring of length k
        substring = string[i * k : (i + 1) * k]
        
        # Remove duplicate characters while maintaining order
        seen = set()
        result = []
        
        for char in substring:
            if char not in seen:
                seen.add(char)
                result.append(char)
        
        # Print the result
        print(''.join(result))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
  

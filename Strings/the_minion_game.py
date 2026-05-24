"""
Problem Summary:

String S is given (e.g., "BANANA")
Stuart makes words starting with consonants
Kevin makes words starting with vowels
Each player scores +1 point for each occurrence of their substring in S
Print the winner and their score (or "Draw" if tied)

Key Insight:

Count how many substrings START with a vowel vs START with a consonant
It's about the first letter of each possible substring, not counting letters inside
Counting all possible substrings, not acyual English words
Scoring based on what letter they start with

For each position i in the string, the number of substrings starting at that position is (length - i)
If the character at position i is a vowel, add (length - i) to Kevin's score
If it's a consonant, add to Stuart's score
Compare and print the winner

Example:
String: "IEVA"

Length = 4
Positions: I(0), E(1), V(2), A(3)
Vowels: I, E, A
Consonants: V


Step-by-step calculation:
Position 0: 'I' (vowel) → Kevin gets points

Can make 4 substrings: I, IE, IEV, IEVA
Formula: 4 - 0 = 4
Kevin += 4


Position 1: 'E' (vowel) → Kevin gets points

Can make 3 substrings: E, EV, EVA
Formula: 4 - 1 = 3
Kevin += 3


Position 2: 'V' (consonant) → Stuart gets points

Can make 2 substrings: V, VA
Formula: 4 - 2 = 2
Stuart += 2


Position 3: 'A' (vowel) → Kevin gets points

Can make 1 substring: A
Formula: 4 - 3 = 1
Kevin += 1


Final Scores:
Kevin (vowels I, E, A): 4 + 3 + 1 = 8 points
Stuart (consonant V): 2 = 2 points
Winner: Kevin 8 🎉

All substrings visualized:

Starting with vowels (Kevin): I, IE, IEV, IEVA, E, EV, EVA, A = 8 total
Starting with consonants (Stuart): V, VA = 2 total
"""
def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0  # vowels
    stuart_score = 0  # consonants
    
    length = len(string)
    
    for i in range(length):
        # Number of substrings starting at position i
        # is (length - i)
        if string[i] in vowels:
            kevin_score += (length - i)
        else:
            stuart_score += (length - i)
    
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

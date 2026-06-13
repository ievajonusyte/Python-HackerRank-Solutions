S = input()

'''
Task: sort string S by custom order:
1. lowercase letters (a to z)
2. uppercase letters (A to Z)
3. odd digits (1, 3, 5, 7, 9)
4. even digits (0, 2, 4, 6, 8)
'''

# Separate characters into four groups
lowercase = sorted(c for c in S if c.islower())
# sorted()loops through every character c in S, keeps only the ones where c.islower() is True, then sorts them. So for "Sorting1234 characters where islower() is True: o, r, t, i, n, gafer sorting: ['g', 'i', 'n', 'o', 'r', 't']
uppercase = sorted(c for c in S if c.isupper())
# keeps only uppercase letters
odd_digits = sorted(c for c in S if c.isdigit() and int(c) % 2 != 0)
# converting it to integer and checking the remainder when divided by 2 is not zero (meaning it's odd)
even_digits = sorted(c for c in S if c.isdigit() and int(c) % 2 == 0)
# keeps only even digits (including 0)
# Join all groups in the required order
print(''.join(lowercase + uppercase + odd_digits + even_digits))

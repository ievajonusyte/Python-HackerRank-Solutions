'''
Task: debug score_words so it returns the correct score.

Rules:
vowels are a, e, i, o, u, y
each word scores 2 if it has an even number of vowels, otherwise 1
total score is the sum of scores for all words

Bug found: the line "++score" does nothing in Python, there is no
increment operator, so the odd-vowel case never added 1 to score.
Fix: replace "++score" with "score += 1"
'''
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


n = int(input())
words = input().split()
print(score_words(words))

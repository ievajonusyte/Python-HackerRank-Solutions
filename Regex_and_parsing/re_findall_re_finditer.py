import re


def find_substrings_between_consonants_with_vowels(input_string):
    """
    Find all substrings that contain 2 or more vowels in a row,
    where the vowel sequence is located between two consonants.
    Return -1 if no match is found.
    """
    pattern = r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])'
    matches = re.findall(pattern, input_string, flags=re.IGNORECASE)
    return matches if matches else [-1]
    # (?<=[qwrtypsdfghjklzxcvbnm]) is a lookbehind, checking the character right before the match is a consonant, without consuming it
    # ([aeiou]{2,}) captures 2 or more consecutive vowels
    # re.IGNORECASE means you don't need to list uppercase letters separately
    # findall returns just the captured group (the vowel sequence) since lookbehind/lookahead aren't part of the match


if __name__ == '__main__':
    s = input()
    results = find_substrings_between_consonants_with_vowels(s)
    for result in results:
        print(result)

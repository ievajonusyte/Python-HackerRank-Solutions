import re

def find_first_repeated_alphanumeric_character(input_string):
    """
    Find the first occurrence of a substring containing two
    consecutive repeated alphanumeric characters and return that character.
    Return -1 if no such substring exists.
    """
   
    match = re.search(r'([a-zA-Z0-9])\1', input_string)
    # ([a-zA-Z0-9]) captures one alphanumeric character into group 1
    # \1 is a backreference requiring the very next character to match group 1 exactly
    # re.search scans left to right, so the first match found is the first repeated pair in the string
    
    
    return match.group(1) if match else -1
    # match.group(1) returns just the repeated character, not the pair

if __name__ == '__main__':
    s = input()
    print(find_first_repeated_alphanumeric_character(s))

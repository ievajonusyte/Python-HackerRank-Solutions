def wrapper(f):
    def fun(l):
        '''
        Standardize a list of mobile numbers into the format +91 XXXXX XXXXX
        and pass the standardized list to the decorated function.

        Each input number may have one of the following forms:
        - +91 followed by 10 digits
        - 91 followed by 10 digits
        - 0 followed by 10 digits
        - just the 10 digit number with no prefix
        
        Steps:
        1. Take only the last 10 characters of each number, which removes
           any +91, 91, or 0 prefix and leaves the actual 10 digit number.
        2. Split those 10 digits into a first group of 5 and a second group
           of 5.
        3. Join them together with +91 and a space in between to match the
           required output format.
        4. Call the original function with the new standardized list.
        '''
      
        standardized = [] # empty list to hold the standardized phone numbers
        for number in l: # We loop through each phone number in the original list l
            # take only the last 10 digits, ignoring any prefix
            number = number[-10:] # take the last 10 characters of the string number
            standardized.append('+91 ' + number[:5] + ' ' + number[5:])
        f(standardized) # Once all numbers are standardized, we call the original function f (which is sort_phone), but pass it the standardized list instead of the original l. This is the whole point of the decorator - sort_phone never "knows" the numbers were transformed before it received them
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

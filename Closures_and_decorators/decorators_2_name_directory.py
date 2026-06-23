import operator

def person_lister(f):
    def inner(people):
        '''
        Sort the list of people by age (the 4th field, index 2) in
        ascending order, then call the original function with the
        sorted list.

        Each person is a list: [first_name, last_name, age, sex]
        as strings, so age needs to be compared as a number, not
        as text.
        '''
        return [f(person) for person in sorted(people, key=lambda person: int(person[2]))]
        # sorted(people, key=lambda person: int(person[2])) - sorts the whole people list by that age key, in ascending order. Since sorted is stable, two people with the same age keep their original relative order (which matches the requirement "for two people of the same age, print them in the order of their input").
        # f(person) for person in ... - for each person in that newly sorted list, call f (which is name_format) on them, producing the formatted string like 'Mr. Mike Thomson'
        # The whole thing is wrapped in [...], a list comprehension, so the result is a list of formatted name strings, already in age order
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

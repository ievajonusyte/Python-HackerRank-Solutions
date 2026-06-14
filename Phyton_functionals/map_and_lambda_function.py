cube = lambda x: x ** 3  # raise x to the power of 3

def fibonacci(n):
    # return a list of fibonacci numbers
    fibs = []
    a, b = 0, 1 # start with the first two Fibonacci values
    for _ in range(n):  # repeat n times
        fibs.append(a)  # add current number to the list
        a, b = b, a + b  # shift: next number becomes current, sum becomes next, both sides are evaluated before assigning, so a a becomes the old b, and b becomes their sum
    return fibs
    
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

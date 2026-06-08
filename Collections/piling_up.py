from collections import deque # # deque = double-ended queue
'''
Task: You have a row of n cubes with given side lengths. 
Pick cubes one by one  always from the leftmost or rightmost position  and stack them. Each new cube placed on top must be smaller or equal to the one below it. 
Print Yes if you can stack all cubes this way, otherwise No.
'''

T = int(input()) # read how many test cases there are
for _ in range(T): # run the logic T times, one per test case
    n = int(input())  # read number of cubes (we don't actually use n directly, just consume the line)
    blocks = deque(map(int, input().split())) # read the cube sizes as a deque, e.g. "4 3 2 1 3 4" becomes deque([4, 3, 2, 1, 3, 4])
    
    top = float('inf') # the size limit for the next cube we place, infinity at start = first cube can be any size
    possible = True  # assume Yes until proven otherwise
     
    while blocks: # keep going until all cubes are placed (deque is empty)
        left = blocks[0] # peek at the leftmost cube (don't remove yet)
        right = blocks[-1] # peek at the rightmost cube (don't remove yet)

        
        if left > top and right > top:
            possible = False
            break
            # BOTH ends are too big to place on current top, no valid move exists - impossible
        
       
        if left > right: # left cube is bigger than right cube
            if left <= top:  # left fits on the stack - take it (bigger = harder to place later)
                blocks.popleft();
                top = left
            else: # left is too big, so we must take right instead
                blocks.pop();
                top = right
        else: # right cube is >= left cube
            if right <= top: # right fits on the stack - take it (bigger = harder to place later)
                blocks.pop();
                top = right
            else: # right is too big, so we must take left instead
                blocks.popleft();
                top = left
    
    print("Yes" if possible else "No") # if we placed all cubes without breaking - Yes, otherwise No

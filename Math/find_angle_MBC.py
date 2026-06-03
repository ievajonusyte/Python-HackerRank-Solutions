'''
Find Angle MBC
Right triangle ABC, 90 degrees at B. M is the midpoint of hypotenuse AC. Given AB and BC, find angle MBC (theta) rounded to nearest integer, output with degree symbol.
Key math: atan(AB / BC) converted to degrees.
'''
import math

AB = int(input())
BC = int(input())

angle = math.atan2(AB, BC)
print(str(round(math.degrees(angle))) + '\xb0')

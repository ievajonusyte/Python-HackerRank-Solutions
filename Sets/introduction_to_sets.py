'''
Explanation
The Problem:

Ms. Gabriel Williams wants to find the average of distinct plant heights in her greenhouse
We need to eliminate duplicate heights before calculating the average

Step-by-Step Solution:

Convert to Set: set(array) removes all duplicate values

For example: [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
Becomes: {161, 182, 154, 176, 170, 167, 171, 174} (8 distinct values)
Sets automatically eliminate duplicates (a key property of sets in Python)


Calculate Average:

Sum all distinct heights: 161 + 182 + 154 + 176 + 170 + 167 + 171 + 174 = 1355
Divide by count: 1355 / 8 = 169.375


Round to 3 Decimal Places: round(avg, 3) ensures the result has exactly 3 decimal places as required
'''
def average(array):
    # Convert array to set to get distinct values
    heights = set(array)
    
    # Calculate average: sum of distinct heights / count of distinct heights
    avg = sum(heights) / len(heights)
    
    # Round to 3 decimal places
    return round(avg, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

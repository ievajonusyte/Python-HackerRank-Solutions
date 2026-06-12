'''
Task: Compute average score for each student across all subjects.

Input:
  - First line: N (students) and X (subjects)
  - Next X lines: scores of all N students in that subject

Output:
  - N lines: average score for each student, to 1 decimal place

Example:
  Input: 5 students, 3 subjects
    5 3
    89 90 78 93 80    (subject 1)
    90 91 85 88 86    (subject 2)
    91 92 83 89 90.5  (subject 3)
  
  Output:
    90.0  (student 1: (89+90+91)/3)
    91.0  (student 2: (90+91+92)/3)
    82.0  (student 3: (78+85+83)/3)
    90.0  (student 4: (93+88+89)/3)
    85.5  (student 5: (80+86+90.5)/3)
'''
# Read the first line: N and X
n, x = map(int, input().split())

# Read x lines of scores
# Each line contains n scores (one score from each student in that subject)
# This creates a list of x lists
# Example: [[89, 90, 78, 93, 80], [90, 91, 85, 88, 86], [91, 92, 83, 89, 90.5]]
scores = [list(map(float, input().split())) for _ in range(x)]

# zip(*scores) unpacks the list and groups by student instead of by subject
# Without zip: data is grouped by subject (row)
# With zip(*scores): data is grouped by student (column)
# Each iteration gives one tuple containing all scores for one student
for student_scores in zip(*scores):
    # Calculate the average: sum of all scores divided by number of subjects
    average = sum(student_scores) / len(student_scores)
    # Print with exactly 1 decimal place
    print("%.1f" % average)

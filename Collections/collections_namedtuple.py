from collections import namedtuple
'''
Dr. Wesley has a spreadsheet with student data (ID, MARKS, CLASS, NAME) columns can be in any order. 
Calculate the average of all MARKS and print it rounded to 2 decimal places.
'''

n = int(input()) # Read the number of students
columns = input().split() # Read the column names line e.g. ID MARKS CLASS NAME and split into a list
Student = namedtuple('Student', columns) # Dynamically create a namedtuple using whatever column order was given so you can later access fields by name like student.MARKS

total = 0
for _ in range(n):
    data = input().split()
    student = Student(*data)
    total += int(student.MARKS)
# For each student: read the line, unpack it into a Student namedtuple, then grab .MARKS by name and add to total
print(f"{total/n:.2f}") # Divide total by number of students and print with 2 decimal places

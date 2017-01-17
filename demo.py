"""
Python script for the cof's
Steps ToDo :
1. Read the data from all csv file.
2. Map the document with the read csv file and also with the database schema
3. MySQL Python connector
4. Connect to the database
5. Execute the script

"""


import csv

# Read the file in an object
with open('section_3.csv', 'r') as f:
    reader = csv.reader(f)
    courseGoals_list = list(reader)

for row in courseGoals_list:
    print(row)


# truncate the data from the table in the database

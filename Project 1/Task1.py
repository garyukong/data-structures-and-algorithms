"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Create a list containing all unique phone numbers across texts and calls records
num = set()
for row in texts:
    num.add(row[0])
    num.add(row[1])
for row in calls:
    num.add(row[0])
    num.add(row[1])

# Print results
print("There are {} different telephone numbers in the records".format(len(num)))
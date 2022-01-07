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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# PART A
# Create a list containing calls made by (080) area code:
bangalorecalls = ()
for row in calls:
    if '(080)' in row[0]:
        bangalorecalls.append(row)

# Create a list containing receiving area codes and mobile prefixes
receivingcodes = []
for row in bangalorecalls:
    # Retrieve fixed lines
    fixedlineend = row[1].find(')')+1
    if fixedlineend > 0 and row[1][:fixedlineend] not in receivingcodes:
        receivingcodes.append(row[1][:fixedlineend])
    # Retrieve mobile numbers
    if row[1][0] in ['7','8','9'] and row[1][:4] not in receivingcodes:
        receivingcodes.append(row[1][:4])
receivingcodes = sorted(receivingcodes) # Sort list

# Print outputs
print("The numbers called by people in Bangalore have codes:",*receivingcodes, sep = "\n")

# PART B
# From bangalorecalls, count the number of calls made to fixed lines also in bangalore
bangalorecallstobangalore = 0
for row in bangalorecalls:
    if '(080)' in row[1]:
        bangalorecallstobangalore += 1

# Calculate percentage based on length of lists
answer = bangalorecallstobangalore / len(bangalorecalls) * 100

# Format to two decimal points
answer = "{:.2f}".format(answer)

# Print results
print(answer, "percentage of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
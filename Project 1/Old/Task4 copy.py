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
TASK 4: 
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Create list of unique phone numbers that make outgoing calls
makecalls = []
for row in calls:
    if row[0] not in makecalls:
        makecalls.append(row[0])

# Create a list of unique phone numbers that receive incoming calls
receivecalls = []
for row in calls:
    if row[1] not in receivecalls:
        receivecalls.append(row[1])

# Create a list of unique phone numbers that sent texts
senttexts = []
for row in texts:
    if row[0] not in senttexts:
        senttexts.append(row[0])

# Create a list of unique phone numbers that receive texts
receivetexts = []
for row in texts:
    if row[0] not in receivetexts:
        receivetexts.append(row[0])

# Create a list of unique phone numbers that make calls but never send texts, receive texts or receive incoming calls
posstelemkt = []
for row in makecalls:
    if row not in (receivecalls or senttexts or receivetexts):
        posstelemkt.append(row)

# Sort possible telemarketers
posstelemkt = sorted(posstelemkt)

# Print message
print("These numbers could be telemarketers:", *posstelemkt, sep="\n")

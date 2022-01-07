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

# Create set of unique phone numbers that make outgoing calls
makecalls = set()
for row in calls:
    makecalls.add(row[0])

# Create a set of unique phone numbers that receive incoming calls
receivecalls = set()
for row in calls:
    receivecalls.add(row[1])

# Create a set of unique phone numbers that sent texts
senttexts = set()
for row in texts:
    senttexts.add(row[0])

# Create a set of unique phone numbers that receive texts
receivetexts = set()
for row in texts:
    receivetexts.add(row[0])

# Create a set of possible telemarketers by substracting relevant numbers from the makecalls set
posstelemkt = makecalls - (receivecalls | senttexts | receivetexts)

# Sort possible telemarketers
posstelemkt = sorted(posstelemkt)

# Print message
print("These numbers could be telemarketers:", *posstelemkt, sep="\n")
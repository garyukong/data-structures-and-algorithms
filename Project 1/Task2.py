"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

# Create a dictionary containing all phone numbers in calls. Sum durations
calldir = {}
for row in calls:
    calldir[row[0]] = int(calldir.get(row[0],0))+int(row[3])
    calldir[row[1]] = int(calldir.get(row[1],0))+int(row[3])

# Retrieve maximum value (cumulative duration of calls) and key (phone number) with longest time on the phone
maxvalue = max(calldir.values()) # maximum value
maxkey = max(calldir, key=calldir.get) # key with maximum value

# Print a message
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(maxkey,maxvalue))
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

send_texts, receive_texts, receive_calls =set(), set(), set()
for record in texts:
    send_texts.add(record[0])
    receive_texts.add(record[1])
        
for record in calls:
    receive_calls.add(record[1])

tele_result = set()
for record in calls:
    temp_send = record[0]
    if temp_send not in send_texts and temp_send not in receive_texts and temp_send not in receive_calls:
        tele_result.add(temp_send)

tele_result = list(tele_result)
tele_result.sort()       #nlogn  
        
print("These numbers could be telemarketers: ")
for item in tele_result:
    print(item)
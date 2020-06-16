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

num_list = set()

for record in texts:
    num_list.add(record[0])
    num_list.add(record[1])
for record in calls:
    num_list.add(record[0])
    num_list.add(record[1])
print("There are",len(num_list),"different telephone numbers in the records.")

"""Worst Case Big-O is O(n*n), because the worst case of set add is O(n)"""

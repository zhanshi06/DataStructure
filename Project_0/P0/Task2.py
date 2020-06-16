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


dict_of_times = {}

for record in calls: #O(n)
    if record[0] not in dict_of_times.keys():
        dict_of_times[record[0]] = int(record[-1]) 
    else:
        dict_of_times[record[0]] += int(record[-1])
        
    if record[1] not in dict_of_times.keys():
        dict_of_times[record[1]] = int(record[-1]) 
    else:
        dict_of_times[record[1]] += int(record[-1])

"""list comphrehension method to find longest time and numberadapted from stack overflow"""    
longest_number_time = max(dict_of_times.items(), key=lambda x: x[1]) # O(n)
#print result which is first item in list longest number
print(longest_number_time[0],"spent the longest time", longest_number_time[1], "seconds, on the phone during September 2016.")

"""Worst Case Big-O is O(n*log n)"""

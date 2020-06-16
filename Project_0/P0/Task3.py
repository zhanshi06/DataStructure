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
in Bangalore.
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

def get_code(s):
    #mobile number
    if " " in s:
        return s[0:4]
    #fixed lines
    if "(" in s:
        end = s.index(")")
        return s[2:end]
    #telemark, probably not needed, who would call a telemarketer
    if s[0:3] == "140":
        return "140"

list_of_codes = set()
total_bang1 = 0 #count calls from 080
total_bang2 = 0 #count calls to 080

for record in calls: #O(n)
    #fixed line in Bangalore
    if "(080)" in record[0]:
        total_bang1 +=1
        temp = get_code(record[1])
        if temp == "80":
            total_bang2 +=1
        list_of_codes.add(temp)

list_of_codes = list(list_of_codes) #O(n)
list_of_codes.sort()  #nlog n 
print("The numbers called by people in Bangalore have codes:") 
for item in list_of_codes:
    print(item)
"""Worst Case Big-O is O(n*log n)"""

"""
Part B
""" 
percent = 100*total_bang2/total_bang1
percent = str(round(percent, 2))
print(percent,"percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.") 
"""Worst Case Big-O is O(1)"""

Explanation problem 2 : Finding Files
For this problem, I at first checking if path is valid and exit. If not, simply return empty list. 
If it is valid path and exist,two lists are maintaiend to help. One is to hold directories to walk through and append new directory; the second is the value of files including path. After that, the code goes throung a while loop, pop the first value of directories and getting all items from that directory. then, for each item I am checking if its directory or not and if its directory, add it to directories list (the first one), else check for file and with extension by suffix passed.

Time complexity is O(n) and space complexity is O(n). n is the number of the files/dirs within the dir
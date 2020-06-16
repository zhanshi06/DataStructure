import sys

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_int = sys.maxsize
    max_int = -sys.maxsize - 1
    for num in ints:
        if num > max_int:
            max_int = num 
        if num < min_int:
            min_int = num
    return (min_int, max_int)

## Example Test Case of Ten Integers
import random

# Test Case one
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# output: Pass

# Test Case two
l = [1] 
print ("Pass" if ((1, 1) == get_min_max(l)) else "Fail")
# output: Pass

# Test Case three
l = [-1,0,1] 
print ("Pass" if ((-1, 1) == get_min_max(l)) else "Fail")
# output: Pass

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return 0
    left = 0
    right = number//2+1
    while(right > left):
        median = (left+right) // 2 + 1
        if median*median == number:
            return median
        elif median*median > number:
            right = median-1
        else:
            left = median + 1
    if median*median < number:
        return median
    else:
        return median-1

# Test case one
print(sqrt(1))
# output: 1

# Test case two
print(sqrt(0))
# output: 0

# Test case three
print(sqrt(4))
# output: 2

# Test case four
print(sqrt(5)) 
# output: 2

# Test case five
print(sqrt(-1)) 
# output: 0


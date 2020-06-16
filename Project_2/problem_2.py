def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    left = 0
    right = len(input_list) - 1
    
    if len(input_list) == 0:
        return -1
    if (len(input_list)) == 1:
        if input_list[0] == number:
            return 0
        else:
            return -1
    
    while(left < right):
        if input_list[left] == number:
            return left
        if input_list[right] == number:
            return right
        median = (left + right) // 2 + 1
        if input_list[median] == number:
            return median
        if (input_list[median] > input_list[left] and number > input_list[median]) \
            or (input_list[median] > input_list[left] and number < input_list[median] and number < input_list[left]) \
                or (input_list[median] < input_list[left] and number > input_list[median] and number < input_list[right]):
                left = median + 1
        else:
            right = median-1
    return -1
        

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Test case one
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# output: pass

# Test case two
test_function([[], 1])
# output: pass

# Test case three
test_function([[8], 8])
# output: pass

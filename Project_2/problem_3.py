from heapq import heappop, heappush, heapify 

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    list_len = len(input_list)
    if list_len <= 1:
        return [-1, -1]


    # Creating  heap 
    heap = [] 
    heapify(heap) 
    for number in input_list:
        heappush(heap, -1 * number) 

    digit_rank = list_len//2
    if list_len%2 == 1:
        largest_digit = -1*heappop(heap) 
        element_one, element_two = largest_digit*(10**digit_rank), 0
    else:
        element_one, element_two = 0, 0
    for i in range(digit_rank): 
        digit_one = -1*heappop(heap)
        element_one += digit_one*(10**(digit_rank-1-i))

        digit_two = -1*heappop(heap)
        element_two += digit_two*(10**(digit_rank-1-i))

    return element_one, element_two

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test case one
test_function([[1, 2, 3, 4, 5], [542, 31]])
# output: Pass

# Test case two
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
# output: Pass

# Test case three
test_case = [[1,1,1,1,1], [111, 11]]
test_function(test_case)
# output: Pass


# Test case four
test_function([[], [-1, -1]])
test_function(test_case)
# output: Pass


# Test case five
test_function([[0], [-1, -1]])
test_function(test_case)
# output: Pass



def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    hash_dict = {0:0,1:0,2:0}
    for i in range(len(input_list)):
        hash_dict[input_list[i]] += 1
    return [0]*hash_dict[0] + [1]*hash_dict[1] + [2]*hash_dict[2]
    

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Test Case One:
test_function([])
# output: pass

# Test Case Two:
test_function([0 ,0, 0, 2, 2, 2])
# output: pass

# Test Case Three:
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# output: pass
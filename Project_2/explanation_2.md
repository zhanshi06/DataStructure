Search in a Rotated Sorted Array

This case we already have the sorted array, we can still use it but to need to find more condition;
As shown:
if (input_list[median] > input_list[left] and number > input_list[median]) \
            or (input_list[median] > input_list[left] and number < input_list[median] and number < input_list[left]) \
                or (input_list[median] < input_list[left] and number > input_list[median] and number < input_list[right]):

 time: O(log(n))
 space: O(1)
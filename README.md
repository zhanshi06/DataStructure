# DataStructure

### Project_0: Investigating Texts and Calls

### Project_1: Data Structures

OrderedDict was used from collections module, the time-complexity of the OrderedDict for move_to_end is O(1) . After instantiating class with max capacity, we can use set() method to set cache and assign value at specific keys. All keys are None until assigned. It will try to assign value to given key by removing the value if assigned else after checking capacity and key item is removed from dict and value is assigned again. To get value of the key, we can use get() method.
For get(key): we return the value of the key that is queried in O(1) and return -1 if we don’t find the key in out dict/cache. And also move the key to the end to show that it was recently used.

For set(key, value): first,  add/ update the key by conventional methods. And also move the key to the end to show that it was recently used. 

Time complexity of get() is O(1) and of set() is O(1). Space complexity of the LRU Cache is O(n).





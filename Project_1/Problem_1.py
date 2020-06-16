
import collections
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        if capacity == 0:
            print("Warning please provice the capacity larger than 0")
        self.cache = collections.OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        # use the move_to_end methods(O(1)) to handle the get as well as the most recent value; 
        if key not in self.cache: 
            return -1
        else: 
            self.cache.move_to_end(key) 
            return self.cache[key] 

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        self.cache[key] = value 
        self.cache.move_to_end(key) 
        if len(self.cache) > self.capacity: 
            self.cache.popitem(last = False) 
        
### Test Case one ###
lru_cache = LRU_Cache(0)
lru_cache.set(1, 9);
print(lru_cache.get(9))       # returns -1 because capacity is zero

### Test Case two ###
lru_cache = LRU_Cache(5)
lru_cache.set(1, 1);
lru_cache.set(2, 2);
lru_cache.set(3, 3);
lru_cache.set(4, 4);
print(lru_cache.get(2))      # returns 2
print(lru_cache.get(9))      # returns -1 because 9 is not present in the cache

### Test Case three ###
lru_cache = LRU_Cache(5)
lru_cache.set(1, 1);
lru_cache.set(2, 2);
lru_cache.set(3, 3);
lru_cache.set(4, 4);
lru_cache.set(5, 5) 
lru_cache.set(6, 6)
print(lru_cache.get(1))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    item_set = set() # Space cpmplexity O(n)
    _current = llist_1.head 
    while(_current):
        item_set.add(_current.value)
        _current = _current.next
    _current = llist_2.head 
    while(_current):
        item_set.add(_current.value)
        _current = _current.next
    
    result_list = LinkedList()
    for item in item_set: 
        
        result_list.append(item)

    return result_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    item_dict = dict() # Space cpmplexity O(n)
    item_joint = set()
    _current = llist_1.head 
    while(_current):
        item_dict[_current.value] = 1
        _current = _current.next
    _current = llist_2.head 
    while(_current):
        if _current.value in item_dict:
             item_joint.add(_current.value)
        _current = _current.next
    
    result_list = LinkedList()
    for item in item_joint: 
        
        result_list.append(item)

    return result_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
'''
output:
32 -> 65 -> 2 -> 35 -> 4 -> 6 -> 1 -> 9 -> 11 -> 3 -> 21 -> 
6 -> 4 -> 6 -> 21 -> 
'''

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
'''
output:
65 -> 2 -> 35 -> 4 -> 6 -> 1 -> 8 -> 9 -> 7 -> 11 -> 3 -> 21 -> 23 -> 

'''

# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
'''
output:
65 -> 2 -> 35 -> 4 -> 6 -> 3 -> 23 -> 

'''
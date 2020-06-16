import datetime
import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            temp_data = self.last
            self.last = Block(timestamp, data, temp_data)
            self.last.previous_hash = temp_data


def get_timestamp():
    return datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")

###  Test Case One  ###
A = BlockChain()  
print(A.head) #output: None 

###  Test Case Two  ###
# blocks
block_zero = Block(get_timestamp(), "Information X", 0)
block_one = Block(get_timestamp(), "Information Y", block_zero)
block_two = Block(get_timestamp(), "Information Z", block_one)

# linked list
linked_list = BlockChain()
linked_list.append(get_timestamp(), "Information A")
linked_list.append(get_timestamp(), "Information B")

# tests
print("Block Zero data : ", block_zero.data)
print("Block Zero hash : ", block_zero.hash)
print("Block Zero timestamp : ", block_zero.timestamp)
print("Block one's previous block's data : ", block_one.previous_hash.data)
print("Linked list last data : ", linked_list.last.data)
print("Linked list last's previous hash data : ", linked_list.last.previous_hash.data)
'''
output:
('Block Zero data : ', 'Information X')
('Block Zero hash : ', 'a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10')
('Block Zero timestamp : ', '14/06/2020 05:31:30')
("Block one's previous block's data : ", 'Information X')
('Linked list last data : ', 'Information B')
("Linked list last's previous hash data : ", 'Information A')
'''

###  Test Case Three  ###
# linked list
linked_list = BlockChain()
linked_list.append(get_timestamp(), "Information A")
print("Linked list last data : ", linked_list.last.data)
'''
output:
('Linked list last data : ', 'Information A')
'''

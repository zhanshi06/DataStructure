import sys
import heapq

class Huff_Node:
    def __init__(self,value, wt):
        """Create node for given symbol and weight."""
        self.left = None
        self.right = None
        self.value = value
        self.wt = wt        
        
    #Python method redefined to compare two Huff_Nodes
    def __lt__(self, other):
        return self.wt < other.wt
    
    #return a string version of Huff_Node, used for testing
    def __str__(self):
        return str(self.value)+" "+str(self.wt)

def huffman_encoding(data):
    if len(data)==0:
        return "", {}
    
    # get the char frequency and put itnto the minheap 
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1
    
    #create a sorted list key, freq tuple pairs
    freq_sorted = sorted(zip(freq.values(), freq.keys()))
    heap = []
    for i in range(len(freq_sorted)):
        value = freq_sorted[i][1] #second item is value
        freq = freq_sorted[i][0] #first item is frequency
        
        heap.append(Huff_Node(value, freq))
    
    heapq.heapify(heap)#Create heap

    while len(heap) != 1:
        Z = Huff_Node(None,None)
        lft = heapq.heappop(heap)
        Z.left  = lft
        rgt = heapq.heappop(heap)
        Z.right  = rgt
        Z.wt = lft.wt + rgt.wt
        heapq.heappush(heap, Z)

    code_table = {}
    def getCode(hNode, currentCode):
        if (hNode == None): 
            return
        if (hNode.left == None and hNode.right == None):
            code_table[hNode.value] = currentCode
        getCode(hNode.left, currentCode + "0")
        getCode(hNode.right, currentCode + "1")
    
    if len(freq_sorted) == 1:
        getCode(heap[0], "0")
    else:
        getCode(heap[0], "")

    huffman_code = ""

    for char in data:
       huffman_code += code_table[char]
    return huffman_code, heap


def huffman_decoding(data,tree):
    if tree[0].left == None and tree[0].right == None:
        return str(tree[0].value)*len(data)

    decode = ""
    n = len(data)
    count = 0
    while count < n:
        current = tree[0]
        while current.left != None or current.right != None:
            if data[count] == "0":
                current = current.left
            else:
                current = current.right
            count+=1
        decode+=current.value
        
    return decode

if __name__ == "__main__":
    ### Test Case one ###

    codes = {}

    a_great_sentence = "ssss"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print("="*20)
    '''
    output:

    The size of the data is: 41

    The content of the data is: ssss

    The size of the encoded data is: 24

    The content of the encoded data is: 0000

    The size of the decoded data is: 41

    The content of the encoded data is: ssss

    '''

    ### Test Case two ### 
    codes = {}

    b_great_sentence = "abc"
    print ("The size of the data is: {}\n".format(sys.getsizeof(b_great_sentence)))
    print ("The content of the data is: {}\n".format(b_great_sentence))
    
    encoded_data, tree = huffman_encoding(b_great_sentence)
    print(encoded_data)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print("="*20)
    '''
    output:
    ====================
    The size of the data is: 40

    The content of the data is: abc

    01110
    The size of the encoded data is: 24

    The content of the encoded data is: 01110

    The size of the decoded data is: 40

    The content of the encoded data is: abc
    '''


    # ### Test Case three ### 
    codes = {}

    a_great_sentence = "The bird is the word"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    '''
    output:
    The size of the data is: 57

    The content of the data is: The bird is the word

    The size of the encoded data is: 36

    The content of the encoded data is: 0000001111011010101111011010110111110111100001001111011010001001011010

    The size of the decoded data is: 57

    The content of the encoded data is: The bird is the word

    '''
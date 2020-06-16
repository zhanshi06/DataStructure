
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.last = False
        
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode() 
    
    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)

            current_node = current_node.children[char]

        current_node.last = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return None
            
            current_node = current_node.children[char]
        
        return current_node

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.last = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        chars_list = []
        for char in self.children:
            if self.children[char].last:
                chars_list.append(suffix + char)
            
            for tmp_res in self.children[char].suffixes(suffix+char):
                chars_list.append(tmp_res)
        
        return chars_list


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

def test_func(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

# Test Case one
test_func('ant') 
# output 
'''
hology
agonist
onym
'''
print('#'*10)

# Test Case two
test_func('f')
# output 
'''
un
unction
actory
'''
print('#'*10)

# Test Case three
test_func('fu')
# output 
'''
n
nction
'''
print('#'*10)
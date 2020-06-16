# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode('/', root_handler)

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        _cur = self.root
        
        for path in path_list:
            if path not in _cur.children:
                _cur.insert(path)
            _cur = _cur.children[path]

        _cur.handler = handler


    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        _paths = path_list
        
        _cur = self.root
        for path in _paths:
            if path not in _cur.children:
                return None
            _cur =  _cur.children[path]
        return _cur.handler 

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, value='', handler=None):
        # Initialize the node with children as before, plus a handler
        self.value = value
        self.children = {}
        self.handler = handler

    def insert(self, path, handler=None):
        # Insert the node as before
        self.children[path] = self.children.get(path, RouteTrieNode(path))
        self.children[path].handler = handler


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie = RouteTrie(root_handler)
        self.not_found = not_found_handler

    def add_handler(self, paths, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(paths)
        self.routeTrie.insert(path_list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        if self.routeTrie.find(path_list):
            return self.routeTrie.find(path_list)
        else:
            return self.not_found

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_list = []
        for p in path.split('/'):
            if len(p.strip()) > 0:
                path_list.append(p)
        return path_list

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
# Test Case one:
print(router.lookup("/")) 
# Output: 'root handler'

# Test Case one:
print(router.lookup("/home")) 
# Output: 'not found handler' 

# Test Case three:
print(router.lookup("/home/about")) 
# Output: 'about handler'

# Test Case four:
print(router.lookup("/home/about/")) 
# Output: 'about handler'

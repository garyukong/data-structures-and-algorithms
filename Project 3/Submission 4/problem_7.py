class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = "not found handler"

class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert_recursively(self, arr, node, handler):
        """Inserts an array of elements into the trie"""
        # Do nothing if the length of the array is 0
        if len(arr) == 0:
            return

        # If the element is not yet in the Trie, create a new child node for the element
        if arr[0] not in node.children:
            node.children[arr[0]] = RouteTrieNode()

        # If only single element in the array, set handler
        if len(arr) == 1:
            node.children[arr[0]].handler = handler

        # Otherwise, recurse by taking a slice of the original array and setting node as the relevant child
        else:
            self.insert_recursively(arr[1:], node.children[arr[0]], handler)

    def insert(self, arr, handler):
        """Inserts an array of elements into the trie"""
        self.insert_recursively(arr, self.root, handler)

    def find_recursively(self, arr, node):
        """Navigates the trie to find a match for a path given by an array of elements"""
        # If the entire array has been traversed, return the node
        if len(arr) == 0:
            return node
        
        # If the path is not found, return not found handler
        if arr[0] not in node.children:
            return None

        # Else, recurse through the tree until all elements in arr have been traversed
        return self.find_recursively(arr[1:], node.children[arr[0]])

    def find(self, arr):
        """Navigates the trie to find a match for a path given by an array of elements"""
        return self.find_recursively(arr, self.root)

class Router:
    def __init__(self, root_handler, not_found_handler):
        """Create a new RouteTrie for holding routes"""
        self.rt = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def split_path(self, path):
        """Outputs an array where each element represent a part of the path"""
        path_parts = []
        path_parts[:] = [part for part in path.split('/') if part != '']
        return path_parts
        
    def add_handler(self, path, handler):
        """Adds handler for a given path into the RouteTrie"""
        self.rt.insert(self.split_path(path), handler)

    def lookup(self, path):
        """Looks up a path in the RouteTrie and returns handler"""
        out_node = self.rt.find(self.split_path(path))
        if out_node:
            return out_node.handler
        return self.not_found_handler

if __name__ == '__main__':

    # TEST CASE 1: Creating the router and adding /home/about/me handler (creating a fresh new trie)
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about/me", "me handler")
    print('\nTEST CASE 1')
    print(router.lookup("")) # should print 'root handler'
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler'
    print(router.lookup("/home/about")) # should print 'not found handler'
    print(router.lookup("/home/about/")) # should print 'not found handler'
    print(router.lookup("/home/about/me")) # should print 'me handler'

    # TEST CASE 2: The same as above but adding /home/about/me/ instead of /home/about/me
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about/me/", "me handler")
    print('\nTEST CASE 2')
    print(router.lookup("")) # should print 'root handler'
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler'
    print(router.lookup("/home/about")) # should print 'not found handler'
    print(router.lookup("/home/about/")) # should print 'not found handler'
    print(router.lookup("/home/about/me")) # should print 'me handler'

    # TEST CASE 3: Adding /home/about handler (adding handler to node that is not a leaf)
    router.add_handler("/home/about", "about handler")
    print('\nTEST CASE 3')
    print(router.lookup("")) # should print 'root handler'
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler'
    print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me")) # should print 'me handler'

    # TEST CASE 4: Adding /home/about/me/you handler (adding new node and handler which is a leaf)
    router.add_handler("/home/about/me/you", "you handler")
    print('\nTEST CASE 4')
    print(router.lookup("")) # should print 'root handler'
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler'
    print(router.lookup("/home/about")) # should print 'about handler'
    print(router.lookup("/home/about/")) # should print 'about handler'
    print(router.lookup("/home/about/me")) # should print 'me handler'
    print(router.lookup("/home/about/me/you")) # should print 'you handler'

    # TEST CASE 5: Adding empty path and handler
    router.add_handler("", "")
    print('\nTEST CASE 4')
    print(router.lookup("")) # should print 'root handler'
    print(router.lookup("/")) # should print 'root handler'

    # TEST CASE 5: Adding empty path and handler
    router.add_handler("///////////////////////", "Strange handler")
    print('\nTEST CASE 5')
    print(router.lookup("")) # should print 'root handler' - root handler cannot be modified once the router has been made
    print(router.lookup("/")) # should print 'root handler' - root handler cannot be modified once the router has been made
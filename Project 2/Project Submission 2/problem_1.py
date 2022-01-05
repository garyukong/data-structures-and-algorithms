class Node():
    
    def __init__(self, key, value, recency):
        self.key = key
        self.value = value
        self.recency = recency # Counter to check the relative order of item being accessed. Node with the lowest recency is the least recently accessed node

class LRU_Cache():

    def __init__(self, capacity = 5):
        self.cache = []
        self.capacity = capacity
        self.operationCount = 0 # Counter to check the total number of get/set operations performed on the cache. Used as reference to set recency value of nodes

    def getLength(self):
        """
        Determine length of the cache

        Returns:
            integer length of the cache
        """
        return len(self.cache)

    def cacheHit(self,key):
        """
        Determine whether or not the key is in the cache.

        Traverses the cache until a value with a match to the key is found, or return false otherwise.
        
        Args:
            key(int): key to check for in the cache

        Returns:
            boolean value of whether the key is in the cache

        """
        index = 0
        while index < self.getLength():
            if self.cache[index].key == key:
                return True
            index += 1
        return False

    def getLRU(self):
        """
        Determine index of the element that is least recently used.

        Iterates through elements in the cache to find item with lowest 'recency' value.

        Returns:
            index of the least recently used element in the cache
        """
        # Initialise as the total number of operations
        LRUflag = self.operationCount

        # Find the item with the lowest recency value
        LRUindex = 0
        for index, element in enumerate(self.cache):
            if element.recency < LRUflag:
                LRUflag = element.recency
                LRUindex = index
        return LRUindex

    def get(self, key):
        """
        Get value for node with the provided key. Return -1 if nonexistent

        Traverses through the cache until a node with the given key is found and return its value

        Args:
            key: the key to search for

        Returns:
            value of node with the provided key
        """
        # Increment count of operations
        self.operationCount += 1
        
        # Traverse through the array and return the value if a cache hit occurs      
        index = 0
        while index < self.getLength():
            if self.cache[index].key == key:                    # If the cell contains a node with the given key
                self.cache[index].recency = self.operationCount # Set recency value as the current count of operations
                return self.cache[index].value                  # Return the value
            index += 1
        
        # Return -1 otherwise
        return -1

    def set(self, key, value):
        """
        Set the value for a given key.
        
        Appends, replaces, or updates node containing key:value pair in/to the cache
        (depending on whether the cache already contains the key and whether the cache is at capacity)

        Args:
            key: the key to add to the cache
            value: the value to add to the cache 
        """      
        # Increment count of operations by 1
        self.operationCount += 1

        # Create a new node. Set the recency value to equal to current count of operations
        new_node = Node(key, value, self.operationCount)

        # If the capacity is 0, raise an exception
        if self.capacity <= 0:
            raise Exception("Sorry, capacity has to be greater than 0")

        else:
            # If the key is not in the cache
            if self.cacheHit(key) is False: 
                if self.getLength() < self.capacity:        # If the cache is not full, append the new node into the cache
                    self.cache.append(new_node)
                else:                                       # If the cache is full, replace the least used item with the new node
                    self.LRUindex = self.getLRU()
                    self.cache[self.LRUindex] = new_node
                return
                    
            # Else, if the key is already in the cache, update the value of the node with the corresponding key
            else:
                index = 0
                while index < self.getLength():
                    if self.cache[index].key == key:
                        self.cache[index].value = value
                    index +=1
                return

if __name__ == "__main__":

    # Test case 1: Cache is size 5 (Deletions occur due to cache reaching capacity)
    def test_case_1():
        our_cache = LRU_Cache(5)

        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)

        print(our_cache.get(1))     # should return 1
        print(our_cache.get(2))     # should return 2
        print(our_cache.get(9))     # should return -1 because 9 is not present in the cache

        our_cache.set(5, 5) 
        our_cache.set(6, 6)

        print(our_cache.get(3))     # should return -1 because the cache reached its capacity and 3 was the least recently used entry

        our_cache.set(7,'Seven')

        print(our_cache.get(7))     # should return 'Seven'
        print(our_cache.get(4))     # should return -1 because the cache reached its capacity and 4 was the least recently used entry

        our_cache.set(4,1)

        print(our_cache.get(4))     # should return 1
        print(our_cache.get(1))     # should return -1 because the cache reached its capacity and 1 was the least recently used entry

    print()
    print("TEST CASE 1: CACHE SIZE 5")
    print(test_case_1())

    # Test case 3: Cache is size 20 (Deletions do not occur as cache never reaches capacity)
    def test_case_2():
        our_cache = LRU_Cache(20)

        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)

        print(our_cache.get(1))         # should return 1
        print(our_cache.get(2))         # should return 2
        print(our_cache.get(9))         # should return -1 because 9 is not present in the cache

        our_cache.set(5, 5) 
        our_cache.set(6, 6)

        print(our_cache.get(3))         # should return 3

        our_cache.set(7,'Seven')

        print(our_cache.get(7))         # should return 'Seven'
        print(our_cache.get('Seven'))   # should return -1 because 'Seven' (as a key) is not present in the cache

        our_cache.set(4,1)

        print(our_cache.get(4))         # should return 1
        print(our_cache.get(1))         # should return 1

    print()
    print("TEST CASE 20: CACHE SIZE 20")
    print(test_case_2())

    # Test case 3: Cache is size 0
    def test_case_3():
        our_cache = LRU_Cache(0)

        our_cache.set(1, 1)

    print()
    print("TEST CASE 3: CACHE SIZE 0")
    print(test_case_3()) # Should return an exception as the cache's capacity has to be greater than 0
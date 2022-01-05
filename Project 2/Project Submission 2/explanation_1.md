# Problem 1: LRU Cache

## Design considerations
For the cache, an array of nodes was used, whereby each node contains a key, value, and recency value. There are several reasons for doing this:
- Firstly, using an array of nodes enables each item to have three attributes (key, value, recency value). Recency value is required to identify the least recently used item in the cache.
- An array was more suitable vs. a linked list due to an array’s ability to point to elements by index – needed to identify and replace the most recently used elements (as required by the set function when the cache is full)
- An array also has in-built python methods (e.g., len function needed to compare current length of the cache to the capacity)

## Set function complexity

### Time complexity
Time complexity of the set function is O(1):

Time complexity of the set function comes largely from two cases which require traversal of the cache:

- The first, when the when the key is not already in the cache, but the cache has reached its capacity, it calls the getLRU function (which involves cache traversal) through the following:

        self.LRUindex = self.getLRU()

  This would lead to a time complexity of O(n) where n refers to the number of items in the cache

- The second is when the key is already in the cache and the value needs to be updated, the function uses a while loop to traverse the cache until an element with a matching key is found:

        while index < self.getLength():
  
  This too would lead to a time complexity of O(n) where n refers to the number of items in the cache

However, as the inputs of the set function are 'key' and 'value', time complexity of the set function is constant and is independent of the size of the cache.

### Space complexity
Space complexity of the set function is O(n):

1. Input space complexity is O(n) as both key and value can take multiple data types, and memory utilisation will depend on the data type being used for each:
    - O(n) for key
    - O(n) for value

2. Auxiliary space complexity is O(n) as due to creation of a new_node:

        new_node = Node(key, value, self.operationCount)

3. This evaluates to O(2n) --> O(n)

## Get function complexity

### Time complexity
Time complexity of the get function is O(1) as time complexity is largely driven by the traversal of the cache, which depends on the size of the cache but not the input of the get function (the key to be added)

### Space complexity
Space complexity of the get function is O(n):
1. Input space complexity is O(n) as the key can take multiple data types, and memory utilisation will depend on the data type being used for the key
2. Auxiliary space complexity is O(1) as no new objects are created in the algorithm which depends on the size of the input of the function (the key)
- This evaluates to O(n + 1) --> O(n)

# Problem 2: File Recursion

## Design considerations
A recursive algorithm was chosen because file structures have recursive nature. By choosing to use recursion over a while/for loop, there is no limit to the number of iterations that has to be done in order to traverse the entire depth of the directory (i.e., the algorithm will iterate as many times as it has to until it reaches all files in the directory)

## Time complexity
Time complexity is O(n^2):

1. There are n recursive call of the function, occuring once for each entry in the path and its subdirectories. This is because the call:

        find_files(suffix, childpath)
  
   is only made from within the for loop, and each entry will only be accessed once.

2. For each recursive call, the algorithm spends O(n) time as there are other operations that occur within the for loop beyond the recursive call, specifically:

        os.path.join(path, filename)

        files += filesToAd

3. Thus, there are O(n) recursive calls, and there are O(n) operations per recursive call, evaluating to O(n^2)

## Space complexity
Space complexity is O(n + 1) --> O(n)

1. Input space complexity is O(1) because both inputs (suffix and path) can only take strings which each take the same amount of memory

2. Auxiliary space complexity is O(n) where n refers to the depth of the directory inserted in the path.

   The maximum size of the call stack is the depth of the directory as the function will keep making recursive calls until the path refers to a file i.e., no longer has any subdirectories, as per the terminating conditions:

        if os.path.isfile(path) and path.endswith(suffix):

        elif os.path.isfile(path):

# Problem 3: Huffman Coding

## Huffman_encoding

### Design considerations
To create the initial queue, the count_chars function creates a dictionary, which lends itself well to storing individual unique characters and their frequencies. Dictionaries have the advantage of only having unique key values, so condenses the initial string to only unique characters.

An array of node objects was used to form the priority queue for several reasons:
- Node objects were inserted into the array so that each item in the array could contain four attributes: characters, frequencies, left child, and right child
- In-built python functionality for arrays readily enables popping of last-inserted elements from the queue (in the process_queue function)
- Arrays have index functionality, enableing re-insertion of nodes after merging into the appropriate positions of the priority queue (through the insert_node function)

In the encode_string function, a dictionary was made that contained unique characters and the associated binary codes for each character. Creating this dictionary prior to encoding each individual character in the string means that characters only have to be mapped to binary codes (encode_char) once per unique character (as opposed to once per character in the string).

### Time complexity
Worst-case time complexity is O(n log n) where n refers to the length of the string.

Each of these four helper functions are called sequentially in the broader huffman_encoding function:

        charCounts = count_chars(string)
        initialQueue = make_initial_queue(charCounts)
        root = process_queue(initialQueue)
        finalOutput = encode_string(root, charCounts)
        
        return finalOutput, root

The time complexities of the char_counts, make_initial queue, process_queue, and encode_string functions are O(n), O(n), O(n^2), and O(n log n), respectively. So overall time complexity of the huffman_encoding function is O(2n + n^2 + n log n) which can be simplified to O(n log n)

The rationale for each individual sub-functions' time complexities are as follows:

1. Count_chars has time complexity of O(n) where n refers to the length of the string due to the for loop:

        charCounts = {}
        for char in string:
        if char not in charCounts:
                charCounts[char] = 1
        else:
                charCounts[char] += 1
        return charCounts

2. Make_initial_queue has time complexity of O(n) where n refers to the length of the string, due to the for loop: 

        charCounts = dict(sorted(charCounts.items(),key = lambda x: x[1]))
        priorityQueue = []
        for char, freq in charCounts.items():
                new_node = Node(char, freq)
                priorityQueue.append(new_node)
        return priorityQueue

    Whilst using the dictionary from count_chars should reduce the length of the string that has to be iterated over, in the worst-case scenario (all characters in the string are unique), the length of the dictionary would equal the length of the string.

3. Process_queue has a time complexity of O(n^2) where n refers to the length of the string, due to the while loop:
       
        while len(priorityQueue) > 1: 

  Within the while loop, there is a call to the insert_node function, which involves a for loop iterating through the queue:
  
        for i in range(len(queue)):
                if node.freq < queue[i].freq:   # If node to be inserted has lower frequency than a given node in the queue
                queue.insert(i, node)       
                return
        queue.append(node)                  
        return

  In the worst case scenario (all characters in the string are uniuqe), the length of the queue would be equal to the length of the string.

4. Encode_string has time complexity of O(n log n):

- The first part of the function has a time complexity of O(n log n) where n refers to the length of the string.

        huffmanMap = {}
        for char in charCounts:
            huffmanMap[char] = encode_char(root, char)

  The for loop has a worst-case time complexity of O(n) where n refers to the length of the string (assuming worst case scenario of each character being distinct).

- The for loop runs in O(n * log n time).

  Each iteration of the for loop makes a call to encode_char, which has a time complexity of O(log n), due to the sub-function's call to the map_path function:
        
        traversalPath = map_path(root, char)
    
  The number of recursive calls map_path makes depends on the depth of the Huffman tree, and the depth of the Huffman tree grows logarithmically vs. the number of distinct characters in the string.
  
- The for loop in the second part of the function runs in O(n) time where n refers to the length of the string:

        for char in string:
                output += huffmanMap[char]

- Therefore, the encode_string function has time complexity of O(n + n log n), which evaluates to O(n log n)

### Space complexity
Space complexity is O(n + 1) --> O(n):

1. Input space complexity is O(1) because the input is a string which will remain an array of size 256 no matter what the input (string) size is

2. Auxiliary space complexity is O(n) where n is the length of the string, as the number of elements in the priority queue (and thus, the Huffman tree) is proportional to the length of the string in the worst-case scenario in which each character of the string is unique

## Huffman_decoding

### Time complexity
Time-complexity is O(n) where n refers to the length of the encoded data:

1. For the 'data' parameter, the for loop:

        for bit in data:

   leads to a time-complexity of O(n) where n refers to the length of the encoded data, as the loop will have to iterate through each bit in the encoded the data.

2. For the 'root' parameter, time complexity is constant vs. the depth of the Huffman tree). The total number of iterations in huffman_decoding function is agnostic of the depth of the Huffman tree (i.e., there is no nested for/while loop here)

### Space complexity
Space complexity is O(1 + 1) --> O(1):

1. Input space complexity is O(1):
- O(1) for the 'data' parameter because the input is a single string which will remain an array of size 256 no matter what the input (string) size is
- O(1) for the 'root' parameter because the input is a single node which which will occupy the same amount of memory no matter what node is inputted. Any node contains four parameters which always has the same data types: char(character), freq(integer), left(node), and right(node)

2. Auxiliary space complexity is O(1). The algorithm creates and updates two objects (decodedString and currentNode) which will always occupy the same amount of memory as the algorithm runs:
- decodedString will always be a single string (i.e., an array of size 256)
- currentNod will always be a Node object

# Problem 4: Active Directory

## Design considerations
The code makes a recursive call in the following code:

      for sub_group in group.groups:
        return is_user_in_group(user, sub_group)

This enables the function to traverse all groups and users within a given 'group' input irrespective of the number of levels in the directory.

## Time complexity
Time complexity is O(n) where m refers to the total number of users in the directory.

1. The function will make O(j) recursive calls where j refers to the total number of groups in the directory, as the recursive call is nested under a for loop

2. Each recursive call runs in O(k) time, where k refers to the number of users in each group, due to use of the IN operator in:

        if user in group.users

3. This can be simplified to O(n), where n refers to the total number of users, since number of users (n) = number of groups (j) * number of users per group (k)

## Space complexity
Space complexity is O(m * n), where m refers to the depth of the directory and n is the maximum number of entries per level of the directory

1. Input space complexity is O(1) for the 'user' parameter. The 'user' parameter can take multiple data types but will almost certainly be a string, which will remain an array of size 256 no matter what the input(string) length is

2. Input space complexity is O(l) for the 'group' parameter where l refers to the size of the inputted Group object. The size of the inputted Group object which will depend on the number of entries (groups and users) within the object (i.e., self. groups and self.users)

3. Auxiliary space complexity is O(m * n) where m refers to the depth of the directory and n refers to the maximum number of entries per level of a directory
 - maximum number of recursive calls (m) in the call stack is equal to the depth of the directory
 - memory occupied per recursive call (n) equals the number of entries within a 'Group' object used as the 'group' input in the recursive call:
        
        return is_user_in_group(user, sub_group)

 - the theoretical limit to auxiliary space used is therefore the depth of the directory (m) * maximum number of entries per level of the directory (n)

4. O(l) <= O(m * n) since at most, O(m) = O(n) where the Group object inputted into the is_user_in_group function is the Group with the largest number of self.group and self.child entries (i.e., the maximum number of entries per level of the directory)

5. As such, overall time complexity is at maximum O(m * 2n) --> O(m * n)

# Problem 5: Blockchain

## Design considerations
The block class contains 'previous' variable in addition to those outlined in the diagram. While the previous_hash variable do point to hashes of previous blocks in the blockchain, the previous_hash variable points to a hash variable as opposed to an entire block. In contrast, the previous 'variable' allows each block to point to an entire block.

The initial block of the Blockchain corresponds to the tail of the Blockchain (as opposed to a head of a typical Linked List), with each block containing a 'previous' variable which is the opposite of the typical 'next' variable of a Linked List node. As such, the append_data function has a logic that largely follows that of a prepend function for a conventional Linked List.

Several functions typically present in a linked list were excluded in the Blockchain implementation:
- Prepend was not included as in a blockchains, blocks are always added to the tail (and not to the head)
- There is no functionality to insert blocks at different specific indices as blocks can only be appended in a blockchain
- Pop and delete functions were not included as data cannot be removed from a blockchain

## Complexity (Functions in the Block class)
calc_hash has time and space complexity of O(n) and O(1), respectively, where n refers to the length of the string to be encoded.
- The SHA-256 algorithm breaks the string into 512-bit parts and performs operations per 512-bit part. As the length of the input string grows, so will the number of 512-bit parts that operations need to be performed on, leading to O(n) time complexity.
- The algorithm involves use of a fixed number of temp variables (constituting auxiliary space utilisation) irrespective of the length of the input string, leading to space complexity of O(1)

All other functions has O(1) time and space complexity as they primarily involve retrieval of values from a single block.

## Complexity (Functions in the Blockchain class)
append_data time complexity is O(1) as the function involves a constant number of operations irrespective of the length of the blockchain or the data(string) being added

append_list time complexity is O(n) where n refers to the length of data_list, due to the use of a for loop iterating over the data_list

search_hash, search_data, search_index, get_hashes, get_hash_tuples, get_all_details, __len__, __repr__ time complexity is O(n), where n refers to the length of the blockchain. Each of these functions involve single while loops used to traverse each block of the blockchain, and so the number of operations will grow linearly with the number of blocks. The worst case scenarios are where the items being searched occur at the head of the blockchain, leading to a need to traverse every block prior before the search operations are completed

Space complexity of all functions is O(n), driven by O(n) input space complexity. All functions have a blockchain as an input, and memory used by the blockchain input grows linearly with the number of blocks in the blockchain. For the get_ functions, space complexity is technically O(2n) due to O(n) auxiliary space complexity outputs are lists whose lengths grow linearly as the number of blocks processed grows. O(2n) however evaluates to O(n) overall space complexity.

# Problem 6: Set and Intersection

## Union function

### Design considerations
A set was made based on the values from both linked lists as it immediately removes all duplicate values. Union operations by definition are also required to produce a set, so the set data structure served as a natural fit

### Complexity
Time complexity is O(n), where n refers to the combined length of llist_1 and llist_2:
1. Creating an empty union_set object (through the set() operator) runs in O(1)
2. The two while loops to traverse through each linked list collectively runs in O(j + k) time, where j and k represent the lengths of each input linked list, respectively. This can be simplified to O(n) where n represents the combined length of each linked list.
3. The for loop to iterate through union_set runs in O(n). In the worst-case scenario (where all elements in each input list is completely unique), length of union_set would be equal to the combined length of each linked list (i.e., n)
4. Overall, this evaluates to O(2n + 1), which can be simplified to O(n)

Space complexity is O(n), where n refers to the combined length of llist_1 and llist_2:
1. Input space complexity is O(n) since inputs are linked lists whose lengths will impact the amount of memory used
2. Auxiliary space complexity is O(2n) since two objects are created whose memory utilisation depends on the size of the original inputs: a union_set (a Set), and out (a Linked List)
3. This evaluates to O(3n) --> O(n)

## Intersection function

### Design considerations
A dictionary was used where keys represent unique values in the first linked list, and values (0/1) represent a flag of whether the key also appears in the second list. The dictionary has an advantage of only storing unique keys (thus removing duplicates) and allowing me to filter keys based on whether each key appears in both input lists.

Thereafter, an array was used as it allows for sorting and is an iterable, enabling creation of the output linked list.

### Complexity
Time complexity is O(n), where n represents the combined length of llist_1 and llist_2
1. The first while loop to traverse through llist_1 runs in O(j) time, where j represents the length of llist_1
2. The second while loop to traverse through llist_2 runs in O(k) time, where k represents the length of llist_2
4. Creating intersection_array runs in O(j) time. Doing so involves iterating through all key:value pairs in the dictionary. In the worst-case scenario, all items in llist_1 would also appear in llist_2 (i.e., values == 1 for every key), and the length of the dictionary would equal the length of llist_1
5. Iterating through the sorted intersection_array runs in O(j) time, under the same worst-case scenario described in point #4 above
6. Overall, this evaluates to time complexity of O(3j + k) --> O(n), since the coefficient 3 can be disregarded and j + k = n

Space complexity is O(n), where n represents the combined length of llist_1 and llist_2
1. Input space complexity is O(n) since inputs are linked lists whose lengths will impact the amount of memory used
2. Auxiliary space complexity is O(3j) as three separate objects are created: intersection_dict (a dictionary), intersection_array (an array), out (a linked list). The upper limit of memory utilisation for each of these objects is bounded by the length of llist_1
6. Overall, this evaluates to space complexity of O(3j + n) --> O(n), since the coefficient 3 can be disregarded and j <= n
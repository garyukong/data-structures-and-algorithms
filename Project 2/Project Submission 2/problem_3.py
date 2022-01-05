import sys

class Node():

    def __init__(self, char = None, freq = None, left = None, right = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def is_leaf(self):
        return (self.left == None) and (self.right == None)

    def __repr__(self):
        return (f"""{self.char}""")

    def __str__(self):
        return (f"""{self.char}""")

def huffman_encoding(string):
    """
    Makes a huffman tree from a string. Uses the following steps and helper functions:

    Phase I: Makes a huffman tree
    1.1 count_chars: Make a dictionary with unique characters and frequencies
    1.2 make_initial_queue: From the dictionary, make an initial queue of characters
    1.3 process_queue: Process queue until there is a single element left in the priority queue

    Phase II: Generate the Encoded data
    2.1 map_path: Make a list containing path from root to leaf node with a given character
    2.2 encode_char: Traverse the path to generate unique binary codes for each character of the string
    2.3 make_binary_map: Create a dictionary mapping characters to individual Huffman codes
    2.4 encode_string: Iterate through all characters in the string to create the Huffman code for the string

    Args:
        string(string): string of alphabetic characters to make a huffman tree from

    Returns:
        tuple containing encoded data (string format, binary code) and the root of the huffman tree (a node object)
    """
    # Phase I helper functions
    # ------------------------------------------------------------------------------------------------------------------
    def count_chars(string):
        """
        Make a dictionary with unique characters and frequencies

        Args:
            string(string): string of alphabetic characters to make a dictionary from

        Returns:
            dictionary with format {character: frequencies}, to serve as input for make_initial_queue
        """
        charCounts = {}
        for char in string:
            if char not in charCounts:
                charCounts[char] = 1
            else:
                charCounts[char] += 1
        return charCounts

    # ------------------------------------------------------------------------------------------------------------------
    def make_initial_queue(charCounts):
        """
        From the dictionary generated in count_chars, create a priority queue containing nodes with characters and frequencies

        Args:
            charCounts(dict): dictionary with format {character: frequencies}

        Returns:
            a 'flat' priority queue, to serve as input to process_queue
        """
        charCounts = dict(sorted(charCounts.items(),key = lambda x: x[1])) # Sort dictionary by frequency
        priorityQueue = []
        for char, freq in charCounts.items():
            new_node = Node(char, freq)
            priorityQueue.append(new_node)
        return priorityQueue
    
    # ------------------------------------------------------------------------------------------------------------------
    def process_queue(priorityQueue):
        """
        Process the priority queue until only one node is left

        Args:
            priorityQueue(list): a 'flat' priority queue where node that
            has lowest frequency have higher priority to be popped-out

        Returns:
            root node of the Huffman tree
        """

        # Helper function to enable re-insertion of nodes into the priority queue
        def insert_node(node, queue):         
            """
            Inserts node into the priority queue at the appropriate position to maintain ordering
            
            Args:
                node(node): node to be inserted into the priority queue
                queue(list): the priority queue
            """
            for i in range(len(queue)):
                if node.freq < queue[i].freq:   # If node to be inserted has lower frequency than a given node in the queue
                    queue.insert(i, node)       # Insert the node at the said node's position
                    return
            queue.append(node)                  # Otherwise, append to the end of the queue
            return
        
        # Repeat until the queue has one element left
        while len(priorityQueue) > 1: 

            # Pop-out two nodes with the minimum frequency from the priority queue
            left = priorityQueue.pop(0)
            right = priorityQueue.pop(0)

            # Create a new node
            new_node = Node(left.char + right.char, left.freq + right.freq, left, right)

            # Insert the node into the priority queue at the relevant position
            insert_node(new_node,priorityQueue)

        return priorityQueue[0]

    # Phase II helper functions
    # ------------------------------------------------------------------------------------------------------------------
    # Helper code to generate path from root to leaf node with a given character
    def map_path(root, char):
        """
        Creates a list containing path from root to leaf node with the given character
        :param: Root of the tree to be traversed
        :param: Character to be searched for    
        """
        def map_path_reversed(root, char):
            # Base case: root is empty
            if root is None:
                return None

            # Base case: root's character is equal to the character being searched for
            elif root.char == char:
                return [char]

            # Traverse left
            leftResult = map_path_reversed(root.left, char)
            if leftResult is not None:
                leftResult.append(root.char)
                return leftResult

            # Traverse right
            rightResult = map_path_reversed(root.right, char)
            if rightResult is not None:
                rightResult.append(root.char)
                return rightResult

        return list(reversed(map_path_reversed(root, char)))

    # Helper code to convert characters to a binary Huffman code
    def encode_char(root, char):
        """
        Returns binary Huffman code for a given character
        
        Args:
            root(Node): Root of the Huffman tree
            char(character): Character to convert to Huffman code
        """
        # Create a list representing the path from the root to the relevant leaf node of the Huffman tree
        traversalPath = map_path(root, char)

        # Initialise variables
        current = root # Set root as the current node
        encoded_data = ''
            
        # Iterate through each item in the pathList (excluding the first item which is the root)
        for chars in traversalPath:
            if current.left.char == chars:
                encoded_data += '0'
                current = current.left # Traverse to the left child
            elif current.right.char == chars:
                encoded_data += '1'      # Add 1 to the encoded_data
                current = current.right # Traverse to the right child

        return encoded_data

    def encode_string(root, charCounts):
        """
        Loop through all characters in the original string to create final Huffman code

        Args:
            root(Node): the root node of the Huffman tree generated from the make_huffman_tree function
            charCounts(dictionary): dictionary containing distinct characters from string as keys
        
        Returns:
            huffman code (string format) for the original input string
        """
        # Create a dictionary with keys representing unique characters and values representing Huffman code for each character
        huffmanMap = {}
        for char in charCounts:
            huffmanMap[char] = encode_char(root, char)

        # Using the dictionary, iterate through the input string to convert it to its huffman code
        output = ''
        for char in string:
            output += huffmanMap[char]
        return output

    # Execute functions
    # ------------------------------------------------------------------------------------------------------------------
    
    # Check that the input contains at least two characters
    if len(string) <= 1:
        raise Exception("Invalid input. String must contain at least two characters. \n")

    # Encode the string
    else:
        charCounts = count_chars(string)
        initialQueue = make_initial_queue(charCounts)
        root = process_queue(initialQueue)
        finalOutput = encode_string(root, charCounts)
        return finalOutput, root

def huffman_decoding(data, root):
    """
    Decode data from binary Huffman code to its alphabetic representation

    Args:
        data(string): encoded data (in binary) to be decoded
        root(Node): root node of the huffman tree used to encode the data

    Returns:
        decoded string in alphabetic format
    """
    # Declare a blank decoded string
    decodedString = ''

    # Set currentNode as root
    currentNode = root

    # Pick a bit from the encoded data, traversing from left to right
    for bit in data:
        
        # If the current bit is 0, move to the left child
        if bit == '0':
            currentNode = currentNode.left

        # If the current bit is 1, move to the right child
        elif bit == '1':
            currentNode = currentNode.right
        
        # If after traversal, the current node is a leaf
        if currentNode.is_leaf():
            decodedString += currentNode.char
            currentNode = root

    return decodedString

if __name__ == "__main__":
    codes = {}

    def encode_and_decode(string):
        print("INPUTTED DATA: {}\n".format(string))

        print ("The size of the data is: {}\n".format(sys.getsizeof(string)))
        print ("The content of the data is: {}\n".format(string))

        encoded_data, root = huffman_encoding(string)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, root)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))

        print ('---------------------------------------------------------------------------------------')

    # EXPECTED RESULTS FOR EACH TEST CASE (UNLESS OTHERWISE MENTIONED):
    ## The size of the decoded data should equal the size of the original input data
    ## The size of the encoded data should be smaller than the size of the original data and decoded data
    ## The encoded data should be a string of binary digits
    ## The decoded data should be a string of alphabets and match the original input data

    # TEST CASE 1 - Encode and decode string with some repeating characters
    encode_and_decode('The bird is the word')

    # TEST CASE 2 - Encode and decode string with distinct alphabetic characters:
    encode_and_decode('ABCDEFG#!@#^')

    # TEST CASE 3 - Encode and decode string with repeated alphabetic characters:
    encode_and_decode('AAAABBBCCCCCDDDEEEEFFFGGGG####!!!@@@@')

    # TEST CASE 4 - Encode and decode string with distinct numbers
    encode_and_decode('1234567890')

    # TEST CASE 5 - Encode and decode string with repeated numbers
    encode_and_decode('11232345556788890')
    
    # TEST CASE 6 - Encode and decode string with single alphabetic character
    encode_and_decode('A')
    # Should return an error and terminate the code as there is no Huffman tree to traverse under this scenario

    # TEST CASE 7 - Encode and decode empty string
    encode_and_decode('')
    # Should return an error as there is no Huffman tree to traverse under this scenario.
    # Note: Need to deactivate TEST CASE 6 before this will run

    # TEST CASE 8 - Encode and decode integers
    encode_and_decode(12345)
    # Should return an error as the code should only work with strings
    # Note: Need to deactivate TEST CASE 7 and TEST CASE 6 before this will run
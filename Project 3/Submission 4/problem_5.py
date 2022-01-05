class TrieNode:

    def __init__(self, char):
        self.char = char
        self.is_word = False
        self.children = {}
    
    def has_child(self):
        return type(self.children) == dict and self.children != {}

class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        """Add 'word' to the trie"""
        # Initiate at the root
        node = self.root

        # Increment through each character in the word
        for char in word:

            # If the character is not a child of the current node
            if char not in node.children:

                # Create a new node for the character
                new_node = TrieNode(char)

                # Set the new node as the child of the current node
                node.children[char] = TrieNode(char)

            # Traverse to the child node for the next character
            node = node.children[char]
        
        # Mark the current_node as a word
        node.is_word = True

    def find(self, node, prefix):
        """Find and return the Trie node that represents this prefix"""
        # Initiate at the root
        node = self.root

        # Increment through each character in the word and traverse through the tree
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        # Return the  node
        return node

    def dfs(self, node, prefix):
        """Depth-first-search algorithm that traverses trees and its subtrees and appends words to self.output"""
        # If the node represents a word, append to the word to the output list
        if node.is_word:
            self.output.append(prefix + node.char)

        # If the node has no children, then return
        if node.has_child() == False:
            return

        # Otherwise, traverse through the node's children
        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def suffixes(self, prefix):
        """Returns all suffixes for words with a matching prefix"""
        # Initiate at the root
        node = self.root

        # If the node has no child (i.e., empty trie)
        if node.has_child() == False:
            return []

        # Traverse the prefix and move down the trie until the end of the prefix
        node = self.find(node, prefix)

        # If the prefix is not present in the trie, return []
        if node == []:
            return []

        # Create an empty list to be populated in depth-first search
        self.output = []

        # Call depth-first search
        self.dfs(node, prefix[:-1])

        # Update elements in the output list to exclude the prefix
        self.output[:] = [x[len(prefix):] for x in self.output if x[len(prefix):] != '']

        return self.output

if __name__ == '__main__':
    def generate_trie(wordList):
        """Generates a trie based on a list of words"""
        trie = Trie()
        for word in wordList:
            trie.insert(word)
        return trie

    def test_function(trie, prefix, answer):
        output = trie.suffixes(prefix)
        print(output)
        if output == answer:
            print("Pass")
        else:
            print("Fail")

    wordList = [
        "ant", "anthology", "antagonist", "antonym", 
        "fun", "function", "factory", 
        "trie", "trigger", "trigonometry", "tripod"
    ]
    testTrie = generate_trie(wordList)
    testTrie.suffixes('Zara')

    # Test case 1: No prefix
    test_function(testTrie, '', ["ant", "anthology", "antagonist", "antonym", "fun", "function", "factory", "trie", "trigger", "trigonometry", "tripod"])

    # Test case 2: Prefix is not a word
    test_function(testTrie, 'an', ['t', 'thology', 'tagonist', 'tonym'])

    # Test case 3: Prefix is a word
    test_function(testTrie, 'fun', ['ction'])

    # Test case 4: Prefix is not in the wordlist
    test_function(testTrie, 'zara', [])

    emptyTrie = generate_trie([])

    # Test case 5: Empty tree
    test_function(emptyTrie, 'fun', [])
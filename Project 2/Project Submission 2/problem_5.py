import hashlib
import datetime

class Block():
    
    def __init__(self, data):
        self.index = 0
        self.timestamp = self.calc_timestamp()
        self.data = data
        self.previous_hash = None
        self.hash = self.calc_hash(data)
        self.previous = None

    def calc_timestamp(self):
        """ Returns the current timestamp """
        return datetime.datetime.now()

    def calc_hash(self, data):
        """ Returns the hash to create a new block """
        if type(data) != str:
            raise TypeError("Data must be a string")
            
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_hash_tuple(self):
        """ Returns a tuple containing the previous hash and the hash of the block """
        hash_tuple = (self.previous_hash, self.hash)
        return hash_tuple

    def get_block_parameters(self):
        """ Returns a string containing all variables of the block"""
        return (f"""i: {self.index} | TS: {self.timestamp} | D: {self.data} | PH: {self.previous_hash} | H: {self.hash}""")
        
    def __repr__(self):
        return self.data

    def __str__(self):
        return self.data

class Blockchain():

    def __init__(self):
        self.tail = None

    def append_data(self, data):
        """ Add a block to the end of the blockchain """
        new_tail = Block(data)

        # If there are no blocks in the blockchain, set new block as the tail
        if self.tail is None:
            self.tail = new_tail
            return

        # Otherwise:
        else:
            # Update the index of the new tail
            new_tail.index = self.tail.index + 1

            # Set the previous hash of the current tail as the new tail's hash
            new_tail.previous_hash = self.tail.hash

            # Set the new tail's to point to the current tail
            new_tail.previous = self.tail

            # Set the new tail as the current tail
            self.tail = new_tail
            return

    def append_list(self, data_list):
        """ Adds all elements from a list of data as blocks to the end of the blockchain """
        for data in data_list:
            self.append_data(data)
        return

    def search_hash(self, hash):
        """ Search the blockchain for the latest block with the requested hash and return the block """
        if self.tail is None:
            return None

        # Traverse the blockchain until a block with a matching hash is found
        current_block = self.tail
        while current_block:
            if current_block.hash == hash:
                return current_block
            current_block = current_block.previous
        
        raise ValueError("Hash not found in the blockchain")

    def search_data(self, data):
        """ Search the blockchain for the latest block with the requested data and return the block """
        if self.tail is None:
            return None

        # Traverse the blockchain until a block with a matching hash is found
        current_block = self.tail
        while current_block:
            if current_block.data == data:
                return current_block
            current_block = current_block.previous
        
        raise ValueError("Data not found in the blockchain")

    def search_index(self, index):
        """ Search the blockchain for a block with the requested index and return the block """
        if self.tail is None:
            return None

        # Traverse the blockchain until a block with a matching index is found
        current_block = self.tail
        while current_block:
            if current_block.index == index:
                return current_block
            current_block = current_block.previous
        
        raise ValueError("Index out of range")

    def get_timestamps(self):
        """ Returns a list of timestamps for each block in the blockchain """
        output_list = []
        current_block = self.tail
        while current_block:
            output_list.append(current_block.timestamp)
            current_block = current_block.previous
        output_list.reverse()
        return output_list

    def get_previous_hashes(self):
        """ Returns a list of previous hashes for each block in the blockchain """
        output_list = []
        current_block = self.tail
        while current_block:
            output_list.append(current_block.previous_hash)
            current_block = current_block.previous
        output_list.reverse()
        return output_list

    def get_hashes(self):
        """ Returns a list of hashes for each block in the blockchain """
        output_list = []
        current_block = self.tail
        while current_block:
            output_list.append(current_block.hash)
            current_block = current_block.previous
        output_list.reverse()
        return output_list

    def get_hash_tuples(self):
        """ Returns a list of tuples of (previous_hash, hash) for each block in the blockchain """
        output_list = []
        current_block = self.tail
        while current_block:
            output_list.append(current_block.get_hash_tuple())
            current_block = current_block.previous
        output_list.reverse()
        return output_list

    def get_all_details(self):
        """
        Returns a list with all details of each block in the blockchain:
        i = index, TS = timestamp, D = data, PH = previous hash, H = hash        
        """
        output_list = []
        current_block = self.tail
        while current_block:
            output_list.append(current_block.get_block_parameters())
            current_block = current_block.previous
        output_list.reverse()
        return output_list

    def __len__(self):
        """ Returns the number of blocks in the blockchain """

        # Traverse the blockchain and increment length for each block
        length = 0
        current_block = self.tail
        while current_block:
            length += 1
            current_block = current_block.previous
        return length

    def __repr__(self):
        """ Returns a list of data for each block in the blockchain """
        output_list = []
        current_block = self.tail
        while current_block:
            output_list.append(current_block.data)
            current_block = current_block.previous
        output_list.reverse()
        return str(output_list)

if __name__ == "__main__":
    # Helper functions for test cases
    def test_hashes(blockchain):
        """ Tests whether all previous_hash values point to hash values of previous blocks"""
        hashes = blockchain.get_hashes()
        previous_hashes = blockchain.get_previous_hashes()
        for i in range(len(blockchain)-1):
            if hashes[i] != previous_hashes[i+1]:
                return (f"""FAIL. At index {i}, hash: {hashes[i]} does not match previous_hashes[i+1]: {previous_hashes[i+1]}""")
        return "PASS: All previous_hash values are equal to hash values of previous blocks"

    def test_length(blockchain, correct_length):
        """ Tests whether the blockchain's length matches correct_length """
        blockchain_length = len(blockchain)
        if blockchain_length == correct_length:
            return (f"""PASS. Blockchain length: {blockchain_length} blocks""")
        return (f"""FAIL. Blockchain length: {blockchain_length} blocks""")

    def test_search_hash(blockchain, hash, correct_index):
        """ Tests whether the block.index value returned by the search_hash(hash) function matches the correct_index """
        block = blockchain.search_hash(hash)
        if block.index == correct_index:
            return (f"""PASS. Searched hash {hash} and returned block index {block.index}""")
        return (f"""FAIL. Searched hash {hash} and returned block index {block.index}""")

    def test_search_data(blockchain, data, correct_index):
        """ Tests whether the block.index value returned by the search_data(data) function matches the correct_index """
        block = blockchain.search_data(data)
        if block.index == correct_index:
            return (f"""PASS. Searched for data {data} and returned block index {block.index}""")
        return (f"""FAIL. Searched for data {data} and returned block index {block.index}""")

    def test_search_index(blockchain, index, correct_data):
        """ Tests whether the block.data value returned by the search_index(index) function matches the correct_data """
        block = blockchain.search_index(index)
        if block.data == correct_data:
            return (f"""PASS. Searched index {index} and returned block with data {block.data}""")
        return (f"""FAIL. Searched index {index} and returned block with data {block.data}""")

    #------------------------------------------------------------------------------------------------#

    # TEST CASE 1: STANDARD CASE
    print("\nTEST CASE 1: STANDARD CASE")
    
    testbc = Blockchain()
    testbc.append_list(['SOL', 'LUNA', 'BTC', 'ETH'])

    # Manual check to see that all functions to display the blockchain works:
    print(f"""(All details): {testbc.get_all_details()}""") # Should list all details of the blocks in the blockchain
    print(f"""(Default view): {testbc}""") # Should list data of each node in the blockchain (['SOL', 'LUNA', 'BTC', 'ETH'])
    print(f"""(Previous hashes): {testbc.get_previous_hashes()}""") # Should return a list with all previous hash values
    print(f"""(Hashes): {testbc.get_hashes()}""") # Should return a list with all hash values
    print(f"""(Previous hashes, hashes): {testbc.get_hash_tuples()}""") # Should return a list of tuples of previous_hash, hash values

    print()
    print(test_hashes(testbc)) # Previous hash values for each block should be equal to hash value of preceding block
    print(test_length(testbc, 4)) # Should return 4

    testbc.append_data('BTC')

    print(test_length(testbc, 5)) # Should return 5
    print(test_search_index(testbc, 4, 'BTC')) # Should return the block with Data: 'BTC'
    print(test_search_hash(testbc, 'da8562e7abc01a6f0d49a25d144ce6a9d7752a079c5d950ad5a93fd6d623f7fd', 4)) # Should return the block with index 4
    print(test_search_data(testbc, 'SOL', 0)) # Should return the block with index 0 since 'SOL' was added first

    #------------------------------------------------------------------------------------------------#

    # TEST CASE 2: BLOCKCHAIN WITH BLOCKS CONTAINING DUPLICATE ITEMS
    print("\nTEST CASE 2: BLOCKCHAIN WITH BLOCKS CONTAINING DUPLICATE ITEMS")
    testbc = Blockchain()
    testbc.append_list(['BTC', 'BTC', 'BTC', 'ETH', 'ETH', 'ETH'])

    print(test_hashes(testbc)) # Previous hash values for each block should be equal to hash value of preceding block
    print(test_length(testbc, 6)) # Should return 6

    testbc.append_data('BTC')

    print(test_length(testbc, 7)) # Should return 7
    print(test_search_index(testbc, 6, 'BTC')) # Should return the block with Data: 'BTC'
    print(test_search_hash(testbc, 'da8562e7abc01a6f0d49a25d144ce6a9d7752a079c5d950ad5a93fd6d623f7fd', 6)) # Should return the block with index 6
    print(test_search_data(testbc, 'ETH', 5)) # Should return the block with index 5

    #------------------------------------------------------------------------------------------------#

    # TEST CASE 3: BLOCKCHAIN WITH LARGE NUMBER OF ITEMS (1,000,000 numbers)
    print("\nTEST CASE 3: BLOCKCHAIN WITH LARGE NUMBER OF ITEMS (1,000,000 numbers)")
    testbc = Blockchain()
    data_list = [str(i) for i in range(1000000)]
    testbc.append_list(data_list)

    print(test_hashes(testbc)) # Previous hash values for each block should be equal to hash value of preceding block
    print(test_length(testbc, 1000000)) # Should return 500000

    print(test_search_index(testbc, 1, '1')) # Should return the block with Data: '1'
    print(test_search_hash(testbc,testbc.search_index(5).hash,5)) # Should return the block with index 5
    print(test_search_data(testbc, '0', 0)) # Should return the block with index 0
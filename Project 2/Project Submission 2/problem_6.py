class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

def union(llist_1, llist_2):
    """ Returns a set in the form of a linked list representing the union of llist_1 and llist_2 """
    
    # Create an empty set
    union_set = set()

    # Traverse through each element of llist_1, adding each element to the set
    node = llist_1.head
    while node:
        union_set.add(node.value)
        node = node.next

    # Do the same for llist_2
    node = llist_2.head
    while node:
        union_set.add(node.value)
        node = node.next

    # Iterate through each element of the (sorted) set and convert to a linked list
    out = LinkedList()
    for element in sorted(union_set):
        out.append(element)
    
    return out
    
def intersection(llist_1, llist_2):
    """ Returns a set in the form of a linked list representing the intersection of llist_1 and llist_2 """
    
    # Create a dictionary based on all elements of llist_1 where keys are elements of llist
    intersection_dict = {}
    node = llist_1.head
    while node:
        intersection_dict[node.value] = 0
        node = node.next

    # Flag values as 1 if the key appears in llist_2
    node = llist_2.head
    while node:
        if node.value in intersection_dict.keys():
            intersection_dict[node.value] = 1
        node = node.next

    # Create a new array containing all keys in the dictionary where 1 is the value
    intersection_array = [key for key, value in intersection_dict.items() if value == 1]

    # Iterate through the sorted array to create a new linked list containing intersection elements
    out = LinkedList()
    for element in sorted(intersection_array):
        out.append(element)
    
    return out

if __name__ == "__main__":
    def test_function(list_1, list_2):
        """ Helper function to generate linked lists and test union and intersection functions"""
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        for i in list_1:
            linked_list_1.append(i)

        for i in list_2:
            linked_list_2.append(i)

        print (f"""Union: {union(linked_list_1,linked_list_2)}""")
        print (f"""Intersection: {intersection(linked_list_1,linked_list_2)}""")

    # ----------------------------------------------------------------------------------------------
    # TEST CASE 1 
    print ('\nTEST CASE 1: TWO LINKED LISTS THAT INTERSECT')
    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]
    test_function(element_1, element_2)
    # Union should return 1 -> 2 -> 3 -> 4 -> 6 -> 9 -> 11 -> 21 -> 32 -> 35 -> 65 -> 
    # Intersection should should return 4 -> 6 -> 21

    # ----------------------------------------------------------------------------------------------
    # TEST CASE 2
    print ('\nTEST CASE 2: TWO LINKED LISTS THAT DO NOT INTERSECT')
    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]
    test_function(element_1, element_2)
    # Union should return 1 -> 2 -> 3 -> 4 -> 6 -> 7-> 8 -> 9 -> 11 -> 21 -> 23 -> -> 35 -> 65 -> 
    # Intersection should return an empty linked list as no elements intersect

    # ----------------------------------------------------------------------------------------------
    # TEST CASE 3
    print ('\nTEST CASE 3: TWO EMPTY LINKED LISTS')
    element_5 = []
    element_6 = []
    test_function(element_5, element_6)
    # Union should return an empty linked list as there are no elements in either input lists
    # Intersection should return an empty linked list as no elements intersect

    # ----------------------------------------------------------------------------------------------
    # TEST CASE 4
    print ('\nTEST CASE 4: TWO LINKED LISTS COMPOSED OF STRINGS (NOT NUMBERS) THAT INTERSECT')
    element_7 = ['a','a','a','b','c','d','e','e','e','f','g']
    element_8 = ['e','e','e','f','g','h','i','i','i','j','k','l']
    test_function(element_7, element_8)
    # Union should return a -> b -> c -> d -> e -> f -> g -> h -> i -> j -> k -> l
    # Intersection should return 'e' -> 'f' -> 'g'

    # ----------------------------------------------------------------------------------------------
    # TEST CASE 5
    print ('\nTEST CASE 5: TWO LINKED LISTS: ONE COMPOSED OF NUMBERS, THE OTHER OF STRINGS')
    element_9 = [1,1,1,2,3,4,5,6,7,9]
    element_10 = ['e','e','e','f','g','h','i','i','i','j','k','l']
    test_function(element_9, element_10)
    # Both union and intersection should return an error as the 'sorted' command
    # applied to the arrays in both functions cannot compare numbers and strings
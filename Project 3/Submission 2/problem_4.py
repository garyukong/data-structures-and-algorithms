def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # Initialise the position of where 0s should go and where 2s should go
    next_0 = 0
    next_2 = len(input_list) - 1

    # Initialise current index at 0
    current = 0

    # Iterate until all 2s have been moved to the end of the array
    while current <= next_2:
        
        # If the current element is a 2:
        if input_list[current] == 2:
            input_list[current], input_list[next_2] = input_list[next_2], input_list[current] # Flip position with element at next_2
            next_2 -= 1                                                                       # Decrement next_2

        # If the current element is a 0:
        elif input_list[current] == 0:
            input_list[current], input_list[next_0] = input_list[next_0], input_list[current] # Flip position with element at next_0
            next_0 += 1                                                                       # Increment next_0
            current +=1                                                                       # Increment current

        # If the current element is a 1:
        elif input_list[current] == 1:
            current += 1                                                                      # Increment current

        # If a number other than 0, 1, 2 is given then raise an exception
        else:
            raise Exception("Invalid input: Please only enter 0s, 1s and 2s")

    return input_list

if __name__ == "__main__":    
    def test_function(test_case):
        sorted_array = sort_012(test_case)
        print(sorted_array)
        if sorted_array == sorted(test_case):
            print("Pass")
        else:
            print("Fail")

    # Standard cases
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

    # Edge cases
    test_function([])
    test_function([1,2,3,4,5,6,7,8,9]) # Should raise an exception as numbers other than 0, 1, 2 were inserted
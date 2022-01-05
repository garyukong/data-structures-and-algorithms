def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # Initiate min and max each as the first number in the list
    min = ints[0]
    max = ints[0]

    # Iterate through the list, doing comparisons and updating min and max vals
    for int in ints:
        if int < min:
            min = int
        if int > max:
            max = int

    return (min, max)

if __name__ == '__main__':

    import random

    # Test case 1 - a list containing 0 to 9
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

    # Test case 2 - a list containing only 1s
    l = [1 for i in range(0, 10)]
    random.shuffle(l)
    print ("Pass" if ((1, 1) == get_min_max(l)) else "Fail")

    # Test case 3 - a list containing empty values
    l = [None for i in range(0, 10)]
    random.shuffle(l)
    get_min_max(l) # Should return an error as comparisons cannot be done on empty values
def find_pivot(arr, low, high):
    """
    Find the pivot in a rotated sorted array

    Args:
        arr(array): Rotated sorted array to find pivot in
        low(int): Lower boundary index of the array
        high(int): Upper boundary index of the array
    Returns:
        int: Index or -1
    """
    # Base cases
    if high < low:
        return -1

    if high == low:
        return low

    mid = int((low + high)/2)
    
    # Case 1: Pivot is the midpoint 
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid

    # Case 2: Pivot is midpoint - 1
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)

    # Case 3: Pivot is to the left of the midpoint
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid-1)
    
    # Case 4: Pivot is to the right of the midpoint
    return find_pivot(arr, mid + 1, high)

def binary_search(arr, low, high, number):
    """
    Find the index of a target in a sorted array by running a binary search

    Args:
        arr(array): Sorted array
        low(int): Lower boundary index of the array
        high(int): Upper boundary index of the array
        number(int): Number to search in the array
    Returns:
        int: Index or -1
    """

    # Case 1: length of the array is less than 1 (value not found)
    if high < 1:
        return -1

    # Find midpoint
    mid = int((low + high)/2)

    # Case 2: midpoint is the target
    if number == arr[mid]:
        return mid

    # Case 3: number is greater than the midpoint
    if number < arr[mid]:
        return binary_search(arr, low, mid - 1, number)

    # Case 4: number is smaller than the midpoint
    if number > arr[mid]:
        return binary_search(arr, mid + 1, high, number)

def rotated_array_search(arr, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       arr(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Find pivot
    pivot = find_pivot(arr, 0, len(arr)-1)

    # If the array is not rotated, run a normal binary search
    if pivot == -1:
        return binary_search(arr, 0, len(arr)-1, number)

    # Based on the pivot, calculate minimum and maximum values of the array
    min_val = arr[pivot + 1]    # Min value is 1 element to the right of the pivot
    max_val = arr[pivot]        # Max value is the pivot
    last_val = arr[-1]

    # If target is the pivot
    if number == max_val:
        return pivot

    # If target is to the right of the pivot:
    if min_val <= number <= last_val:
        return binary_search(arr, pivot+1, len(arr)-1, number)

    # If target is to the left of the pivot:
    if number < max_val:
        return binary_search(arr, 0, pivot, number)

    return -1


if __name__ == "__main__":

    def linear_search(input_list, number):
        for index, element in enumerate(input_list):
            if element == number:
                return index
        return -1
        
    def test_function(test_case):
        input_list = test_case[0]
        number = test_case[1]
        if linear_search(input_list, number) == rotated_array_search(input_list, number):
            print("Pass")
        else:
            print("Fail")

    # Normal cases
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])

    # Edge cases
    test_function([[], 10])
    test_function([[8,9,1,3,2,5,10], 10])
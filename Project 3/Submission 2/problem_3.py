def reverse_mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = reverse_mergesort(left)
    right = reverse_mergesort(right)
    
    return reverse_merge(left, right)
    
def reverse_merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) >= 2:
        
        # Sort the input list in descending order
        sorted_input_list = reverse_mergesort(input_list)

        # Create an empty output list for the two maximum sums
        out = ['','']

        # Iterate through elements of the sorted list
        for index, element in enumerate(sorted_input_list):

            ## If index is even, concatenate to the first cell of the output list
            if index % 2 == 0:
                out[0] += str(element)

            # If index is odd, concatenate to the second cell of the output list
            else:
                out[1] += str(element)

        # Convert output list into a list of integers
        out[0], out[1] = int(out[0]), int(out[1])

        return out

if __name__ == "__main__":
    
    def test_function(test_case):
        output = rearrange_digits(test_case[0])
        solution = test_case[1]
        if output == solution:
            print("Pass")
        else:
            print("Fail")

    # Normal cases
    test_function([[1, 2, 3, 4, 5], [531, 42]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
    test_function([[9, 9, 9, 9, 9], [999, 99]])

    # Edge cases
    test_function([[], None])   # Empty element
    test_function([[0], None])  # Single element
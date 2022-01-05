# Problem 1: Floored Square Root
## Design considerations
Binary search was used as it allows us to find the square root in O(log N) time, as opposed to O(n) time if we were to iterate through each number that could be the square root of the input number.

Binary search also allows us to find the floor square root. Because a lower bound is stored in memory through a binary search algorithm, it is possible to find the floor square root for numbers that do not have integer square roots, through the condition:

    mid - lower < 1:
        return lower

i.e., if a further recursive call were to produce a midpoint that was not an integer, then we know to take the lower value as the result

## Time complexity
Time complexity is O(log n). Each recursive call leads to the halving of the range that the binary search has to conduct such that there will be a total of log n recursive calls (and hence each operation has to occur log N times)

## Space complexity
Space complexity is O(log N):
- Input space complexity is O(1) as the number inserted will always be an integer that occupies the same amount of memory.
- Auxiliary space complexity is O(log n). In the worst case, there will be log n recursive calls and all these calls will be stored in the call stack and utilise memory.

# Problem 2: Search in rotated sorted array

## Design considerations
The find_pivot function takes advantage of the fact that  the pivot will be the only occurrence in the array in arr[i] > arr[i+1]. Using this property, we can simply recurse through the function until this condition is met.

I initially considered using the pivot to create a new sorted array, before conducting a binary search on the new sorted array but decided against this to reduce complexity. Instead, the rotated_array_search function takes advantage of the fact that the maximum value of the array corresponds to the pivot, and the minimum value of the array corresponds to value to the right of the pivot. Using these properties, we can do a divide and conquer strategy to determine whether the target number is to the right or the left of the pivot, and recurse using binary search accordingly.

## Time complexity
Time complexity of rotated_array_search is O(log N):
- Complexity of the function is driven by the calls to find_pivot and binary_search
- Both find_pivot and binary_search runs in O(log N) time. Complexity is driven by the recursive calls, and each recursive call halves the length of the array, such that the number of recursive calls will equal log N

## Space complexity
Space complexity of rotated_array_search is O(log N):
- Input space complexity is O(N) where N refers to the length of the array
- Auxiliary space complexity is O(log N) and is driven by recursive calls of the find_pivot and binary_search function. Memory used by the call stack will equal the number of recursive calls (log N)

# Problem 3: Rearrange array elements

## Design considerations
The function takes into consideration the fact that the maximum sum of two numbers made out of a elements of array will occur when the largest digits in the array are used as the first digits of the two numbers, respectively, the next two largest digits are used as the next digits of the two numbers, respectively, and so forth e.g.,
- The two largest digits are 6 and 5. Therefore, 6 and 5 are the first digits of the two numbers, respectively --> number 1 = 6XX, number2 = 5XX (X refers to unknown digits)
- The next largest digits are 4 and 3. Therefore, 4 and 3 are the second digits of the two numbers --> number 1 = 64X, number 2 = 53X
- The smallest digits are 2 and 1. Therefore, 2 and 1 are the last digits of the two numbers, respectively --> number 1 = 642, number 2 = 531

To accomplish this, the input array is first sorted in descending order using mergesort, which has the benefit of having O(N log N) time complexity. As an alternative to mergesort, heap sort could also have been used as it also runs in O(N log N)

## Time complexity
Time complexity is O(N log N):
- The call to the reverse_mergesort function runs in O(N log N) time:
    - First, the array is broken into two sub-arrays through recursive reverse_mergesort calls. This runs in O(log N) time as the size of the array is halved in each cursive call (such that the total number of recursive calls should equal log N).
    - Each recursive call also makes a call to the reverse_merge function, which runs in O(N) time owing to the use of a while loop
- Thereafter, rearrange_digits iterates through the elements of the sorted list using a for loop, which has time complexity of O(N)

## Space complexity
Space complexity is O(N log N), namely driven by the call to the reverse_mergesort function:
- The reverse_mergesort function makes two recursive calls. The maximum depth of recursion (impacting use of space in the call stack) is in the order of log N as the size of the array is halved in each recursive call --> O(log N)
- In each recursvie call, an array is created which has a maximum length of n --> O(n)

# Problem 4: Dutch national flag problem

## Design considerations
Sorting 0s, 1s and 2s in a single array traversal was accomplished using pointers corresponding to next positions for 0s and 2s. In addition to minimising the number of operations by only traversing the array once, the algorithm has the benefit of allowing in-place sorting, thus not requiring any additional memory to be used beyond the input array itself.

## Time complexity
Time complexity is O(n), driven by the while loop:
- In the average case, the number of iterations should be less than n as current only needs to intersect with next_2, and next_2 will keep decrementing each time the current element is a 2
- The worst case would be where there are no 2s in the array, such that next_2 never decrements

## Space complexity
Space complexity is O(n):
- Input space complexity is O(n) since the input is an array which can very in length and thus memory used
- Auxiliary space complexity is O(1) due to use of in-place sorting

# Problem 5: Autocomplete using Trie

## Design considerations
The suffixes function makes use of a depth-first search algorithm. Each recursive call to the dfs algorithm uses prefix + node.char as an argument.  Concatenating the prefix with the character of each node allows the 'prefix' argument of suffixes to act as a cache for the characters traversed in each branch of the trie, before appending whatever is stored in this 'cache' whenever a node's is_word value is True.

## Time complexity
Time complexity of the suffixes function is O(n) where n refers to the number of nodes in the trie
- In line 78, the call to the find function has time-complexity of O(i) where i refers to the length of the prefix, due to the use of a for loop in the function iterating through each character of the prefix
- In line 88, the call to the dfs function has time-complexity of O(j) where j refers to the number of nodes in the trie, as each node in the trie will be traversed through this function
- In line 91, updating the output list has time-complexity of O(k) where n refers to the number of words in the trie
- Both the number of characters in the prefix (i) and the number of words in the trie (k) will never exceed the number of characters / nodes in the trie (j). Since i <= j and k <= j, O(i + j + k) = O(3j) -> O(n) where n refers to the number of nodes in the trie

## Space complexity
Space complexity is O(n) where n refers to the number of nodes in the trie
- Input space complexity is O(i) where i refers to the number of nodes in the trie. Input space complexity for the prefix input is O(1) since prefix is a string which will occupy 256 bytes of memory irrespective of the number of characters
- Auxiliary space complexity is O(k) where k refers to the number of words in the trie
    - DFS has auxiliary space complexity of O(j) where j refers to the height of the trie
    - Creation of the self.output list has auxiliary space complexity of O(k) where k refers to the number of words in the trie
    - j <= k so j can be disregarded here
- k < i so overall space complexity is O(i) --> O(n) where n refers to the number of nodes in the trie

# Problem 6: Unsorted integer array

## Design considerations
A simple for loop was used with two variables stored (min and max) instead of using a sorting algorithm as it allows for a single traversal and the algorithm to run in O(n) time

## Time complexity
Time complexity is O(n) where n refers to the number of values in the list, due to the use of a single for loop

## Space complexity
Space complexity is O(n):
- Input space complexity is O(n) as the input size (the list) can differ depending on the length of the list
- Auxiliary space complexity is O(1) as the number of new objects created is agnostic of the length of the list. There is only also a single function call as no recursion is used

# Problem 7: HTTP router using a trie

## Design considerations
Recursion was used for the RouteTrie class' insert and find functions. Whilst it would have been possible to accomplish the same functionality using iterative functions, recursion has the added benefit of simpler code here.

It is notable that whilst the Router and RouteTrie classes were separated here, there is currently some redundancy. It would have been possible to further simplify the overall code by merging the code found under the Router class into RouteTrie. Calling of the split_path function could have been done in the insert and find functions (instead of doing so in the add_handler and lookup functions), which would have removed the need to have separate add_handler and lookup functions since the insert and find functions would accomplish the same functionality.

## Split_path complexity
Time complexity is O(n) where n refers to the number of parts in the path, owing to the use of a for loop

Space complexity is O(n) where n refers to the number of parts in the path, as the function creates a new array called path_parts whose length depend on the number of parts

## Add_handler complexity
Time complexity is O(n) where n refers to the number of parts in the path
- As above, the call to the split_path function runs in O(n) time
- The call to the insert function runs in O(n) time as the number of recursive calls made would equal the number of parts in the path (i.e., the length of the array generated by the split_path function)

Space complexity is O(n) where n refers to the number of parts in the path
- As above, split_path space complexity is O(n)
- Space complexity for the insert function is O(n), as the size of the call stack depends on the number of recursive calls made

## Lookup complexity
Time complexity is O(n), and space complexity is O(n) where n refers to the number of parts in the path. The same rationale for add_handler applies as the lookup function makes a call to the split_path function, and then the find function, which recurses through the trie based on the number of parts in the path
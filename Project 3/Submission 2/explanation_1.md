# Problem 1: Floored Square Root
## Design considerations
Binary search was used as it allows us to find the square root in O(log N) time, as opposed to O(n) time if we were to iterate through each number that could be the square root of the input number.

Binary search also allows us to find the floor square root. Because a lower bound is stored in memory through a binary search algorithm, it is possible to find the floor square root for numbers that do not have integer square roots, through the condition:

    mid - lower < 1:
        return lower

i.e., if a further recursive call were to produce a midpoint that was not an integer, then we know to take the lower value as the result

## Complexity
Time complexity is O(log n). Each recursive call leads to the halving of the range that the binary search has to conduct such that there will be a total of log n recursive calls (and hence each operation has to occur log N times)

Space complexity is O(log N):
- Input space complexity is O(1) as the number inserted will always be an integer that occupies the same amount of memory
- Auxiliary space complexity is O(log n). In the worst case, there will be log n recursive calls and all these calls will be stored in the call stack and utilise memor

# Problem 2: Search in rotated sorted array

## Design considerations
The find_pivot function takes advantage of the fact that  the pivot will be the only occurrence in the array in arr[i] > arr[i+1]. Using this property, we can simply recurse through the function until this condition is met.

I initially considered using the pivot to create a new sorted array, before conducting a binary search on the new sorted array but decided against this to reduce complexity. Instead, the rotated_array_search function takes advantage of the fact that the maximum value of the array corresponds to the pivot, and the minimum value of the array corresponds to value to the right of the pivot. Using these properties, we can do a divide and conquer strategy to determine whether the target number is to the right or the left of the pivot, and recurse using binary search accordingly.

## Complexity
Time complexity of rotated_array_search is O(log N):
- Complexity of the function is driven by the calls to find_pivot and binary_search
- Both find_pivot and binary_search runs in O(log N) time. Complexity is driven by the recursive calls, and each recursive call halves the length of the array, such that the number of recursive calls will equal log N

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

## Complexity
Time complexity is O(N log N):
- The call to the reverse_mergesort function runs in O(N log N) time:
    - First, the array is broken into two sub-arrays through recursive reverse_mergesort calls. This runs in O(log N) time as the size of the array is halved in each recursive call (such that the total number of recursive calls should equal log N).
    - Each recursive call also makes a call to the reverse_merge function, which runs in O(N) time owing to the use of a while loop
- Thereafter, rearrange_digits iterates through the elements of the sorted list using a for loop, which has time complexity of O(N)

Space complexity is O(n):
- Reverse_mergesort has space complexity of O(n). In each recursive call, the reverse_mergesort function copies values into a new array of size n. However, arrays are deleted at each step so we only need two arrays at any point in time: the original array and the array that the original array is copied into
- The rest of the code has space complexity of O(1) as it involves creation of a new array called out of constant length (2 elements)

# Problem 4: Dutch national flag problem

## Design considerations
Sorting 0s, 1s and 2s in a single array traversal was accomplished using pointers corresponding to next positions for 0s and 2s. In addition to minimising the number of operations by only traversing the array once, the algorithm has the benefit of allowing in-place sorting, thus not requiring any additional memory to be used beyond the input array itself.

## Complexity
Time complexity is O(n), driven by the while loop:
- In the average case, the number of iterations should be less than n as current only needs to intersect with next_2, and next_2 will keep decrementing each time the current element is a 2
- The worst case would be where there are no 2s in the array, such that next_2 never decrements

Space complexity is O(1) due to use of in-place sorting (i.e., no new arrays are created in running the algorithm)

# Problem 5: Autocomplete using Trie

## Design considerations
The suffixes function makes use of a depth-first search algorithm. Each recursive call to the dfs algorithm uses prefix + node.char as an argument.  Concatenating the prefix with the character of each node allows the 'prefix' argument of suffixes to act as a cache for the characters traversed in each branch of the trie, before appending whatever is stored in this 'cache' whenever a node's is_word value is True.

## Complexity

### insert()
insert() runs is O(i) time where n refers to the length of the word being inserted, due to use of a for loop iterating through each character of the word

insert() has space complexity of O(i) where n refers to the length of the word being inserted. In the worst case (i.e., the trie is currently empty), the number of new nodes added to the trie will equal the number of characters in the inputted word.

### find()
find() runs in O(j) time where n refers to the length of the prefix, due to use of a for loop iterating through each character of the prefix

find() has space complexity of O(1) as no new objects are created by the function

### dfs()
dfs() runs in O(n) time where n refers to number of nodes in the trie

dfs() has space complexity of O(n) where n refers to the number of nodes in the trie:
- Auxiliary space used by the call stack is O(j) where j refers to depth of the trie
- Auxiliary space used by the self.output list is O(k) where n refers to the number of words in the trie
- the depth of the trie (j) and number of words in the trie (k) can be approximated by n, the number of nodes in the trie, since j <= n and k <= n

### suffixes()
suffixes() runs in O(n) time where n refers to the number of nodes in the trie:
- suffixes() initially calls the find() and dfs() functions, whose time complexities are O(j) and O(n), respectively, where j = length of the prefix, n = number of nodes in the trie
- suffixes() then updates elements in the output list to exclude the prefix using a for loop:

        self.output[:] = [x[len(prefix):] for x in self.output if x[len(prefix):] != '']

    This has time complexity of O(k) where l refers to the number of words in the trie. In the worst-case, the length of self.output will equal the total number of words in the trie

- From the above statements, time complexity of suffixes() is O(j + k + n)
- j <= n and k <= n so O(j + n + l) -> O(3n) -> O(n) where n refers to the number of nodes (i.e., characters) in the trie

suffixes() has space complexity of O(n) where n refers to the number of nodes in the trie:
- in addition to making calls to find() and dfs(), which has space complexity of O(1) and O(n) respectively, suffixes updates elements in the output list to exclude the prefix:

        self.output[:] = [x[len(prefix):] for x in self.output if x[len(prefix):] != '']

    This has space complexity of O(1) as the output list is updated in-place

# Problem 6: Unsorted integer array

## Design considerations
A simple for loop was used with two variables stored (min and max) instead of using a sorting algorithm as it allows for a single traversal and the algorithm to run in O(n) time

## Complexity
Time complexity is O(n) where n refers to the number of values in the list, due to the use of a single for loop

Space complexity is O(1) as the number and size of new objects (the min and max variables) created is agnostic of the length of the list. There is also only a single function call as no recursion is used so the size of the call stack will be constant.

# Problem 7: HTTP router using a trie

## Design considerations
Recursion was used for the RouteTrie class' insert and find functions. Whilst it would have been possible to accomplish the same functionality using iterative functions, recursion has the added benefit of simpler code here.

It is notable that whilst the Router and RouteTrie classes were separated here, there is currently some redundancy. It would have been possible to further simplify the overall code by merging the code found under the Router class into RouteTrie. Calling of the split_path function could have been done in the insert and find functions (instead of doing so in the add_handler and lookup functions), which would have removed the need to have separate add_handler and lookup functions since the insert and find functions would accomplish the same functionality.

## Complexity

### insert_recursively() / insert()
Time complexity is O(n) where n refers to the number of elements in the input array, as the function will recur until length of the array == 0, reducing the length of the array by 1 in each recursive call

Space complexity is O(n) as both the maximum size of the call stack, and hence the number of nodes added to the trie depends on the number of recursive calls, which is in the order of n

### find_recursively() / find()
Time complexity is O(n) where n refers to the number of elements in the input array, as the function will continue to recur until length of the array == 0, reducing the length of the array by 1 in each recursive call 

Space complexity is O(n) as the maximum size of the call stack depends on the number of recursive calls, which is in the order of n

## split_path()
Time complexity is O(n) where n refers to the number of parts of the path, due to use a for loop iterating through each part of the path

Space complexity is O(n) where n refers to the number of parts in the path, as the function creates a new array called path_parts whose length depend on the number of parts

## add_handler()
Time complexity is O(n) where n refers to the number of parts in the path:
- split_path() runs in O(i) time where i refers to the number of parts of the path, and returns an array of elements where each element represent a part of a path
- insert() runs in O(j) time where j refers to the number of elements in the input array
- j = i so add_handler() runs in O(n) time

Space complexity is O(n) where n refers to the number of parts in the path:
- split_path has space complexity of O(i) where i refers to the number of parts of the path
- insert() has space complexity of O(j) where j refers to the number of elements in the input array
- as above, j = i so add_handler has space complexity of O(n)

## lookup()
Time complexity is O(n) where n refers to the number of parts in the path:
- split_path() runs in O(i) time where i refers to the number of parts of the path, and returns an array of elements where each element represent a part of a path
- find() runs in O(j) time where j refers to the number of elements in the input array
- j = i so lookup() runs in O(n) time

Space complexity is O(n) where n refers to the number of parts in the path:
- split_path has space complexity of O(i) where i refers to the number of parts of the path
- find() has space complexity of O(j) where j refers to the number of elements in the input array
- as above, j = i so add_handler has space complexity of O(n)
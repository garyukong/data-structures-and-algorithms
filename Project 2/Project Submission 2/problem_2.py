def find_files(suffix, path):
    """
    Find all files beneath a path irrespective of file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # Import OS modules
    import os

    # Base case 1: path is a file and ends with suffix -> return the path
    if os.path.isfile(path) and path.endswith(suffix):
        return [path]

    # Base case 2: path is a file and does not end with suffix -> return an empty list
    elif os.path.isfile(path):
        return []

    # Case where path is not a file (i.e., is a directory)
    else:
        files = []                                              # create an empty list
        for filename in os.listdir(path):                       # iterate through each child in the path
            childpath = os.path.join(path, filename)            # compose full path to child
            filesToAdd = find_files(suffix, childpath)          # make a recursive call to find_all_files and store result as filesToAdd
            if filesToAdd:                                      # if filesToAdd contains files with suffix, join filesToAdd to the list
                files += filesToAdd
        return files                                            # return the now-populated list

if __name__ == "__main__":
    from os import chdir
    
    chdir('/Users/garykong/git/datastructuresandalgorithms/Project: Show Me the Data Structures/')

    # TEST CASE 1: Path points to single file not ending with '.c'. Check for files ending in suffixes '.c'
    print("\nTEST CASE 1")
    print(find_files('.c','./testdir/subdir4/.gitkeep'))
    # Should print []

    # TEST CASE 2: Path points to single file ending with 'c.'. Check for files ending in suffixes '.c'
    print("\nTEST CASE 2")
    print(find_files('.c','./testdir/t1.c'))
    # Should print ['./testdir/t1.c']

    # TEST CASE 3: Path points to subdirectories containing files ending with '.c'. Check for files ending in suffixes '.c'
    print("\nTEST CASE 3")
    print(find_files('.c','./testdir/subdir5'))
    # Should print ['./testdir/subdir5/a.c']

    # TEST CASE 4: Path points to subdirectories containing files not ending with '.c'. Check for files ending in suffixes '.c'
    print("\nTEST CASE 4")
    print(find_files('.c','./testdir/subdir4'))
    # Should print [] 

    # TEST CASE 5: Path points to root of directory. Check for files ending in suffixes '.c'
    print("\nTEST CASE 5")
    print(find_files('.c','./testdir'))
    # Should print ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

    # TEST CASE 6: Path points to directory. Empty value for suffix
    print("\nTEST CASE 6")
    print(find_files(None,'./testdir'))
    # Should return an error because suffix cannot be empty
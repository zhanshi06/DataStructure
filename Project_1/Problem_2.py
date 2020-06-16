import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if len(suffix) == 0:
        return []
    files_list = list()
    if os.path.exists(path):
        
        dir_to_walk = [path]

        while dir_to_walk:
            cur_folder = dir_to_walk.pop() + '/' # get the first folder
            sub_items = os.listdir(cur_folder)

            for item in sub_items:
                item = cur_folder + item
                if os.path.isdir(item):
                    dir_to_walk.append(item)
                elif str(item).endswith(suffix):
                    files_list.append(item)
    
    return files_list


# tets
### Test Case one ###
print(find_files('.h', 'testdir'))   

'''
output: ['testdir/t1.h', 'testdir/subdir1/a.h', 'testdir/subdir5/a.h', 'testdir/subdir3/subsubdir1/b.h']
'''

### Test Case two ###
print(find_files('.c', ''))
'''
output: []
'''

### Test Case three ###
print(find_files('.c', 'testdir/subdir1'))
'''
output: ['testdir/subdir1/a.c']
'''


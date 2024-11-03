# Permutations are just changing the order of elements in an list.
# Look at the concepts folder for more info
def permutations(items):
    if items == []:
        return [[]]

    first = items[0]
    remaining = items[1:]
    perms = permutations(remaining)
    result = []
    for perm in perms:
        for i in range(len(perm)+1):
            result.append([*perm[:i], first, *perm[i:]])
    
    return result

permutations(['a', 'b', 'c']) # -> 
# [ 
#   [ 'a', 'b', 'c' ], 
#   [ 'b', 'a', 'c' ], 
#   [ 'b', 'c', 'a' ], 
#   [ 'a', 'c', 'b' ], 
#   [ 'c', 'a', 'b' ], 
#   [ 'c', 'b', 'a' ] 
# ] 

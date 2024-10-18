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

print(permutations(['red', 'blue'])) # ->
# [ 
#   [ 'red', 'blue' ], 
#   [ 'blue', 'red' ] 
# ]
# What is a subset?

# For an set {x, y, z}, 
# the possible subsets are {}, {x}, {y}, {z}, {x, y}, {y, z}, {z, x} or {x, y, z}.
# Observe that there is an empty set.

def subsets(elements):
    # Step 1: Base case
    # Here, why you need to return [[]], not []?
    # It's due to mathematical reason. The power set is the set of all subsets of a set. 
    # The empty set is a subset of all sets, including itself. 
    # That means that once you have an empty set, its power set is {empty set}. 
    # Since the problem is using list, the empty set is [] & its power set is [[]] 
    if elements == []:
        return [[]]
    # Step 4: Recursive step
    first_element = elements[0]
    subsets_without_first_element = subsets(elements[1:])

    subsets_with_first_element = []
    for subset in subsets_without_first_element:
       subsets_with_first_element.append([*subset, first_element])

    return subsets_without_first_element + subsets_with_first_element

print(subsets(['a', 'b'])) # ->
# [ 
#   [], 
#   [ 'b' ], 
#   [ 'a' ], 
#   [ 'a', 'b' ] 
# ]

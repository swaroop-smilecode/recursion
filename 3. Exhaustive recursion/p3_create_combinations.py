def create_combinations(items, k):
  if len(items) < k:
    return []
  
  if k == 0:
    return [[]]
  
  first = items[0]
  combos_with_first = []
  for combo in create_combinations(items[1:], k - 1):
    combos_with_first.append([ first, *combo ])
  
  combos_without_first = create_combinations(items[1:], k)
  
  return combos_with_first + combos_without_first

print(create_combinations(["a", "b", "c"], 2)); # ->
# [
#   [ 'a', 'b' ],
#   [ 'a', 'c' ],
#   [ 'b', 'c' ]
# ]

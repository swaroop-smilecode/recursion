def sum_of_lengths(strings_list):
  if len(strings_list) == 0:
    return 0
  
  return len(strings_list[0]) + sum_of_lengths(strings_list[1:])

sum_of_lengths(['goat', 'cat', 'purple']) # -> 13

def sum_numbers_recursive(numbers):
  # Step 1: Base case
  if numbers == []:
    return 0
  # Step 4: Recursive step
  return numbers[0] + sum_numbers_recursive(numbers[1:])

print(sum_numbers_recursive([5, 2, 9, 10])) # -> 26
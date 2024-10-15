def fibonacci(n):
  # Step 1: Base cases
  if n == 0:
    return 0
  if n == 1:
    return 1
  # Step 4: Recursive step
  return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4)); # -> 3

def factorial(n):
    # Step 1: Base case
    if n == 0:
        return 1
    # Step 4: Recursive step
    return n * factorial(n-1)

factorial(3) # -> 6

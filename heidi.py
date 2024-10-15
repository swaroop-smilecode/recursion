def count_down(n):
    # Base case
    if n == 0:
        return

    # Work need to be done before entering into recursive call.
    print(f"Entering {n}")

    # Recursive case
    count_down(n-1)

    # Work need to be done before entering into recursive call.
    print(f"Leaving {n}")
count_down(3)
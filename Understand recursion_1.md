Read the below program & you will automatically understand 
the Recursion concept.
```
def count_down(n):
    # Base case
    if n == 0:
        return

    # Specific work you want to do
    print(n)

    # Recursive case
    count_down(n-1)

count_down(10)
```




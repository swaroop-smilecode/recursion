- Let's consider you are calling function b from function a.
  The, first the function b gets executed & then function b
  The stack diagram looks like below. As we can see the function 
  b ended on top, so, it gets executed first & then the 
  execution continues.
  -----
  | b |
  -----
  | a |
  -----
- This can be better understood by below example. Execute the below program 
  & understand why the output gets printed the way it gets printed.
```
def count_down(n):
    if n == 0:
        return

    print("Entering "+ str(n))
    count_down(n-1)
    print("Returning from "+ str(n))

count_down(2)
```




def palindrome(s):
  # Step 1: Base case
  if s == "":
    return True
  # Step 4: Recursive step
  # Here, you wont face an index out of bound problem with s[1:-1]
  # The reason is slicing out of bound indexes will give to "" 
  # & you are handling this "" in the base case.
  return s[0] == s[-1] and palindrome(s[1:-1])

palindrome("pop") # -> True

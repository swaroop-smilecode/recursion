def palindrome(s):
  def reverse_string(s):
    if len(s) == 0:
        return "" 
    return reverse_string(s[1:]) + s[0]

  if s == reverse_string(s):
     return True
  else:
     return False


palindrome("pop") # -> True

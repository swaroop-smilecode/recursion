def reverse_string(s):
  # Step 1: Base case
  if s == "":
    return ""
  # Step 4: Recursive step  
  return reverse_string(s[1:]) + s[0]

reverse_string("hello") # -> "olleh"


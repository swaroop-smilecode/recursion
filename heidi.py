def c():
  print("I am function c")

def b():
  print("I am function b")
  c()

def a():
  print("I am function a")
  b()

a()
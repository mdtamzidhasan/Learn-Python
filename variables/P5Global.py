#Those variables that are defined outside of a function are known as global variables.
# This code demonstrates the use of local variables.
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



# This code demonstrates the use of global variables.
a = "awesome"
def myfunc():
  global a
  a = "fantastic"

myfunc()

print("Python is " + a)
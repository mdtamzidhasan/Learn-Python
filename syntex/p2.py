#Indentation in Python is defined by the number of spaces at the beginning of a line.
# The following code will raise an IndentationError if not properly indented.
"""
if 5 > 2:
print("Five is greater than two!")
"""

# Correct indentation for the code snippet
if 5 > 2:
  print("Five is greater than two!")
  
  #You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
""" 
    if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
"""
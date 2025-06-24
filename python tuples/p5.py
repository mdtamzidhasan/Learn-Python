# Unpacking a tuple
mytuple = ("apple", "banana", "cherry")
x, y, z = mytuple
print(x)
print(y)    
print(z)


# Unpacking a tuple with asterisk
mytuple = ("apple", "banana", "cherry", "orange", "kiwi")
x, *y = mytuple
print(x)  # Output: apple
print(y)  # Output: ['banana', 'cherry', 'orange', 'kiwi']
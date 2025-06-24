# Convert the tuple into a list to be able to change it
x = ("apple", "banana", "cherry")

y = list(x)
y[1] = "kiwi"  # Change the second item
x = tuple(y)
print(x)


# add item using append()
y = list(x)
y.append("orange")
x = tuple(y)
print(x)

# add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange", "mango", "grape")
thistuple += y  # Concatenate tuples
print(thistuple)
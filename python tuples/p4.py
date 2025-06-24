thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# Or we can delete the tuple completely
# del thistuple

del thistuple
# print(thistuple)  # This will raise an error since thistuple is deleted


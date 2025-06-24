thisset = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}

# To remove an item in a set, use the remove(), discard(), or pop() method.

thisset.remove("banana")
print(thisset)
# If the item to remove does not exist, remove() will raise an error.

thisset.discard("apple")     # This will not raise an error
print(thisset)


# You can also use the pop() method to remove an item, but this method will remove a random item, so
# so you cannot be sure what item that gets removed.

x = thisset.pop()
print(x)
print(thisset)


# The clear() method empties the set.
thisset.clear()
print(thisset)

# The del keyword will delete the set completely.
del thisset
# print(thisset)  # This will raise an error because the set no longer exists
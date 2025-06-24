# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.

myset = {"apple", "banana", "cherry"}
myset.add("orange")  # Add an item
print(myset)


# To add items from another set into the current set, use the update() method.
myset1 = {"apple", "banana", "cherry"}
myset2 = {"orange", "mango", "grape"}
myset1.update(myset2)  # Add items from myset2 to myset1
print(myset1)

#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
myset3 = {"apple", "banana", "cherry"}
mylist = ["orange", "mango", "grape"]
myset3.update(mylist)  # Add items from mylist to myset3
print(myset3)
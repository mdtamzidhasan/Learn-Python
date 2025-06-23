thislist = ["apple", "banana", "cherry"]
print(thislist)

# remove an item by value
thislist.remove("banana")
print(thislist)

# remove an item by index
thislist.pop()
print(thislist)

thislist.pop(0)
print(thislist)

# use del keyword to remove the item
list1 = ['a', 'b', 'c', 'd']
del list1[0]
print(list1)

# use del keyword to remove the entire list
del list1
#print(list1)

# clear the list
thislist.clear()
print(thislist)

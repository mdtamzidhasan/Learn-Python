# You cannot access items in a set by referring to an index or a key.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)
    
    
print("banana" in thisset)  # Check if "banana" is in the set
print("orange" not in thisset)  # Check if "orange" is not in the set


# Once a set is created, you cannot change its items, but you can add new items.
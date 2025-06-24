# The update() method inserts all items from one set into another.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.update(set2)
print(set1)




# The intersection() method will return a new set, that only contains the items that are present in both sets.
set3 = set1.intersection(set2)
print(set3)

set4 = set1 & set2
print(set4)



# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set5 = set1.difference(set2)
print(set5)
set6 = set1 - set2
print(set6)

#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1.difference_update(set2)
print(set1)


# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set7 = set1.symmetric_difference(set2)
print(set7)
set8 = set1 ^ set2
print(set8)


# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1.symmetric_difference_update(set2)
print(set1)
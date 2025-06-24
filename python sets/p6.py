# The union() method returns a new set with all items from both sets.

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = set1 | set2
print(set4)

# Join multiple sets using the union() method.
set5 = {'a', 'b', 'c'}
set6 = {1, 2, 3}

set7 = set1.union(set2, set3, set4, set5, set6)
print(set7)



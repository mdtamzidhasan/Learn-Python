# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
myset = {"apple", "banana", "cherry"}
print(myset)

#It is also possible to use the set() constructor to make a set.
newset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(newset)


# Duplicate values will be ignored
myset1 = {"apple", "banana", "cherry", "apple"}
print(myset1)


# True and 1 is considered the same value:
myset2 = {True, 1, False, 0}
print(myset2)  # Output: {False, True}

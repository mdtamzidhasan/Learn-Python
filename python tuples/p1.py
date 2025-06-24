mytuple = (1, 2, 3, 4, 5)
print(mytuple)

#A tuple is a collection which is ordered and unchangeable and allow duplicate values.

mytuple1 = ("apple", "banana", "cherry")
print(mytuple1)
print(len(mytuple1))


# Create a tuple with one item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple1 = ("apple")
print(type(thistuple1))



#It is also possible to use the tuple() constructor to make a tuple.
thattuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thattuple)


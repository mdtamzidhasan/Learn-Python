fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newfruits = []

for x in fruits:
    if "a" in x:
        newfruits.append(x)
        
print(newfruits)


# using list comprehension
newlist = [x for x in fruits if 'a' in x]
print(newlist)

#syntex for list comprehension
#newlist = [expression for item in iterable if condition == True]


newlist2 = [x for x in range(10) if x < 5]
print(newlist2)
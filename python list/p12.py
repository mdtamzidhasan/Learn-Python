# Join two lists using the + operator
thislist1 = ["apple", "banana", "cherry"]
thislist2 = ["orange", "mango", "grape"]

newlist = thislist1 + thislist2
print(newlist)



# Join two lists using the extend() method
newlist.extend(thislist1)
print(newlist)



# Join two lists using the append() method

for x in thislist2:
    thislist1.append(x)
print(thislist1)
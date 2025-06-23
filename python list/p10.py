#Sort the list alphabetically:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.sort()

print(thislist)


#Sort the list numerically:
thislist1 = [43, 24, 12, 34, 56, 78, 90]
thislist1.sort()

print(thislist1)



#Sort the list descending:
thislist.sort(reverse=True)
print(thislist)

#Sort the list numerically descending:
thislist1.sort(reverse = True)
#thislist1 = reverse()
print(thislist1)



#Custom sort function:
# sort the list based on how close the number is to 50
def myfunc(n):
    return abs(n - 50)

thislist1.sort(key = myfunc)
print(thislist1)


#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
#So if you want a case-insensitive sort function, use str.lower as a key function
thislist2 = ["banana", "Orange", "Kiwi", "cherry"]
thislist2.sort(key = str.lower)
print(thislist2)
thislist = ["apple", "banana", "cherry"]

for x in thislist:
    print(x)
    

for i in range(len(thislist)):
    print(thislist[i])
    

# using a while loop
i=0
while i < len(thislist):
    print(thislist[i])
    i+= 1
    

# using list comprehension
list1 = ["apple", "banana", "cherry"]
[print(x) for x in list1]


#Strings are Arrays
a = "Hello, World!"
print(a[1])

#Looping Through a String
for x in "banana":
  print(x)
  
#String Length
a = "Hello, World!" 
print(len(a))

#Check String
txt = "The best things in life are free!"
print("free" in txt)
#using if
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
#Using if
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
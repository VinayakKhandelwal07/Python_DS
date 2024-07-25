#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.ButYou can convert the tuple into a list, change the list, and convert the list back into a tuple

#Update a Tuple 
x = ("apple", "banana", "cherry")
y = list(x)     #Convert the tuple into a list to be able to change it
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add items in tuple

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)  #Convert the tuple in list 
y.append("orange") # then use append Method in list
thistuple = tuple(y) # convert the list into tuple

# Add tupe to a tuple 
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# Remove items in Tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)#Conert the tuple into the list
y.remove("apple") #use remove method 
thistuple = tuple(y)# convert it back into a tuple

#The del keyword can delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

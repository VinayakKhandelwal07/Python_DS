#Sets are used to store multiple items in a single variable.
# Note: Set items are unchangeable, but you can remove items and add new items.
#Create a Set
thisset = {"apple", "banana", "cherry"}#(Sets are written with curly brackets.)
print(thisset)

#Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}#(Duplicate values will be ignored)
print(thisset)
#output ---> {"apple","banana","cherry"}


#Get the number of items in a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))



# set1 = {"abc", 34, True, 40, "male"}  >>>A set with strings, integers and boolean values


myset = {"apple", "banana", "cherry"}
print(type(myset))#(What is the data type of a set?)
# output will be <class 'set'>

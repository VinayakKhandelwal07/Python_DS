#To remove an item in a set, use the remove(), or the discard() method
#Remove "banana" by using the remove() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# using discard method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")#Remove "banana" by using the discard() method
print(thisset)

# Note: If the item to remove does not exist, remove() will raise an error

# clear method
#The clear() method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#Delelte Method 
#The del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

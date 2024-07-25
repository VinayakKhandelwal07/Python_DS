#Join Sets

#The union() and update() methods joins all items from both sets.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #(Join set1 and set2 into a new set)
print(set3)

#join multiple sets with the union() method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

# Use | to join two sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

#The union() method allows you to join a set with other data types, like lists or tuples
#Join a set with a tuple

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)



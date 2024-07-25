#The update() method inserts all items from one set into another.

#The update() changes the original set, and does not return a new set

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)#The update() method inserts the items in set2 into set1
print(set1)

#update() will exclude any duplicate items.

# You cannot access items in a set by referring to an index or a key.But

# Loop through the set, and print the values
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  #Output will be :​
      # cherry 
         #apple 
       #banana


thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)#(Check if "banana" is present in the set)
#Output will be in True and False


#ADD Items
#add one item to a set use the add() method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Add sets 
#To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Lists are used to store multiple items in a single variable.
# Creation of a List 
thislist = ["apple", "banana", "cherry"]
print(thislist)

list1 = ["abc", 34, True, 40, "male"]
print(list1)

# List items are ordered, changeable, and allow duplicate values
# List items are indexed, the first item has index [0], the second item has index [1] etc.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]# Lists Allows Duplicate Values
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))# Print the number of items in the list 
#ACCESS Element
thislist = ["apple", "banana", "cherry"] 
print(thislist[1])#(By INDEX )

thislist = ["apple", "banana", "cherry"]
print(thislist[1:3] # (Given Range from 1 to 3)
#Negative Indexing
#Negative indexing means start from the end, -1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Change Item Value
#To change the value of a specific item, refer to the index number:
thislist = ["apple","banana","cherry"]
thislist[1] = "blackcurrant"
print(thislist)    
# Output ---> ['apple', 'blackcurrant', 'cherry']

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Loop Through a List
#You can loop through the list items by using a for loop:
thislist = ["apple","banana","cherry"]
for x in thislist:
  print(x)
  #Output --- > 
   #apple
   #banana
   #cherry

#Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] #print all items in a list

#Join two list 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

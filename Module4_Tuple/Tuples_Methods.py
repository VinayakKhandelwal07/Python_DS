#count()---------> Returns the number of times a specified value occurs in a tuple

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)#Return the number of times the value 5 appears in the tuple
print(x)


#index()-------->Searches the tuple for a specified value and returns the position of where it was found

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)#(Search for the first occurrence of the value 8, and return its position)
print(x)

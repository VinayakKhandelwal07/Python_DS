#List Method 
Method	         Description
append()	    Adds an element at the end of the list
clear()	      Removes all the elements from the list
copy()	      Returns a copy of the list
count()	      Returns the number of elements with the specified value
extend()	     Add the elements of a list (or any iterable), to the end of the current list
index()	      Returns the index of the first element with the specified value
insert()	     Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	     Reverses the order of the list
sort()	         Sorts the list


# Append() Method
 fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)

# CLear Method
fruits = ['apple', 'banana', 'cherry']
fruits.clear()

# Copy Method 
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()

# count Method()
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")

#Extend Method 
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars

#index()	Method 
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")#(What is the position of the value "cherry")

#insert() Method
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")#(Insert the value "orange" as the second element of the fruit list)

#Pop () Method 
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)#(Remove the second element of the fruit list)

#remove() Method 
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")#(Remove the "banana" element of the fruit list)

#reverse() Method
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()

#sort() Method
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()

#Sort the list descending:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)


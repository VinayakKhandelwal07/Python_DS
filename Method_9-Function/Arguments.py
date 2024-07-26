#Information can be passed into functions as arguments.

#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Number of Arguments

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#Arbitrary Arguments, *args
# the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Keyword Arguments
#You can also send arguments with the key = value syntax.This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#Return Values
#To let a function return a value, use the return statement

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

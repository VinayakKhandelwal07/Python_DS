
#The finally block, if specified, will be executed regardless if the try block raises an error or not
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


#to throw an exception if a condition occurs.
#To throw (or raise) an exception, use the raise keyword

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

# The Raise Keyword is used to raise an exception
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")#(Raise a Typeerror if X is not an ineger)

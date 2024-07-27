#Exception Handling
#When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

#These exceptions can be handled using the try statement

#The try block lets you test a block of code for errors.

try:
  print(x)#(The try block will generate an exception, because x is not defined)
except:
  print("An exception occurred")

#Many Exception
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


#ELSE 
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")




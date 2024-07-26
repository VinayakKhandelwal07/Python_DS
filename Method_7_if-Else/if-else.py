# If 
a = 33
b = 200
if b > a:
  print("b is greater than a")

# indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose
a = 33
b = 200
if b > a:
print("b is greater than a")# You will be get an error 

#Elif The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition"
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

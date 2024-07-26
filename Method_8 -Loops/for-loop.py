# for loop in list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

  
# loop in string
for x in "banana":
  print(x)

#Breek Statement 
#Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


#For loop Using the range() function:

for x in range(6):
  print(x)

#for loop Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

#Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")


#Nested loop 
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

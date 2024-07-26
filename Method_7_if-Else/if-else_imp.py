#Short Hand If ... Else
#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line
# This technique is known as Ternary Operators, or Conditional Expressions.

a = 2
b = 330
print("A") if a > b else print("B")#(One line if else statement)

#Nested If
#You can have if statements inside if statements, this is called nested if statements.
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
  pass

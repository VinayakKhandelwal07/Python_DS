# Dictionaries are used to store data values in key:value pairs.
# Creation of dictionary 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates .

# Accessing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] #(Get the value of the "model" key)

#Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

#Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict: #(Check if "model" is present in the dictionary)
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

### Dictionaries ###

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
"""
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:
"""
#create and print a dictionary:
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict)


## Dictionary Items ##
"""
Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
"""

#print the "brand" value of the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


## Ordered or Unordered? ##
"""
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
"""

## Changeable ##
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.


## Duplicates Not Allowed ##

# Dictionaries cannot have two items with the same key:
#duplicate values will overwrite existing values:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2016
}
print(thisdict)


## Dictonary Length ##

# To determine how many items a dictionary has, use the len() function:
#print the number od items in the dictionary:
print(len(thisdict))


## Dictionary Items - Data Types ##

# The values in dictionary items can be of any data type:
# Strings, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


## types() ##

# From Python's perspective, dictionaries are defined as objects with the data type 'dict':
#print the data type of a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))



## Accecc Items ##

# You can access the items of a dictionary by referring to its key name, inside square brackets:
#get the value of the "model" key:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

# There is also a method called get() that will give you the same result:
#get the value of the "model" key:
x = thisdict.get("model")


## Get Keys ##

# The keys() method will return a list of all the keys in the dictionary:
#get a list of the keys:
x = thisdict.keys()

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
#add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change

car["color"] = "red"
print(x) #after the change


## Get Values ##

# The values() method will return a list of all the values in the dictionary:
#get a list of the values:
x = thisdict.values()

# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
#make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change

car["year"] = 2022
print(x) #after the change


## Get Items ##

# The items() method will return each item in the dictionary, as tuples in a list.
#get a list of the key:value pairs:
x = thisdict.items()

# The returned list is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
#make a change in the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change

car["year"] = 2022
print(x) #after the change

#add a new item to the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change

car["color"] = "red"
print(x) #after the change


## Check if Key Exists ##

# To determine if a specified key is present in a dictionary use the in keyword:
#check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")



### Change Dictionary Items ###


## Change Values ##

# You can change the value of a specific item by referring to its key name:
#change the "year" to 2021:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2021


## Update Dictionary ##

# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
#update the "year" of the car by using the update() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2021})



### Loop Dictionaries ###


## Loop Through a Dictionary ##
"""
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
"""
#print all keys names in the dictionary, one by one:
for x in thisdict:
    print(x)

#print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

#you can also use the values() method to return values of the dictionary:
for x in thisdict.values():
    print(x)

#you can also use the keys() method to return keys of the dictionary:
for x in thisdict.keys():
    print(x)

#loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
    print(x, y)



### Copy Dictionaries ###


## Copy a Dictionary ##
"""
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().
"""
#make a copy of a dictionary with the copy() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function dict().
#make a copy of a dictionary with the dict() function:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)



### Nested Dictionaries ###

# A dictionary can contain dictionaries, this is called nested dictionaries.
#create a dictionary that contains three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Or, if you want to add three dictionaries into a new dictionary:
#create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}



### Dictionary Methods ###
"""
Method	                Description
clear()	                Removes all the elements from the dictionary
copy()	                Returns a copy of the dictionary
fromkeys()	            Returns a dictionary with the specified keys and value
get()	                Returns the value of the specified key
items()	                Returns a list containing a tuple for each key value pair
keys()	                Returns a list containing the dictionary's keys
pop()	                Removes the element with the specified key
popitem()	            Removes the last inserted key-value pair
setdefault()	        Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	            Updates the dictionary with the specified key-value pairs
values()	            Returns a list of all the values in the dictionar
"""
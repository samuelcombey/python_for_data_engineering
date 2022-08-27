### Sets ###
"""
* Note: Set items are unchangeable, but you can remove items and add new items.
Note: Sets are unordered, so you cannot be sure in which order the items will appear.
Once a set is created, you cannot change its items, but you can remove items and add new items.
"""

# Sets are written with curly brackets {}
#create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)


## Dupicates Not Allowed ##
#duplicate values will be ignored
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


## Get the Length of a Set ##

# To determine how many items a set has, use the len() method.
#get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))


## Set Items - Data Types ##

# String, int and boolean date types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, True}

# A set with strings, integers, and booleans:
set4 = {"apple", 1, True}


## The set() Constructor ##

# It is also possible to use the set() constructor to make a set.
#using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)



### Access Set Items ###
"""
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
"""

#loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for item in thisset:
    print(item)

#check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)



### Add Set Items ###


## Add Items ##

# To add one item to a set, use the add() method.
#add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


## Add Sets ##

# To add items from another set into the current set, use the update() method.
#add elements from tropical in thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


## Add Any Iterable ##

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
#add elements of a list to a set:
thisset = {"apple", "banana", "cherry"}
mylist = ["orange", "mango", "grapes"]
thisset.update(mylist)



### Remove Set Items ###
# To remove an item in a set, use the remove(), or the discard() method.

#remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#remove the last item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword removes the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) # this will raise an error because the set no longer exists.


## Loop Sets ##

# You can loop through the set items using a for loop.
#loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)



### Join Sets ###


## Join Two Sets ##

# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

# The union() method returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# The update() method inserts all the items from one set into another:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)

# Note: Both union() and update() will exclude any duplicate items.


## Keep Only the Duplicates ##

# The intersection_update() method will keep only the items that are present in both sets.
#keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# The intersection() method returns a new set with items that are in both sets:
#return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)


## Keep All, But NOT the Duplicates ##

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
#keep the items that are not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
#return a set that contains all the items from both sets, except items that are present in both:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)



### Set Methods ###

"""
Method	                                Description
add()	                                Adds an element to the set
clear()	                                Removes all the elements from the set
copy()	                                Returns a copy of the set
difference()	                        Returns a set containing the difference between two or more sets
difference_update()	                    Removes the items in this set that are also included in another, specified set
discard()	                            Remove the specified item
intersection()	                        Returns a set, that is the intersection of two other sets
intersection_update()	                Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                        Returns whether two sets have a intersection or not
issubset()	                            Returns whether another set contains this set or not
issuperset()	                        Returns whether this set contains another set or not
pop()	                                Removes an element from the set
remove()	                            Removes the specified element
symmetric_difference()	                Returns a set with the symmetric differences of two sets
symmetric_difference_update()	        inserts the symmetric differences from this set and another
union()	                                Return a set containing the union of sets
update()	                            Update the set with the union of this set and others
"""
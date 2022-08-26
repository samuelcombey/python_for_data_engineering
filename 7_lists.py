### List ###
# List are used to store multiple values in a single variable.
# Lists are created using square brackets [], and can contain any type of variable.

# Create list
my_list = [1, 2, 3, 4, 5]
print(my_list)


## List Items ##
# List items are ordered, changeable and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] and so on.


## Ordered ##
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.


## Changeable ##
# The list is changeable, meaning that we can change, add and remove items in a list after it has been created.


## Allow Duplicates ##
# Since list are indexed, list can have items with the same value.
#lists allow duoplicate values:
this_is_list = ["a", "b", "c", "a", "b", "c"]
print(this_is_list)


## List Length ##
# To determine how may items a list has, use the len() function.
#print the number of items in the list:
this_is_list = ["apple", "banana", "cherry"]
print(len(this_is_list))


## List Items - Data Types ##
# List items can be any data type:
#string, int and boolean data types.
list1 = ["apple", "banana", "cherry"]
list2 = [1, 2, 3]
list3 = [False, True, False]

#a list can contain different data types:
list4 = ["apple", "banana", "cherry", 1, 2, 3, False, True, False]


## The list() Constructor ##
# The list() constructor is used to create a list.
#using the list() constructor to create a list:
list5 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(list5)


## Python Collections (Arrays) ##
# There are four collection data types in the Python programming language:
# List, Tuple, Dictionary, and Set.
"""
# Lists are ordered, changeable and allow duplicate values.
# Tuples are ordered, unchangeable and allow duplicate values.
# Dictionaries are unordered, changeable and allow duplicate keys.
# Sets are unordered, unchangeable and don't allow duplicate values.
"""



### Access List Items ###
# List items are indexed and you can access them by referring to the index number.

#print the second item of the list:
this_is_list = ["apple", "banana", "cherry"]
print(this_is_list[1])


## Negative Indexing ##
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

#print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


## Range of Indexes ##
# You can specify a range of indexes by specifying the start and end indexes.

#return the third, forth and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# Note: The search will start at index 2 (included) and end at index 5 (not included).

# By leaving out the start value, the range will start at the first item:
#this example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# By leaving out the end value, the range will go on to the end of the list:
#this example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


## Range of Negative Indexes ##
# Specify negative indexes if you want to start the search from the end of the list:
#this example returns the items from "orange" (-4) to, but NOT including, "mango" (-4):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


## Check if Item Exists ##

# To determine if a specified item is present in a list use the "in" keyword.
#check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")



### Change Item Value ###


## Change Item Value ##

# To change the value of a specific item, refer to the index number:
#change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


## Change a Range of Item Values ##

# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
#change the values "banana" and cherry to "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
#change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
#change the second and third values by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["blackcurrant"]
print(thislist)


## Insert Items ##

# To insert an item into a list, use the insert() method.
#insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")



### Add List Items ###


## Append Items ##

# To add an item to the end of the list, use the append() method.
#using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("watermelon")
print(thislist)


## Insert Items ##

# To insert an item at a specific index, use the insert() method.
#insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "watermelon")
print(thislist)
# Note: As a result of the examples above, the lists will now contain 4 items.


## Extend List ##

# To append elements from another list, use the extend() method.
#add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["watermelon", "pineapple", "mango"]
thislist.extend(tropical)
print(thislist)


## Add Any Iterable ##

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("watermelon", "pineapple", "mango")
thislist.extend(thistuple)
print(thislist)



### Remove List Items ###


## Remove Specified Item ##

# The remove() method removes the specified item:
#remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


## Remove Specified Index ##

# The pop() method removes the specified index.
#remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.
#remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
#remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely:
#delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist


## Clear List ##

# The clear() method empties the list:
# The list still remains, but it has no content.
#clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)



### Loop Lists ###


## Loop Through a List ##

# You can loop through the list items by using a for loop.
#print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for items in thislist:
    print(items)


## Loop Through the Index Numbers ##

# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
#print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for index in range(len(thislist)):
    print(thislist[index])


## Using a While Loop ##

# You can loop through the list items by using a while loop.
"""
Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.
"""
#print all items, using a while loop to go through all the index numbers:
thislist = ["apple", "banana", "cherry"]
index = 0
while index < len(thislist):
    print(thislist[index])
    index = index + 1


## Looping Using list Comprehension ##

# List comprehension offers the shortest syntax for looping through lists:
#short hand for looping that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(item) for item in thislist]



### List Comprehension ###
"""
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write a for statement with a conditional test inside:
"""
fruits = ["apple", "banana", "cherry", "kiwi", "melon", "mango"]
new_fruits = []

for fruit in fruits:
    if "a" in fruit:
        new_fruits.append(fruit)

print(new_fruits)

# With list comprehension you can do all this in one line:
fruits = ["apple", "banana", "cherry", "kiwi", "melon", "mango"]
new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)


## The Syntax ##
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

# Condition #
# The condition is like a filter that only accepts the items that the valuate to True.

#only accept items that are not "apple":
newlist = [item for item in fruits if item != "apple"]

# The condition 'if item != "apple"' will return True for all elements other than "apple", making the list contain all fruits except "apple".
# The condition is optional and can be omitted:
#with no if statement
newlist = [fruit for fruit in fruits]

# Iterable #
# The iterable can be any iterable object, like a list, tuple, dictionary, set etc.
#you can use the range() function to create an iterable:
newlist = [x for x in range(10)]

# Same example but with a condition:
#accept only numbers lower than 5:
newlist = [num for num in range(10) if num < 5]

# Expression #

# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
#set the values in the new list to upper case:
newlist = [item.upper() for item in fruits]

# You can set the outcome to whatever you like:
#set all values in the new list to "hello":
newlist = ["hello" for item in fruits]

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
#return "orange" insted of "banana":
newlist = [fruit if fruit != "banana" else "orange" for fruit in fruits] 
# Return the fruit if it is not banana, if it is banana return "orange".



### Sort Lists ###


## Sort List Alphabetically ##
# List objects have a sort() method that will sort the list alphabetically, ascending, by default.

#sort the list alphabetically:
thislist = ["apple", "banana", "cherry"]
thislist.sort()
print(thislist)

#sort list numerically:
thislist = [100, 40, 23, 65, 82]
thislist.sort()
print(thislist)


## Sort Descending ##
# To sort descending, use the keyword argument reverse = True:

#sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


## Customize Sort Function ##
"""
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):
"""

#sort the list based on how close the number is to 50:
def my_sort(item):
    return abs(item - 50)

thislist = [40, 65, 82, 23, 100, 50]
thislist.sort(key = my_sort)
print(thislist)


## Case Insensitive Sort ##

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
#case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# So if you want a case-insensitive sort function, use str.lower as a key function:
#perform a case-insensitive sort:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


## Reverse Order ##

# What if you want to reverse the order of a list, regardless of the alphabet?

# The reverse() method reverses the current sorting order of the elements.
#reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)



### Copy a List ###
"""
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().
"""

#make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
new_list = thislist.copy()
print(new_list)

# Another way is to use the built-in function list().
#make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
new_list = list(thislist)
print(new_list)




### Join Lists ###


## Join Two Lists ##
"""
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.
"""

#join two lists:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
#append list2 into list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for item in list2:
    list1.append(item)

print(list1)

# Or you can use the extend() method:
#use the extend() method to add list2 at the end of list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)



### List Methods ###
"""

Method	        Description
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list
"""
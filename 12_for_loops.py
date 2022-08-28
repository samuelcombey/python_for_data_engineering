### For loops ###

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
#print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# The for loop does not require an indexing variable to set beforehand.


## Looping Through a String ##

# Even strings are iterable objects, they contain a sequence of characters:
#loop through the letters in the word "banana":
for character in "banana":
    print(character)


## The break Statement ##

# With the break statement we can stop the loop before it has looped through all the items:
#exit the loop when fruit is "banana":
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

#exit the loop when fruit is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)


## The continue Statement ##

# With the continue statement we can stop the current iteration of the loop, and continue with the next:
#do not print banana:
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)


## The range() Function ##
"""
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
"""
#using the range() function:
for x in range(10):
    print(x)

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
#using the start parameter:
for x in range(2, 6):
    print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
#increment the squence with 3 (default is 1):
for x in range(2, 30, 3):
    print(x)


## Else in for loops ##

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
#print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")


## Nested Loops ##
"""
A nested loop is a loop inside a loop.
The "inner loop" will be executed one time for each iteration of the "outer loop":
"""
#print each adjective for every fruit:
adjs = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for adj in adjs:
    for fruit in fruits:
        print(adj.capitalize(), fruit)


## The pass Statement ##

# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
    pass
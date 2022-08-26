### Variables
# Variables are containers for storing data values.

# Creating Variables
# Python has no command for declaring a variable.

# A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


### Casting
# Casting is the process of changing the type of a variable.
x = str(3) # x will be of type str '3'
y = int(3) # y will be of type int 3
z = float(3) # z will be of type float 3.0


### Get the Type
# The type() function returns the type of a variable.
x = 5
y = "John"
print(type(x))
print(type(y))


### Single or Double Quotes?
# Strings variables can be declared either by using single or double quotes.
x = "John"
# is the same as
x = 'John'


### Case-Sensitive
# Variable names are case-sensitive.
# This will create two variables:
a = 4
A = "Sam"
# A will not overwrite a.


### Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"


### Multi Words Variable Names
# Variable names with more than one word can be difficult to read.
# There are several techniques you can use to make them more readable:

## Camel Case:
myVariableName = "John"

## Pascal Case:
MyVariableName = "John"

## Snake Case:
my_variable_name = "John"


### Assign Multiple Values

## Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


## One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

## Unpacking a Collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["Orange", "Banana", "Cherry"]
fruit1, fruit2, fruit3 = fruits
print(fruit1)
print(fruit2)
print(fruit3)



### Output Variables

# You can use the print() function to output variables.
x = "Python is awesome"
print(x)

# In the print() function, you can output multiple variables, separated by commas:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

# For numbers, the + operator works as a mathematical operator:
x = 5
y = 10
print(x + y)

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "Sam"
print(x, y)



### Global Variables
# Global variables are variables that are defined outside of a function.
# Global variables can be used by everyone, both inside of functions and outside.

# Create a variable outside of a function and use it inside the function
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)


## The global Keyword
# To create a global variable inside a function, you can use the global keyword.
# If you use the global keyword, the variable belongs to the global scope.
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

# Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
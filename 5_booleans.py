# Booleans represent one of two values: True or False.
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Print a message based on wheather the condition is true or false.
a = 200
b = 33

if a > b:
    print("b is greater than a")
else:
    print("b is not greater than a")


## Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return.

# Evaluate two variables:
x = "Hello"
y = 15

print(bool(x))
print(bool(y))


## Most Values are True
"""
Almost any value is evaluated to True if it has some sort of content.
Any string is True, expect empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""

# The following will return True:
bool("abc")
bool(123)
bool(["apple", "banana", "cherry"])


## Some Values are False
"""
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
"""

# Class with a __len__ function that returns 0 or False
class my_class:
    def __len__(self):
        return 0

my_obj = my_class()
print(bool(my_obj))


## Functions can Return a Boolean

# You can create functions that return a Boolean Value.
# Print that answer of a function.
def my_function():
    return True

print(my_function())

# You can execute code based on the Boolean answer of a function:
# Print "YES!" if the function returns True, otherwise print "NO!".
def my_function():
    return True

if my_function():
    print("YES!")
else:
    print("NO!")

# isinstance() function, which returns True if the object is an instance of the specified type.
x = 200
print(isinstance(x, int)) # True
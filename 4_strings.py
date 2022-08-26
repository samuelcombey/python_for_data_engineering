### Strings ###
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:
print('hello')
print("hello")


## Assign String to a Variable ##
# Assinging a string to a variable is done with the variable name followed by an equal sign and the string.
a = "Hello"
print(a)


## Multiline Strings ##
# You can assign a multiline string to a variable by using three quotes:
a = """This is a multi-line string.
This is the second line."""
print(a)

a = '''This is a multi-line string.
This is the second line.'''
print(a)


## Strings are Arrays ##
# Square brackets can be used to access elements in the string.
# Get the character at position 1 (remeber that the first character has the position 0):
a = "Hello, World!"
print(a[1]) # e


## Looping through a String ##
# Since strings are arrays, you can loop through the characters in a string, with a for loop.
# Loop through the letters in the word "banaan":
for x in "banana":
    print(x)


## String Length ##
# The len() function returns the length of a string:

a = "Hello, World!"
print(len(a)) 


## Check String ##
# To check if a certain phrase or character is present in a string, we use the keyword in.

# Check if "free" is present in the following string:
txt = "The best things in life are free"
print("free" in txt)

# Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present")


## Chech if NOT ##
# To check if a certain phrase or character is not present in a string, we use the keyword not in.

# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free"
print("expensive" not in txt) 

# Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is not present")



### Slice Strings ###
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index separated by a colon (:).

# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5]) # llo


## Slice From the Start ##
# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5]) # Hello


## Slice To the End ##
# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:]) # llo, World!


## Negative Indexing ##
# Use negative indexes to start the slice from the end of the string:

# Get the characters
#From: "o" in "World!" (position -5)
#To, but not including: "d" in "World!" (position -2)
b = "Hello, World!"
print(b[-5:-2]) # orl



### Modify Strings ###


## Upper Case ##
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper()) # HELLO, WORLD!


## Lower Case ##
# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower()) # hello, world!


## Remove Whitespace ##
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # "Hello, World!"


## Replace String ##
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J")) # Jello, World!


## Split Strings ##
# The split() method returns a list where the text between the specified separator becomes the list items

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # ['Hello', ' World!']



### String Concatenation ###
# To concatenate, or combine, two strings, use the + operator
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c) # HelloWorld

# To add a space between them, add a " "
a = "Hello"
b = "World"
c = a + " " + b # Hello World



### Format Strings ###
# You can format a string by placing variables inside of curly braces:
# We can combine strings and numbers by using the formart() method.
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is Sam, and I am {}"
print(txt.format(age)) # My name is Sam, and I am 36

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) # I want 3 pieces of item 567 for 49.95 dollars.

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) # I want to pay 49.95 dollars for 3 pieces of item 567.



### Escape Characters ###
# An escape character is a backslash \ followed by the character you want to insert.

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
txt = "We are the so-called \"Vikings\" from the north."


## Other escape characters used in Python:
"""
Code	            Result
\'	                Single Quote	
\\	                Backslash	
\n	                New Line	
\r	                Carriage Return	
\t	                Tab	
\b	                Backspace	
\f	                Form Feed	
\ooo	            Octal value	
\xhh	            Hex value
"""



### String Methods ###
# All string methods return new values. They do not change the original string.

"""
Method	        Description
capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning
"""
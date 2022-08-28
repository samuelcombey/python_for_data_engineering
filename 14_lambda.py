### Lambda ###
# Lambda is a function that is defined without a name.
# It is a small and simple function, and it can be used to create anonymous functions.


## Syntax ##

# lambda arguments : expression
# The expression is executed and the result is returned.
#Add 10 to argument a, and return the result:
add_ten = lambda a : a + 10
print(add_ten(5))

# Lambda functions can take any number of arguments:
#Multiply argument a with argument b and return the result:
multiply = lambda a, b : a * b
print(multiply(5, 6))


## Why Use Lambda Functions? ##

# Lambda functions are useful when you need a short function but don't want to create a separate function.
# Lambda functions are also useful when you need a function that takes no arguments.
# The power of lambda is better shown when you use them as an anonymous function inside another function.

#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def my_func(n):
    return lambda a : a * n

#Use that function definition to make a function that always doubles the number you send in:
def my_func(n):
    return lambda a : a * n

doubler = my_func(2)
print(doubler(10))

#Or, use the same function definition to make a function that always triples the number you send in:
def my_func(n):
    return lambda a : a * n

doubler = my_func(2)
tripler = my_func(3)

print(doubler(10))
print(tripler(10))
### Operators ###

# Operators are used to perform operations on variables and values.


## Arithmetic Operators ##
# Arithmetic operators are used with numeric values to perform common mathematical operations:
"""
Operator	        Name	            Example
+	                Addition	        x + y	
-	                Subtraction	        x - y	
*	                Multiplication	    x * y	
/	                Division	        x / y	
%	                Modulus	            x % y	
**	                Exponentiation	    x ** y	
//	                Floor division	    x // y
"""


## Assignment Operators ##
# Assignment operators are used to assign values to variables:
"""
Operator	            Example	            Same As	
=	                    x = 5	            x = 5	
+=	                    x += 3	            x = x + 3	
-=	                    x -= 3	            x = x - 3	
*=	                    x *= 3	            x = x * 3	
/=	                    x /= 3	            x = x / 3	
%=	                    x %= 3	            x = x % 3	
//=	                    x //= 3	            x = x // 3	
**=	                    x **= 3	            x = x ** 3	
&=	                    x &= 3	            x = x & 3	
|=	                    x |= 3	            x = x | 3	
^=	                    x ^= 3	            x = x ^ 3	
>>=	                    x >>= 3	            x = x >> 3	
<<=	                    x <<= 3	            x = x << 3
"""


## Comparison Operators ##
# Comparison operators are used to compare two values:
"""
Operator	            Name	                    Example
==	                    Equal	                    x == y
!=	                    Not equal	                x != y
>	                    Greater than	            x > y
<	                    Less than	                x < y
>=	                    Greater than or equal to	x >= y
<=	                    Less than or equal to	    x <= y
"""


## Logical Operators ##
# Logical operators are used to combine conditional statements:
"""
Operator	       Name	                                                          Example
and	               Returns True if both statements are true	                      x > 5 and x < 10
or	               Returns True if one of the statements is true	              x > 5 or x < 10
not	               Reverse the result, returns False if the result is true	      not(x > 5 and x < 10)
"""


## Identity Operators ##
# Identity operators are used to compare the values of two variables:
"""
Operator	        Name	                                                          Example
is	                Returns True if both variables are the same object	              x is y
is not	            Returns True if both variables are not the same object	          x is not y
"""


## Membership Operators ##
# Membership operators are used to test if a value exists in a sequence:
"""
Operator	        Name	                                                          Example
in	                Returns True if a value exists in the sequence	                  x in y
not in	            Returns True if a value does not exist in the sequence	          x not in y
"""


## Bitwise Operators ##
# Bitwise operators are used to compare (binary) values:
"""
Operator	        Name	                     Description
&	                AND	                         Sets each bit to 1 if both bits are 1
|	                OR	                         Sets each bit to 1 if one of two bits is 1
^	                XOR	                         Sets each bit to 1 if only one of two bits is 1
~	                NOT	                         Inverts all the bits
<<	                Zero fill left shift	     Shifts bits to the left	
>>	                Signed right shift           Shifts bits to the right	
"""
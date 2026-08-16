"""
Operators and Data Types:
    
    This file explains the different operators, datatypes, and results of those operators and how thye apply to data types.

    To begin lets get you used to some comments and simple operators
"""

#This is a single line comment   : signle line comments stop being a comment at the next new line of a file.

"""
 this is a doc string and is considered a multilined comment
 these two forms of comments will direct you and give you information throughout this guide.
"""


#The assignment operator

x = 1

"""
    As you can see the assignment OPERATOR is the equal sign, the letter and the number area variable and integer respectively. These are known as OPERANDS.
"""


#in python variables do not need an explicit type declaration like int for a value of 1 (like so int x = 1)

#The Addition, Multiplication, Subtraction, and Division Operators

x + 1   #(this results in 2)
x - 1   #(this results in 0)
x * 5   #(this results in 5)
x / 0   #(this results in a NaN or more commonly known as NOT A NUMBER, however in python is also just raises an error and terminates your program)


"""
Data Types:

data types are just different ways on how to read the same sequence of bits to mean something.

bits are a switch that is either on or off and 8 bits are a byte 

Universal data constant: Word  (this is 16 bits) (Older books 1980's and below almost always talk in words)
1. Numerical Representation: Int (up to 64 bits), float (32 bits), double (64 or 86 bits), 
2. Character Representation: Char (8 bits), String (an array of chars)
3. Logical Representatation: Bool (1 bit), Null/Void (up to 64 bits)
4. Object Representation   : array, list, dictonary, sets, tuples, class, object, ect (these are all indeterminate amount of bits)
"""

x = 1     #int
x = 1.0   #float or double (python converts between them automatically based on if an overflow occurs on a float)
x = 'c'   #char
x = "HHH" #String

# Just know that these exist for now
x = []             #Lists
x = {}             #Dictionaries
x = ()             #Tuple
x = set()


"""
Advanced Operators
"""

#Bitwise operators:   Manipulates the bits directly
#Example starting default value of x is 5  or 0101 in bits and a second value when needed is 1 or 0001 in bits
x << 1  #Bitshift Left: Results in 1010 in bit form or 10 in decimal
x >> 1  #Bitshift Right:Results in 0010 in bit form or 2 in decimal
x | 1   #Bitwise or : Results in 0101 in bits or 5 in decimal
x ^ 1   #Bitwise exclusive or : Results in 0100 in bits or 4 in decimal
~x      #Bitwise Not:   Results in 1010 in bits or 10 in decimal
x & 1   #Bitwise And:   Results in 0001 in bits or 1 in decimal

#Adv. Math Operators
x**1  #Exponent
x//2  #Floor division (round down)
x % 1 #get the remainder after division
x += 1 #Short hand for x = x + Value
x -= 1 #Short hand for x = x - Value
x *= 1 #Short hand for x = x * Value
x /= 1 #Short hand for x = x / Value
x **= 1 #Short hand for x = x ** Value

"""
 Awesome! Thats all of the crash course for the operators and datatypes of python please do the following homework below:
 I would recommend doing it in scrap_paper.py
"""

#NOTE  YOU NEED TO KNOW THIS.  print() This is a function, dont worry what that is right now, just know that if you encase () with some value it prints it to the terminal
# Example print(x) or print(1)

#Question 1:   Write a small program to obtain the value of 1234567 * 1234567 * 1234567 * 1234567.  (All solutions are welcome as long as the awnser is printed to the terminal)
#Question 2:   What is the bit value after bitwising ANDing 1000111 and 10000
#Question 3:   What is something you leanred that you did not know about before? Can you apply it to a previous assignment?


"""
SOLUTIONS BELOW PLEASE TRY THESE FIRST BEFORE LOOKING AT THEM
"""




















































#Question 1 Solution:
"""
    print(1234567 * 1234567 * 1234567 * 1234567) or print(1234567**4)
    Value Answer: 2323050529221952581345121
"""

#Question 2 Solution:
"""
    The awnser is 0000000  or 0 in decimal
    
    Here is the breakdown:
    Steps:
        1. Normalize the Values  (make them equal in size)
        2. If two bits in the same position share a on bit then the resulting bit is one  

                 1000111      =      1000111      =      0000000
                   10000      =      0010000      =      0000000

"""

#Question 3 Solution:
"""
This question is always asked at the end to give you an oprotunity to reflect on this information.
"""


"""
Conditionals

This controls how operators are to be read, (when, where, what, why, while) This is becasue when a conditional exists it asks a question and then answers it.
"""

#if statements
"""
    WHEN something is true at this moment DO something OTHERWISE DO another thing
"""

# if CONDITIONAL:
#     SOMETHING
# else:
#     SOMETHING


#Example:
if 1:
    print("Hello!")


"""
Conditional Operators

for conditionals to exist you need some statement to exist about something

Similar to bitwise in thinking, BUT only returns a boolean (True or False | 1 or 0)
"""
x = 2
y = 1

x      #if x is not 0 (False)
x == 1 #equals to
x != 1 #Not equal to
x or y
not x  #Note: also !x works as well
x > y  #is Greater Than
x < y  #is Less Than
x >= y #is Greater Than or Equal To
x <= y #is Less Than or Equal To


"""
 If statements Extended

 elif can be used as a second conditional for something if the first one does not trigger.
 else is if both conditionals do not trigger this is a default operation
"""

if x == y:
    print("Bonjour")
elif y or x:
    print("ananas")
else:
    print("Pineapple Because why ananas there is already bananas?????")



#This is a fun one and it is called a tertiary expression basically a short hand (shortcut) for if-else with no other conditional and has ONE line of code each

#resulting_value if CONDITION else DEFAULT VALUE

0 if x != y else 1

# You can also add tertiary expressions inside lists to generate its elements (You will see why this is useful below)
list_example = [1 if x > y else 0]


"""
Switch Statments  (called match statements in some programming languages such as python)

This is a simpler way to do if elif chains 
all it does is say hey what does x ewual to and it tries to find a match. these cases can also be conditionals like x > y then do this
"""

match x:
    case 0: print("Its 0")
    case _ if x < y: print("Its 1")
    case _: print("This prints if no other case is triggered")

#NOTE: Treat the _ as ANY or ANYTHING

"""
while loops

WHEN something is true do this block of code UNTIL it is false
"""
i = 0
while y != x or i >= 5:
    print("Loopty Loop :D")
    i+=1



"""
For Loops

Do something for each thing in something UNTIL None
#Note: Okay for loops in python are weird as only for-each for loops exist in python, 
this means there must be a chain in independent values in some datastructure to iterate over. Basically, 
every datastructure that is Iterable or a Collection.

Collection is just a sequence of data that is group together. Lists are a type of collection.
Iterable is an interface which allows some object to be used in traversal

NOTE all collections are an Iterable but not all iterables are collections.
most programmers generally refer to both as just an iterable 
"""

#this is an example of a NOT VALID for loop in python
# for i=0; i > 0; i++:
#     print(i)

#Python must know how many elements exist before hand

#Proper for loop example  (each value of i is an int from some ITERABLE or COLLECTION, in this case its the list)
for i in [1, 2, 3]:
    print(i)

#Instead of creating these iterable types we have functions to do it for us. Here are some functions to know

for i in range(3):  #Same as above for loop
    print(i)

stored_values = [1, 2, 3, 4]
for i in stored_values:
    print(i)

for i, v in enumerate(stored_values):  #gets the value of the item in the list and its index of where it is in the list
    print(f'i = {i}   |   v = {v}')    #more on this later, this is called a FORMAT String or f string for short

for i in zip(stored_values, range(3)): #creates a tuple from other iterables, (allowing you to merge data from other variables as one variable)
    print(i)


#Remember those teriarty expressions? I told you it would be useful!
list_example = [i if i > 2 else 0 for i in stored_values]   #Creates a new list thats just the value of the list unless its less than 2 which is 0, so this example generates [0, 0, 3, 4]
#NOTE has to be TERTIARY first then the loop, this also works for while loops (But why would you do that?) Also these only work for non chained conditional statements 



"""
With

I am only going to brush over this because its outside the scope of this project but if you want to read a FILE or something stored outside the program
You need to use the with conditional

why? Because if an error occurs this manages cleanup and recovery, without it its a very dangerous operation which you still can do. But dont.

example

with open(filename, permissions) as file_variable_name:
"""




#NOTE: Again there are more functionalities but you dont need them, they are neich and recreatable with these as such the rest are outside the scope of this project



"""
Lesson over, is application time :D
"""

#Question 1:   Write a conditional where I print an integer whether it is even or odd
#Question 2:   Write a conditional where you print the value over every list element of a list of integers and print a new list after applying the following expression to it: 
#                if even add 1 if odd add 3 (Hint: Modify your previous method with return statements)
#Question 3:   What is something you leanred that you did not know about before? Can you apply it to a previous assignment?

"""
SOLUTIONS BELOW PLEASE TRY THESE FIRST BEFORE LOOKING AT THEM
"""





























































"""
Solutions
"""

#Question 1 Solution:
"""
    def is_even_or_odd(value):
        if value % 2 == 0:
            print("even")
        else:
            print("odd")

    We can use the MODULO operator to get the left over value from division. If a number does not divide cleanly into 2, then it is odd
"""

#Question 2 Solution:
"""
    def is_even(value):
        if value % 2 == 0:
            return True
        else:
            return False

    resulting_list = []
    for element in some_list:
        print(element)
        if is_even(element):
            element += 1
        else:
            element += 3

        resulting_list.append(element)

    print(element)
"""

#Question 3 Solution:
"""
This question is always asked at the end to give you an oprotunity to reflect on this information.
"""
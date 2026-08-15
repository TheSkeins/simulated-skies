"""
Conditionals

This controls how operators are to be read, (when, where, what, why, while) This is becasue when a conditional exists it asks a question and then asnwers it.
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
#Note: Okay for loops in python are weird as only for-each for loops exist in python, this means there must be a chain in independent values in some datastructure to iterate over
"""

#this is an example of a NOT VALID for loop in python
# for i=0; i > 0; i++:
#     print(i)

#Python must know how many elements exist before hand

#Proper for loop example  (each value of i is some ITERABLE which is just a seuqence of values that can be read via an index)
for i in [1, 2, 3]:
    print(i)


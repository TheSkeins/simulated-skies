"""
Advanced Datatypes:

This file is all about Lists, Dictionaries, Tuples, and Sets (Also functions because I need to talk about that somewhere)
"""


#Lists are by far the most useful advanced datatype of these four, lets break it down.
"""
Lists in python are a data structure called a Linked List, more specifically a Doublly linked list. That is you have some have some data with a point to another peice of data and a previous peive of data in NON continguous memeory.
Example of one element inside the hood of the code
{
Same(VALUE)
int* PointerToAddressInMemoryNext
int* PointerToAddressInMemoryPrevious
}

Basically python has some wrapper to encase a value to ensure all data is universal and the pointer (a memory address number) can point to another value or be None.

Here is the practical application in Python
"""

list_variable = []           #Initalize an empy list with None as both the pointer and data
list_variable = [1, 2]       #Initalize a list with two ints with 1 pointing
list_variable[0]             #get the first item in the list (in this case 1)  [The reson for this is because bits start at 0]
list_variable.append(3)      #Add 3 as an element to the list
list_variable.append([4, 5]) #add [4, 5] as an element to the list  (currently [1,2,3,[4,5]])
list_variable.pop()          #Removes the last item in the list, add a value like .pop(0) to remove a specific index, in this case the first element
list_variable[0:1:1]         #Get a Slice of an array, the values are as follows  [Start:Stop:Step]
list_variable[-1::-1]        #Return the list as reversed (sliced)  [all values not set from Start:Stop:Step are 0]
list_variable.reverse()      #Sets the array as reversed (instead of returning it reversed it sets the list in reversed order)


#NOTE: there is a very powerful function to learn call the len() function. This function gets the length of (how many elements exist it) different data structures.
#  More specifically its the first scope of elements IE len([1, 2, 3]) returns 3 and len([1, 2, [3, 4]]) also returns 3

len(list_variable)

#Dictionairies are also a very powerful tool that alows you to TRANSLATE one data to another.
"""
Dictionairies are a datastructure called a hashmap.
Each key (or inital value) MAPS (set to) its hashed value.  This is known as a Key Value Pair.
I wont get too detailed with Pythons Hashmap (mainly because I dont knwo the specifics) But lets say I have the word Cat

Cat goes through a function that converts it do some random string assortment such as AjKesLl, gets the INTEGER representation of it and Modulos to the dictionaies max size
then it gets its value and puts it in its list.  basically DICTONARY[INTEGER_REPRESENTATION] and you get your corrisponding value

Something to note is that all keys must be Unique but values do not have to be.
"""

dict_variable = {}                                      #Initalize and empty Ditionary
dict_variable = {"Key" : "Value"}                       #Set the dictionary with ONE key value pair
dict_variable = {"Key": 1, "Key2" : 0}                  #Set the dictioanry with multiple Key Value Pairs  (Notice the Comma? this ,)
dict_variable.get("Key")                                #Returns 1
dict_variable.update({1 : 0})                           #Adds a new Key value pair 
dict_variable.update({"Key" : 0})                       #Updates the existing key to have a value of 0
dict_variable.keys                                      #Returns all keys in a dictionary
dict_variable.items                                     #Returns all key value pairs as tuples
dict_variable.values                                    #Returns all values in a dictionary

len(dict_variable)


#Tuples are a way to zip different values together as one datastructure (Thats not appendable or popable)
"""
 This datatype doesnt seem like it can do much, but it is exteremely powerful because they use A LOT less memory than lists
 and group values together as one cohesive unit
"""

tuple_var = ()     #This is a useless thing but technically a tuple
tuple_var = (1, 2) #A tuple with 2 elements in it
x, y = tuple_var   #get values out of a tuple

len(tuple_var)

#Sets are "enhanced" tuples that now follow set operations through set theory. All add and remove operations create a new tuple 

set_var = set()                        #initalize an empty set
set_var2 = set(1, 2, 3, 4, 5)          #initalize a set with values
set_var.union(set_var2)                #Add all elements from both sets and return a new set (Does not edit the exist ones)
set_var.update(set_var2)               #Add all elements from both sets and change set_var to that new set
set_var.intersection(set_var2)         #Return the shared values between both sets as a new set
set_var.intersection_update(set_var2)  #Return the shared values between both sets as set_var
set_var.difference(set_var2)           #Return all values not shared between both sets as a new set
set_var.difference_update(set_var2)    #Return all values not shared between both sets into set_var
set_var.issubset(set_var2)             #Return a boolean if the values from set_var1 are in set_var2
set_var.issuperset(set_var2)           #Return a boolean if the values from set_var2 are in set_var1
set_var.isdisjoint(set_var2)           #Return a boolean if no elements in set_var1 intersect with set_var2
set_var.add(1)                         #Appends a new value to a set
set_var.discard(1)                     #Removes a value from a set

len(set_var)


# Function are blocks of code that you can repeat over and over again with a named call

def name(parameter1, parameter2):                  #Structure of a function and how to initialize them
    pass                                           #Pass is used to let the compiler know that this is valid and doesnt need to be set right now (as functions and conditionals cant be left blank)

def print_values(value1, value2):                  #Example with code
    print(value1)
    print(value2)

print_values(1, 2)                                 # How to call a function with different parameters  (parameters are set in chronological order)

def example3():
    return 1                                       # This returns a value to be used in later code

x = example3()

def default(param1="Hello, World!"):               # Adds a default type to parameters so you dont have to set all of them, can be over written
    print(param1)

def type_inference(param1):                        #example of IDE without knowing what type a value is (no auto complete available for you in ide)
    param1.add(1)

def type_inference(param1 : set):                  #Knows what value it is to it can be used for the IDE (DOES NOT EFFECT CODE OR INTERPRITER ONLY YOUR ENVIRONMENT TO CODE IN)
    param1.add(1)

#If you want to challenge yourself research how to do lambda functions in python, this is another function type


"""
Yay this lesson is over with! Time for some homwork :D
"""

#Question 1:   What are the main reasons to use a tuple over a list? What about a dictionary?
#Question 2:   Initalize a Set, a list, and a Dictionary with at least one element and print out the length of each data structure. Please pass all elements through a function to be printed out.
#Question 3:   What is something you leanred that you did not know about before? Can you apply it to a previous assignment?


"""
SOLUTIONS BELOW PLEASE TRY THESE FIRST BEFORE LOOKING AT THEM
"""





























































"""
Solutions
"""

#Question 1 Solution:
"""
    they use A LOT less memory than lists and group values together as one cohesive unit.

    Dictonairies are maps that translate one data to another, unlike lists that just store sequences of data together.
    (More meaning in the type and funtionality)
"""

#Question 2 Solution:
"""
  set_var  = set(1)
  dict_var = {"Key":1}
  list_var = [1]

  def print_length(data_structure):
    print(len(data_structure))

  print_length(set_var)
  print_length(dict_var)
  print_length(list_var)

  If you want to be fancy learn what a lambda function is.
"""

#Question 3 Solution:
"""
This question is always asked at the end to give you an oprotunity to reflect on this information.
"""
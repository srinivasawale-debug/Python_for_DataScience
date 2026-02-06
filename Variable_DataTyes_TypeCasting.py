
#variable and datatypes and typecasting

# A variable is the name  given to a memory location in a program.
# in this section, we will learn about variables, data types, and typecasting
# in Pythonto store and convert data effectively. ## Variables

# variables


# a = 30 # a is a variable or container that stores the integer value 30 #con

# b = "srinivas"  # b is a variable  that stores the string value "srinivas"

# c = 45.67  # c is a variable that stores the float value 45.67 

# d = True  # d is a variable that stores the boolean value True

# e = None  # e is a variable that stores the None value 

# print(type(a))  # prints the data type of variable a   <class 'int'>
# print(type(b))  # prints the data type of variable b   <class 'str'>
# print(type(c))  # prints the data type of variable c    <class 'float'>
# print(type(d))  # prints the data type of variable d     <class 'bool'>
# print(type(e))  # prints the data type of variable e     <class 'NoneType'>

     #data types in python


# common data types in python include:
# python has dynamic typing , meaning you do not need to declare the data type of a variable explicitly.


# int - integer values  
# float - floating-point values
# str - string values
# bool - boolean values (True or False)
# list - ordered collection of values
# tuple - ordered, immutable collection of values
# dict - key-value pairs
# set - unordered collection of unique values

# a = 100 # integer
# print(a)  # prints 100
# print(type(a))  # prints <class 'int'>


# b = 45.67  # float
# print(b)  # prints 45.67
# print(type(b))  # prints <class 'float'>


# c = "Hello, World!"  # string
# print(c)  # prints Hello, World!
# print(type(c))  # prints <class 'str'>


# d = True  # boolean
# print(d)  # prints True
# print(type(d))  # prints <class 'bool'>


# e = [1, 2, 3, 4, 5]  # list
# print(e)  # prints [1, 2, 3, 4, 5]
# print(type(e))  # prints <class 'list'>


# f = (10, 20, 30)  # tuple
# print(f)  # prints (10, 20, 30)
# print(type(f))  # prints <class 'tuple'>


# g = {"name": "Alice", "age": 30}  # dictionary
# print(g)# prints {'name': 'Alice', 'age': 30}
# print(type(g))  # prints <class 'dict'>

# h = {1, 2, 3, 4, 5}  # set
# print(h)  # prints {1, 2, 3, 4, 5}
# print(type(h))  # prints <class 'set'>



# What is Typecasting?

# Typecasting means converting one data type into another.

# In Python, it’s done using built-in functions like:
# int(), float(), str(), bool()
      
Types of Typecasting in Python


1) Implicit Typecasting

Python automatically converts one data type into another.

Example
 a = 10      # int
b = 2.5     # float

c = a + b    # int → float
print(c)            # 12.5
print(type(c))      # <class 'float'>

2) Explicit Typecasting

The programmer manually converts data types.




# examples of typecasting in python

# integer to float


# x = 10  # integer
# y = float(x)  # converting integer to float
# print(y)  # prints 10.0
# print(type(y))  # prints <class 'float'>



# # string to integer


# z = "25"  # string
# w = int(z)  # converting string to integer
# print(w)  # prints 25
# print(type(w))  # prints <class 'int'>


# # float to string


# p = 3.14  # float
# q = str(p)  # converting float to string
# print(q)  # prints "3.14"
# print(type(q))  # prints <class 'str'>


# # integer to boolean


# m = 1  # integer
# n = bool(m)  # converting integer to boolean
# print(n)  # prints True
# print(type(n))  # prints <class 'bool'>


# # float to integer
# f = 9.99
# i = int(f)  # converting float to integer
# print(i)  # prints 9
# print(type(i))  # prints <class 'int'>

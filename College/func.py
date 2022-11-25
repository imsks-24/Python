# important modules
# 1. math module

# now we can use m instead of writing math everywhere #or# from math import cos(to use cos function)
'''
from math import cos, sin 
# #only sin and cos will be imported
print('cos :', cos(3.14)) 
print('sin :', sin(3.14))

# to export every function from math
from math import *
print('cos :',cos(3))
print('sin :',sin(3))
print('pi :',pi)
'''
import math as m
'''
#2 more modules
import string as s
import random as r
'''

print('pi :', m.pi)
print('cos :', m.cos(3.14))
print('sin :', m.sin(3.14))


# User defined functions

# 1.
def average(a, b):
    return (a+b)/2


a = int(input("Enter a : "))
b = int(input('Enter b : '))
avg = average(a, b)
print('average :', avg)


# 2.
def greet(name, dish="Pasta"):
    print('Good Morning,', name)
    print('Please eat', dish)


greet('Satish', 'Samosa')
greet('Nitesh')


# 3.
def sum_of_list(a):
    print('Calculating...')
    return sum(a)


marks = [45, 16, 87, 98, 45]
sum_of_marks = sum_of_list(marks)
print('my sum of marks', sum_of_marks)


# 4.
def greetings(names):
    for name in names:
        print('Hello', name)


names = ['Satish', 'Nitesh', 'Ram']
greetings(names)

# SYS MODULE
# This module provides access to some variables used or maintained by the interpreter and
# to functions that interact strongly with the interpreter. It is always available.

# import sys
# n = len(sys.argv)
# print("Total arguments passed:", n-1)
#
# print("\nName of Python script:", sys.argv[0])
#
# print("\nArguments passed:", end=" ")
# for i in range(1, n):
#     print(sys.argv[i], end=" ")
# Sum = 0
#
# for i in range(1, n):
#     Sum += int(sys.argv[i])
#
# print("\n\nResult:", Sum)

# OS MODULE
# Python OS module provides the facility to establish the interaction between the user and the operating system.

# import os
# def current_path():
#     print(os.getcwd())
#     print()
# print("Current working directory before")
# current_path()
# os.chdir('../')
# print("Current working directory After")
# current_path()

# DATETIME MODULE
# import datetime
# x = datetime.datetime.now()
# print(x)


# # MATPLOTLIB
# Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# xpoints = np.array([25,20,15,15,15,15])
# ypoints = np.array([50,50,50,100,100,100])
#
# plt.plot(xpoints, ypoints)
# plt.show()


# ITERTOOLS
# An iterator is an object that contains a countable number of values.

# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
#
# print(next(myit))
# print(next(myit))
# print(next(myit))

# Create an Iterator
# -To create an object/class as an iterator we have to implement the
#  methods __iter__() and __next__() to our object.
# -The __iter__() method acts similar, we can do operations
#  (initializing etc.), but must always return the iterator object itself.
# -The __next__() method also allows us to do operations, and must
#  return the next item in the sequence.

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# StopIteration

# -To prevent the iteration to go on forever, we can use the StopIteration statement.
#
# -In the __next__() method, we can add a terminating condition to raise an error if
#  the iteration is done a specified number of times:

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#
#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#   print(x)

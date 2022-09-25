# Local Variables
# -If you create a variable with the same name inside a function, this variable will be local,
#  and can only be used inside the function. The global variable with the same name will remain
#  as it was,global and with the original value.

# Global Variables
# -Variables that are created outside of a function are known as global variables.
# -Global variables can be used by everyone, both inside of functions and outside.

# Example for Local & Global Variable
#     x = "awesome"
#
#     def myfunc():
#       x = "fantastic"
#       print("Python is " + x)
#
#     myfunc()
#
#     print("Python is " + x)

# RECURSION
# A function that calls itself is a recursive function.
# This method is used when a certain problem is defined in terms of itself.

# Greatest common divisor or Two numbers
   # def gcd(a, b):
   #    if b ==0:
   #       return a
   #    else:
   #       return gcd(b,a%b)
   # a = 128
   # b = 96
   # print(gcd(a, b))


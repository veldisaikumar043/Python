# LOGGING
# Logging is a means of tracking events that happen when some software runs.

# import logging
# logging.basicConfig(filename="mylog",level=logging.CRITICAL)
# logging.error("Error")
# logging.critical("critical")
# logging.warning("warn")
# logging.debug("Debug")
# logging.info("Info")

# EXCEPTION HANDLING
# - Exception handling is a concept used in Python to handle the exceptions and errors
#   that occur during the execution of any program.
# - Try and except statements are used to catch and handle exceptions in Python.
#   Statements that can raise exceptions are kept inside the try clause and the
#   statements that handle the exception are written inside except clause.

# try:
#     a,b=[int(x) for x in input("enter two numbers : ").split(",")]
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
#     print("please enter a non zero number")

# PICKLE AND UNPICKLE
# - The pickle module is used for implementing binary protocols for serializing
# and de-serializing a Python object structure.
#
# - Pickling: It is a process where a Python object hierarchy is converted into a byte stream
# - Unpickling: It is the inverse of Pickling process where a byte stream is converted into an object hierarchy.

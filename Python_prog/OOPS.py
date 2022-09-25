# Encapsulation
# This puts restrictions on accessing variables and methods directly and can prevent the
# accidental modification of data. To prevent accidental change, an object’s variable can
# only be changed by an object’s method. Those types of variables are known as private variables.

# class Student:
#     def setId(self,id):
#         self.id=id
#     def getID(self):
#         return self.id
#
#     def setName(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
# s=Student()
# s.setId(123)
# s.setName("Saikumar")
# print(s.getID())
#

# INHERITANCE
# Inheritance is the capability of one class to derive or inherit the properties
# from another class.It provides the reusability of a code.

# class BMW:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#
# class ThreeSeries(BMW):
#     def __init__(self, cruiseControl, make, model, year):
#         BMW.__init__(self,make,model,year)
#         self.cruiseControl=cruiseControl
#
# threeSeries=ThreeSeries(True,"BMW","328I",'2022')
# print(threeSeries.cruiseControl)
# print(threeSeries.make)
# print(threeSeries.model)
# print(threeSeries.year)

# POLYMORPHISM
# The word polymorphism means having many forms. In programming, polymorphism means the
# same function name (but different signatures) being used for different types.

# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")
#
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")
#
#     def type(self):
#         print("India is a developing country.")
#
#
# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
#
#     def language(self):
#         print("English is the primary language of USA.")
#
#     def type(self):
#         print("USA is a developed country.")
#
#
# obj_ind = India()
# obj_usa = USA()
# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()

# OBSTRACTION
# It hides the unnecessary code details from the user. Also,  when we do not want to give out
# sensitive parts of our code implementation and this is where data  abstraction came.
# Data Abstraction in Python can be achieved through creating abstract classes.
#
# from abc import abstractmethod,ABC
# class BMW(ABC):
#
#     @abstractmethod
#     def drive(self):
#         print("inside of abstract method")
#
# class ThreeSeries(BMW):
#
#     def drive(self):
#         print("Three series is being driven")



# from abc import abstractmethod, ABC
# class  TouchScreenLaptop(ABC):
#     @abstractmethod
#     def Scroll(self):
#         print("scroll method declared")
#
#     @abstractmethod
#     def click(self):
#         print("click method declared")
#
#
# class HP(ABC):
#     def scroll(self):
#         print("scroll method implemented in HP")
#
# class DELL(ABC):
#     def scroll(self):
#         print("scroll method implemented in DELL")
#
# class HPNotebook(HP):
#     def click(self):
#         print("click method implemented in HPNotebook")
#
# class DELLNotebook(DELL):
#     def click(self):
#         print("click method implemented in DELLNotebook")
#
# hpn=HPNotebook()
# hpn.click()
# hpn.scroll()
#
# dell=DELLNotebook()
# dell.click()
# dell.scroll()

# class InvalidPasswordException(Exception):
#     def __init__(self,msg):
#         self.msg=msg
# def EnterPassword(password):
#      if len(password)<8:
#          raise InvalidPasswordException("the password should be atleast 8 characters")
#      else:
#          print("you can proceed")
# a=input("enter password")
# EnterPassword(a)

from datetime import date
import time


# class musicEvent:
#     def __init__(self, startTime, endTime):
#         self.startTime = startTime
#         self.endTime = endTime
#         self.venue = []
#
#     def eventVenue(self, venue1):
#         self.venue.append(venue1)
#
#
# class musicVenue:
#     def __init__(self, name):
#         self.name = name
#         self.address = []
#
#     def eventAddress(self, address1):
#         self.address.append(address1)
#
#
# class musicAddress:
#     def __init__(self, street, city, state, country, zipcode):
#         self.street = street
#         self.city = city
#         self.state = state
#         self.country = country
#         self.zipcode = zipcode
#
#
# musicevent = musicEvent('03:00:00','04:00:00')
# musicvenue = musicVenue('RockStar')
# musicaddress = musicAddress("1st street", "srcl", "andra", "india", "123456")
# musicvenue.eventAddress(musicaddress)
# musicevent.eventVenue(musicvenue)
# print(musicevent.startTime)
# print(musicevent.endTime)
# for each in musicevent.venue:
#     print(each.name)
#     # print(each.endTime)
#     for eachadd in each.address:
#         print(eachadd.street)
#         print(eachadd.city)
#         print(eachadd.state)
#         print(eachadd.country)
#         print(eachadd.zipcode)

from threading import Thread
from threading import*
def EvenNumbersThread():
    sleep(1)
    for i in range(1,101):
        if(i%2==0):
            print(i,end=" ")
def OddNumbersThread():
    sleep(1)
    for i in range(1,101):
        if(i%2!=0):
            print(i,end=" ")
def MainThread():
    for i in range(1,101):
        print(i,end=" ")

even=Thread(target=EvenNumbersThread)
even.start()

print("Next")
odd=Thread(target=OddNumbersThread)
odd.start()

print("Next")
allNum=Thread(target=MainThread)
allNum.start()

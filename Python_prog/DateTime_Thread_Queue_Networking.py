# SORTING DATES
# from datetime import*
# dates=[]
# d1=date(2020,9,6)
# d2=date(2022,9,27)
# d3=date(2021,8,26)
#
# dates.append(d1)
# dates.append(d2)
# dates.append(d3)
#
# dates.sort()
# for d in dates:
#     print(d)

# CREDIT CARD USE CASE
# from datetime import*
# def validateCard(expDate):
#     if expDate>datetime.now().date():
#         print('valid')
#     else:
#         print('expired')
#
# validateCard(date(2021,12,23))

# THREAD
# A thread is a computation process that is to be performed by a computer.It is a sequence
# of such instructions within a program that can be executed independently of other codes.

# MULTITHREADING
#  - Multithreading is a threading technique in Python programming to run multiple threads concurrently
#    by rapidly switching between threads with a CPU help (called context switching).
#  - Multithreading aims to perform multiple tasks simultaneously, which increases performance,
#    speed and improves the rendering of the application

# THREAD SYNCHRONIZATION
#  - The threading module provided with Python includes a simple-to-implement locking mechanism that
#    allows you to synchronize threads. A new lock is created by calling the Lock() method, which
#    returns the new lock.
#
#  - The acquire(blocking) method of the new lock object is used to force threads to run synchronously.
#    The optional blocking parameter enables you to control whether the thread waits to acquire the lock.
#
#  - If blocking is set to 0, the thread returns immediately with a 0 value if the lock cannot be acquired
#    and with a 1 if the lock was acquired. If blocking is set to 1, the thread blocks and wait for the
#    lock to be released.
#
#  - The release() method of the new lock object is used to release the lock when it is no longer required.

# TICKET BOOKING USECASE WITH SLEEP
# from threading import*
# from time import*
# class bookMyBus():
#     def __init__(self,availableSeats):
#         self.availableSeats=availableSeats
#         self.l=Lock()
#     def buy(self,seatsRequested):
#         self.l.acquire()
#         print("total seats available : ",self.availableSeats)
#         if(self.availableSeats>=seatsRequested):
#             sleep(3)
#             print("confirming a seat ")
#             print("processing the payment")
#             print("printing the ticket")
#
#             self.availableSeats-=seatsRequested
#         else:
#             print("sorry NO seats available")
#         self.l.release()
# obj=bookMyBus(10)
# t1=Thread(target=obj.buy,args=(3,))
# t2=Thread(target=obj.buy,args=(4,))
# t3=Thread(target=obj.buy,args=(4,))
#
# t1.start()
# t2.start()
# t3.start()

# Queue
# Like stack, queue is a linear data structure that stores items in First In First Out
# (FIFO) manner. With a queue the least recently added item is removed first.

#  Queue Object has two methods:
#  1. put(item):
#  Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
#  2. get():
#  Remove and return an item from the queue. If queue is empty, wait until an item is available.

# there are three types of Queues
#  -Queue            :FIFO
#  -LifoQueue        :LIFO
#  -PriorityQueue()  :select from dictionary on the bases of key/value index

# THREAD COMMUNICATION
# - Given multiple threads in the program and one wants to safely communicate or exchange data between them.
# - In programming, to reduce the ideal time of the processor we create multiple threads and assign different
#   sub tasks to every thread. Hence, there must be a communication facility and they should interact with each
#

# notify() Method: When we want to send a notification to only one thread that is in
#                  waiting state then we always use notify() method.
# wait(time) Method: The wait() method can be used to make a thread wait till the
#                    notification(notify()) got and also till the given time will end.

# THREAD COMMUNICATION USING NOTIFY AND WAIT
# from threading import*
# from time import*
# class Producer:
#     def __init__(self):
#         self.products=[]
#         self.c=Condition()
#
#     def produce(self):
#         self.c.acquire()
#
#         for i in range(1,5):
#             self.products.append("product"+str(i))
#             sleep(1)
#             print("Item Added")
#         self.c.notify()
#         self.c.release()
#
# class Consumer:
#     def __init__(self,prod):
#         self.prod=prod
#
#     def consume(self):
#         self.prod.c.acquire()
#         self.prod.c.wait(timeout=0)
#         self.prod.c.release()
#         print("orders shipped",self.prod.products)
#
# p=Producer()
# c=Consumer(p)

# t1=Thread(target=p.produce)
# t2=Thread(target=c.consume)
#
# t1.start()
# t2.start()



# remove elements from A that are in B and note position of that element in a new array
#
# list=[]
# A=[1,2,3,4,5,6,7,8,9]
# B=[2,5,6,9]
# for i in B:
#      if i in A:
#          list.append(A.index(i)+1)
#          A.remove(i)
# print(list)

# To check given elements are present or not in fibonacci series
#
# a=0
# b=1
# i=c=0
# list=[]
# list1=[3,5,88,33,44,55,1,2,5]
# list2=[]
# list.append(a)
# list.append(b)
# while(i<=10):
#     c = a + b
#     list.append(c)
#     a=b
#     b=c
#     i+=1
# for i in list1:
#     if i in list:
#         list2.append(1)
#     else:
#         list2.append(0)
#
# print(list2)


# TO FIND THE REPEATATION OF GIVEN WORD IN AN ARRAY
# def freq(str):
#     str1 = str.split()
#     print(str1)
#     str2 = []
#     for i in str1:
#         if i not in str2:
#             str2.append(i)
#     print(str2)
#     for i in range(0, len(str2)):
#         if str2[i] == "guava":
#             print(str.count(str2[i]))
#             break
#
#
# def main():
#     str0 = 'apple mango apple orange orange apple guava mango mango apple'
#     freq(str0)

# TO DELETE THE ARRAY ELEMENT AT GIVEN INDEX
import numpy as np
a = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
index = 9
a = np.delete(a, index)
print(a)
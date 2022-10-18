# a = 10
# print(a)
# b = 20.54
# print(b)
# c = True
# print(c)
# d = "Iamthebestsaikumar"
# print(d[:8:2])

# lst=['india','china','italy']
# lst.append('canada')
# del(lst[2])
# lst.insert(int(len(lst)/2),'usa')
# print(lst)
# a=;
# print(a)

# lst={1:"onions",2:"lettuce",3:"tomato",4:"olives",5:"peppers",6:"tomatoes"}
#
# print(lst)
# first=int(input("enter first choice "))
# print(lst[first])
# second=int(input("enter second choice "))
# print(lst[second])
# third=int(input("enter third choice "))
# print(lst[third])
#
# howMany=int(input("enter no.of Sandwiches you want "))
# total=5*howMany
# print(f"Total = {total}$")

#GRADING APPLICATION
# maths=int(input("enter maths marks "))
# physics=int(input("enter physics marks "))
# chemistry=int(input("enter chemistry marks "))
# if maths>=35 and physics>=35 and chemistry>=35:
#     print("you passed the exams")
#     avg=(maths+physics+chemistry)/3
#     if avg<=59:
#         print("Grade: C")
#     elif avg<=69:
#         print("Grade: B")
#     else:
#         print("Grade: A")
#
# else:
#     print("you failed the exam")

# #PRINT 1 TO 100 SKIP 10 MULIPLES & BREAK CROSSES 100
# n=int(input("enter a number"))
# i=0
# while(i<=n):
#     i+=1
#     if i%10==0:
#         continue
#     elif i<=100:
#         print(i)
#     else:
#         break

# NUBER IS PRIME OR NOT
# n=int(input("enter a number "))
# primeFlag=True
# for i in range(2,n-1):
#     if n%i==0:
#         primeFlag=False
# if (primeFlag):
#     print("Prime number")
# else:
#     print("Not a Prime number")

# #ATM CHECKER
# accBalance=10000
# print("1 for check balance")
# print("2 for withdraw ")
# print("3 for deposit cash")
# print("4 for deposit check")
# n=int(input("enter a number"))
# if n==1:
#     print("available balance is",accBalance)
# elif n==2:
#     withdraw=int(input("enter amount you want to withdraw"))
#     accBalance=accBalance-withdraw
#     print("amount withdrawn is ", withdraw)
#     print("available balance is", accBalance)
# elif n==3:
#     depositcash = int(input("enter amount you want to Deposit cash"))
#     accBalance=accBalance+depositcash
#     print("available balance is", accBalance)
# elif n==4:
#     depocheck=int(input("enter amount you want to Deposit cash"))
#     print(depocheck," this amount you want to Deposit cash")

#

Input = ["https://www.isb.edu", "www.google.com", "http://cyware.com",
         "https://www.gst.in", "https://www.coursera.org",
         "https://www.create.net", "https://www.ontariocolleges.ca"]


# Function to sort in tld order
def tld(Input):
    return Input.split('.')[-1]


# Using sorted and calling function
Output = sorted(Input, key=tld)

Printing output
print("Initial list is :")
print(Input)
print("sorted list according to TLD is")
print(Output)
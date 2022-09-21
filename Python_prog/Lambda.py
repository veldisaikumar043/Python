# LAMBDA
# -A lambda function is a small anonymous function.
# -A lambda function can take any number of arguments, but can only have one expression.
# Syntax
# lambda arguments : expression
#
# Example 1
# x = lambda a : a + 10
# print(x(5))

# Example 2
# l=lambda x: 'yes' if x%2==0 else 'no'
# print(l(11))

#LAMBDA FUNCTION
# A function definition that takes one argument, and that argument will be multiplied with an unknown number.
# By using function definition to make a function that always doubles the number you send in.
#    def myfunc(n):
#    return lambda a : a * n
#
#    mydoubler = myfunc(2)
#
#    print(mydoubler(11))

# Lambda using the Filter
# lst=[10,2,33,45,89,2]
# result=list(filter(lambda x:x%2==0,lst))
# print(result)

# Lambda using the Map function
# lst=[2,3,4,5]
# result=list(map(lambda n:n*2,lst))
# print(result)


# Regular Expression:
# A Regular Expressions (RegEx) is a special sequence of characters that uses
# a search pattern to find a string or set of strings. It can detect the presence
# or absence of a text by matching it with a particular pattern.
# Python provides a re module that supports the use of regex in Python.

# EXAMPLE OF CHECK FOR DIGIT IN WORD REGEX,FINDALL
# import re
# word='hello12@3sa2&244i'
# Numbers=re.findall(r'\d',word)
# specilChar=re.findall(r'\W',word)
#
# print(''.join(Numbers))
# print(''.join(specilChar))

# EXAMPLE USING SPECIAL CHARACTERS
# import re
# str="Take up One idea at a time"
# result=re.search(r'^T\w*',str)
# print(result.group())

# QUANTIFIERS
# In regular expressions, quantifiers match the preceding characters or character sets a number of times.
#   *    Match its preceding element zero or more times.
#   +    Match its preceding element one or more times.
#   ?    Match its preceding element zero or one time.
#  {n}   Match its preceding element exactly n times.
# {n,m}  Match its preceding element from n to m times.


# import re
# str="Take up One idea at a time One"
# result=re.findall(r'O\w{1,2}',str)
# result1=re.findall(r'O\w*',str)
# print(result)
# print(result1)






# LIST TO TUPLE
# lst=[67,34,"xyz"]
# tpl=tuple(lst)
# print(type(tpl))

#LIST TO DICTIONARY
# lst = ['a', 1, 'b', 2, 'c', 3]
# res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
# print(type(res_dct))
#            OR
# lst = ['a', 1, 'b', 2, 'c', 3]
# it = iter(lst)
# res_dct = dict(zip(it, it))
# print(type(res_dct))
# print(res_dct)

#DICTIONARY TO LIST
# dict={'a': 1, 'b': 2, 'c': 3}
# list1 = list(dict.items())
# print(type(list1))


# Remove Duplicate elements in list
l1=eval(input('enter list numbers by comma'))
l2=[]
for each_value in l1:
    if each_value not in l2:
        l2.append(each_value)
print(l2)




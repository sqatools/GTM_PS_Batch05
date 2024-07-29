'''
*** we can have list inside a list
*** in list data type we can add any type of data like string, int, float, complex, tupple, dictionary
***indexing is possible
***Curly Braces {} Dictionaries: Used to create dictionaries, which store data in key-value pairs
***Square Brackets [] Lists: Used to create lists, which store ordered collections of items (elements)
***Parentheses (): Tuples: Used to create tuples, which store ordered, immutable collections of items.
'''

print('_' * 80)
list2 = ['a','b','c',[4,7,8],[9],[10],'c'] ##we have list inside a list here##
print(list2)
print(list2[3])

#############tuple_data_type#########################
'''
***tupple is in muttable data type, once defined, we can't modify
***tuple can store all type of data(int,float,string,list,dic,set,boolean)
***tuple follow both positive and negitive values as like string and list
***tuple defined with round bracket
***were should we use list , were we should we use tuple ?
***we should use tuple where the data is fixed, which is not going to change once it is defined
eg: months in a year, no.of alphabets, days in a week
***we should use list data type were we see data continuesly changing
***tuple is faster than the list in terms of performances
'''
print('_' * 80)
tup1 = ('abc', 4, 4.5, [4,5,6], (1,2,3),{'name' : 'John'},{5,6,7,8}, True)
print(tup1)
print(type(tup1))

tup2 = (4,6,7,(3,9,2),'a','b')
print(tup2)
print(tup2[3])
print(tup2[3][2])

####################Dictonary_datatype####################
'''
***dic is stored in form of key value pair
 eg : if we want to store persons name, we store in a format of Name : lokesh
***each data can be identify by unique key
***dic does not follow indexing
***dic is a muttable data type, we can update the data whenever we want
***dic doesn't allow duplicate key, the keys are always unique
***All imutable data type can be key in the dictonary, int,float,string,tuple, boolean.
***All type of data can be value in dictonary like int,float,string,list,dictionary, set, boolean
***
'''


dict1 = {'a' : 1234, 'b' : 567}
print(type(dict1))


######################set data type########################################
'''
***set stores only unique values
***set only contain only immutable data type : int,float,string,tuple,boolean
***set is mutable data type
***set doesn't follow any indexing, it stores in random order
'''
print ('_' * 80)
set1 = {4,6,7,4.5,'hello',(4,6,7),4,4,6,6}
print(set1)
print(type(set1))


set2 = {4,6,7,8}
set2.add(400)
print(set2)
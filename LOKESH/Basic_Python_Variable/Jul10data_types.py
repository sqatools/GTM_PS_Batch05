##############python_datatypes################

'''
1.Numeric data Types:	int, float, complex
2.Sequence data Types:	string, list, tuple
3.Dictionary data types : 
4.Set Types: set, frozenset
5.Boolean Type:	TRUE, FALSE
'''

################integer_datatype##############
'''
Intiger data type:
intiger is in-muttable datatype
once it is assigned, we cannot change it

in below example we kept 
var1 = 100
var1 = 200

***here 100 will replace with 200, this is called replacing
if we have both 100 and 200 in var1 then this is called updation

*** we can assign both positive and negitive values
***there is no limit of values in the intiger, we can assign any long value in the integer
***only whole number will be consider as intiger, (decimals not consider as intiger)
***in python everything is object
'''
var1 = 100
var1 = 200

print(type(var1))
print(var1)
#<class 'int'> 200

var2 = 554545454544545454545454545454545454
print(var2, type(var2))
#554545454544545454545454545454545454 <class 'int'>

var3 = -565989874657513549872349884
print (var3, type(var3))
#-565989874657513549872349884 <class 'int'>

##############_FLOAT_DATA_TYPE#################
'''
***intiger is in-muttable datatype once it is assigned, we cannot change it
***all positive and negitive values will be considered as float
*** float values only store pointer and decimal values
*** there is no limit of values in the float, we can assign any long value in the float
'''

var_a = 55.45
var_b = -660.30
var_c = 565646565.46797494949778
var_d = 0.0

print('var_a:', var_a , type(var_a))
print('var_b:', var_b , type(var_b))
print('var_c:', var_c , type(var_c))
print('var_d:', var_d , type(var_d))

##############COMPLEX_DATA_TYPE###############
'''
->Complex number is combination of real and imaginary number
->Complex data type is immutable data type
->Complex number can contain positive and negitive values
'''

print('_' * 80)
#x+yj
data = 10+20j
print (data, type(data)) # this is called complex data_type

data2 = 40 + 50j
data3 = data + data2

print (data3, type(data3))
# here above 10 + below  40 = 50
# here above 20 + below  50 = 70



######################Sequential_Data_Types################
######################String_Data_Types##################
'''
***string is immutable datatype, once it is defined we cannot be changed
***anything which is storing in single quote, double quote, thriple quote consider as a string
***string follows both positive and negitive indexes
'''
str1 = ''
str2 = "HI"
str3 = "GOOD MORNING"
str4 = 'MY NAME IS "LOKESH"'
str5 = "My country name os 'INDIA'"

# str6 :
# "A three-line paragraph condenses ideas concisely"\
# "while delivering essential information. For example,"\
# "effective communication is crucial in both personal and "\
# "professional settings, as it ensures clarity, reduces "\
# "misunderstandings, and fosters collaboration. By honing communication "\
# "skills, individuals can build stronger relationships, achieve goals "\
# "more efficiently, and create a positive impact in their communities."

str7 = "1.Apple\n" \
       "2.Banana\n" \
       "3.Mango\n" \
       "4.Pineapple\n" \
       "5.Lichi\n"
print (str7)

########Indexing in the string##########
str_a = "python"

'''
Positive Indexing:  0  1  2  3  4  5    
                    P  Y  T  H  O  N
Negitive Indexing: -6 -5 -4 -3 -2 -1
'''
print(str_a[0])
print(str_a[-6])

print(str_a[4])
print(str_a[-2])

str_b = "hello"
#printing "e" in both positive and negitive value
print(str_b[1])
print(str_b[-4])

str_c = "good morning"
print (str_c)
print(len(str_c))
print (str_c[5])
print (str_c[-7])

str_d = "HELLO"
str_e = "Good Morning"
str_f = str_d+" "+str_e
print (str_f)
print (type(str_f))

##############################List_Data_Type####################
print('_' * 80)

'''
***list is mutable data type, once it is defined we can change it
***Lists are used to store multiple items in a single variable.
***list can contain all type of data like int, float, string, list, tuple,dict, set, boolean
*** list follows positive and negitive indexing as like string
***list is defined in [ square bracket ] eg : thislist = ["apple", "banana", "cherry"]
***List items are ordered, changeable, and allow duplicate values.
***we can define list inside a list
***we can define tuppple inisde a list
***we can define dicnary inside a list
***list values are camma separated

***use append keyword practice
'''

list1 = [3, 33.56, 'hello', [4,6,7],(3,8,2),{'a'_:123 , 'b'_: 345}, {4,6,8,2}, True, None]
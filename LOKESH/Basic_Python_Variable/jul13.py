#####################string_convertion###################
##string - > int
###we cannot convert string into intiger if it contains characters/words
###we can convert string into intiger if it contains only numbers
str1 = "hello"
num1 = str(str1)
print(num1, type(num1))

# str2 = 'hello'
# num2 = int(str2)
# print(num2, type(num2))

str3 = "365478"
num3 = int(str3)
print(num3 , type(num3), num3*2)

###string_to_float######################
'''
str_a = "python"
num_a = float(str_1)
print(num_a, type(num_a))
'''
##could'nt convert stringbto python : "python"

##if string contains only pointer values then we can convert string into float
str_b = "55.678"
num_b = str(str_b)
print(num_b, type(num_b), num_b*10)

############string_to_list#################################
str_c = "programing"
list_c = list(str_c)
print(list_c, type(list_c))
#######we can do indexling here####
print(list_c[0])

######convert string to tupple####################
str_d = "python"
tup_d = tuple(str_d)
print(tup_d , type(tup_d))
#######we can do indexling here####
print(tup_d[-1])

###########string to dictionary####################
# str_e = "Hello"
# dict_e = dict(str_e)
# print(dict_e , type(dict_e))
print('-' * 80)
import json
str_f = '{"Name" : "LOKESH", "Email" : "lokesh.pathuri@gmail.com" , "City" : "Hyderabad"}'
data_dict = json.loads(str_f)
print(data_dict, type(data_dict))
print(data_dict['Name'])
print(data_dict['Email'])
# with the help of json module we can convert string to dictionary

###########string to set####################
print('_' * 80)

str_t = "python_programing"
set_t = set(str_t)
print(set_t , type(set_t))

##set stores only unique values
##set display data not in a order


###########string to boolean#################
print ('_' * 80)

str_e = ''
bool_e = bool(str_e)
print(bool_e , type(bool_e))

str_f = 'Hello'
bool_f = bool(str_f)
print(bool_f, type(bool_f))


########################list ###########################

###list - > int ### convertion is not possible
###list - > float ## convertion is not possible
###list - > string ## is possible
print('_' * 80)

list_c = [1,2,3,4,'l','m     ','n']
str_i = str(list_c)
print(str_i , type(str_i))
print(str_i[0],str_i[1], str_i[-1] )

###list - > tupple####
print ('_'  * 80)
list_d = [40,50,60,70,80]
tup_d = tuple(list_d)
print(tup_d , type ( tup_d))
print(tup_d [1])


#####list -> dictionary#########convertion is not possible
'''
# print("_" * 80)
# list_e = [4,5,6,7,8]
# dict_e = dict(list_e)
# print(dict_e , type (dict_e))error :cannot convert dictionary update sequence element #0 to a sequence
'''

list1 = ['p','q','r']
list2 = [3,6,7,8]
result = dict(zip(list1, list2))
print(result, type(result))
###in above the extra value 8 is not printed

########list - > set######################################
print('_' * 80)
list_h = [2,3,4,2,6,7,8,4]
set_h = set(list_h)
print(set_h , type(set_h))

############list -> boolean##################################
print('_' * 80)
list_k = ['']
bool_k = bool(list_k)
print(bool_k, type(bool_k))


list_L = ['LP']
bool_L = bool(list_L)
print(bool_L, type(bool_L))



















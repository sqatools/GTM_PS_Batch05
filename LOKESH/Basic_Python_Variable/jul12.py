###########################BOOLEAN_DATA_TYPE####################3
'''
***Boolean is imutable data type
***Boolean can consider with only two values true or false
***All the conditional output will be consider in boolean always
***we can't do arthematic functions on top boolean data_type
'''

var1 = True
print(var1, type(var1))

var2 = False
print(var2, type(var2))


#################################Convertion_of_data_types###############3
##int - > float
print('_' * 80)
num1 = 35
print(num1, type(num1))
print(id(num1))
num2 = float(num1)
print(num2, type(num2))
print(id(num2))

###int - > string
print('_' * 80)
var_a = 567
print(var_a, type(var_a))
print(id(var_a))

var_b = str(var_a)
print(var_b,type(var_b))
print(id(var_b))

print (var_b[0])

###int - > list
# var_c = 676
# var_c = list(var_c)
# print(var_c)

#TypeError : 'int' object is not iterable
#we can't convert intiger to list

###int - > tuple # convertion is not possible
### int - > dictionary ## convertion is not possible
###int - > set  3# is not possible


###int -> boolean it is possible

print('_' * 80)
num1 = 0
bool_val = bool(num1)
print(bool_val)

num2 = 1000
bool_val = bool(num2)
print(bool_val)

num3 = 10
bool_val = bool(num3)
print(bool_val)


#####float_convertion
print('_' * 80)

##float - > int

var_c = 66.45
var_d = int(var_c)
print(var_d, type(var_d))

##float - > string

var_e = 55.45
var_f = str(var_e)
print(var_f,type(var_f))
print (var_f[3])

##float - > list # convertion is not possibel
##float - > tuple # convertion is not possibel
##float - > dictionary # convertion is not possibel
##float - > set # convertion is not possibel
##float - > boolean

print('_' * 80)

val_g = 00.00
val_h = bool(val_g)
print(val_h,type(val_h))

val_i = 33.33
val_j = bool(val_i)
print(val_j,type(val_j))

val_k = 00.33
val_l = bool(val_k)
print(val_l,type(val_l))
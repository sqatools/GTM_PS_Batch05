"""
lambda function is anonymous function which does not have body.
"""
fun_val = lambda a, b : a+b
print("Addition of values :", fun_val(4, 7))

fun2 = lambda x : x%2 == 0

print("check even :", fun2(7)) # False
print("check even :", fun2(8)) # True


##################
print("_"*50)
# Map : Map function help to apply list of input to specific function.

def square(n):
    return n**2

list1 = [5, 8, 2, 6, 4, 7]

square_result = list(map(square, list1))
print("square result :", square_result)  # [25, 64, 4, 36, 16, 49]

square_result2 = list(map(lambda x:x**2, list1))
print("square result :", square_result2) # [25, 64, 4, 36, 16, 49]

lambda_value = lambda x: x**2
print(lambda_value(10))

print("_"*50)
###########################################
# filter : filter return only the favourable output which is matching with condition

list2 = [4, 16, 17, 3, 2, 8, 11]

filter_output = list(filter(lambda x: x%2 == 0, list2))
print("Filter Output :", filter_output) # [4, 16, 2, 8]

print("_"*50)
###########################################
# reduce : reduce return the single output from list of values
from functools import reduce

list3 = [10, 30, 40, 50, 12]
output = reduce(lambda x, y: x+y, list3)
print("addition of all the values :", output)

output_mul = reduce(lambda x, y: x*y, list3)
print("Multiplication of all values :", output_mul)



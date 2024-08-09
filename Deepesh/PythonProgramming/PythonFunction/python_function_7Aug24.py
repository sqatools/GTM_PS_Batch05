"""
def function_name():
    code
"""


def addition():
    num1 = 40
    num2 = 50
    print("addition :", num1 + num2)


# addition()

def multiply_values(param1, param2):
    print("value of param1 :", param1)
    print("value of param2 :", param2)
    print("Multiplication of numbers :", param1 * param2)
    print("Addition :", param1 + param2)


# pass by value : directly pass values for the parameters
# multiply_values(3, 7)

print("_" * 50)
# pass by reference : provide reference any other variable which is holding a value
x = 40
y = 5
# multiply_values(x, y)

print("_" * 50)
# change the sequence of parameters while calling the function
multiply_values(param2=600, param1=6)

print("_" * 50)


############# Function with default parameters ##########
# If any parameter of the function has default value, then function will be called and param will consider default value
# If any parameter has default value, then it will come at right of the parameter.

def function_2(p1, p2=500):
    print("Division of values :", p2 / p1)


function_2(10)  # 50.0
# function_2(5, 125) # # 25.0

def function_3(a=100, b=5):
     print("value of a and b :", a, b)

#function_3(30, 40)
#function_3()


def function_4(x, y, z):
    print("square of each value :", x**2,":", y**2, ":", z**2)

#function_4(4, 6) # TypeError: function_4() missing 1 required positional argument: 'z'
#function_4(3, 6, 8)  # : 9 : 36 : 64



##########################################
# *args argument values

def print_values(*args):
        print("args values :", args)
        for val in args:
            print(val)

print_values(4, 6, 8, 23, 12, [1, 4, 5],  ' pYTHON pROGRAMMING')

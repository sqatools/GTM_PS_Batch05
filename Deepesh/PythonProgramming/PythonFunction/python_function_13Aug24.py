"""
# python variable scope
->  global variable : we define global variable outside of the function, the global variable
                     scope to wider across the module and all the function in the module
                     can access the global variable.

                      -> if we defined a variable inside the function with same name
                      as global variable then that particular variable is a local variable
                      and its value scope is limited to the function

                      -> if you want to update the value of global variable inside the function
                      then we have to use keyword global <variable name>, then we can update the
                      value of global variable across the module

->  local variable : When we define any variable inside the function, then it is known as
                     local variable, the scope of the local variable is limited to the
                     specific function where we have defined it.

->  non-local variable : The variable that we defined inside the outer function and outside of
                    the inner function, then it known as non-local variable, then scope of
                    non-local variable is limited to outer and inner functions.

                    -> If we want update the value of non-local variable inside the inner function
                       then we have to use keyword nonlocal <variable_name> and assign updated value.
"""

var_x = 700  # global variable


def function1():
    global var_x
    var_y = 500  # local variable
    var_x = 800
    print("local variable var_y:", var_y)
    print("global variable var_x:", var_x)


def function2():
    var_z = 400  # local variable
    print("local variable var_z :", var_z)
    print("global variable var_x:", var_x)


"""
function2()
print("_" * 50)
function1()
print("_" * 50)
function2()
"""


############### Non local variable #############

var_A = 900 # global variable

def outer_function():
    var_B = 1000 # non local variable

    def inner_fun1():
        print("--------inner_fun1--------")
        var_C = 1100 # local variable
        print("global variable var_A :", var_A)
        print("non local variable var_B :", var_B)
        print("local variable var_C :", var_C)

    def inner_fun2():
        print("\n--------inner_fun2--------")
        nonlocal var_B
        var_D = 1200 # local variable
        var_B = 1300
        print("global variable var_A :", var_A)
        print("non local variable var_B :", var_B)
        print("local variable var_C :", var_D)

    print("var_B :", var_B)

    inner_fun1()
    inner_fun2()
    inner_fun1()

outer_function()


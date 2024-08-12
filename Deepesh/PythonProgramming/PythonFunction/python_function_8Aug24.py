"""
def function_name():
    code
"""


# **kwargs parameters to the function
# kwargs accepts the values in the dictionary format like key value pair.

def login_fun(**abc):
    print(abc)
    db_username = "Admin"
    db_password = "admin@123"
    if abc['username'] == db_username and abc['password'] == db_password:
        print("Login successful")
    else:
        print("Invalid credentials")


# login_fun(username='john', password='P@ssw0rd', email='user123@gmail.com')
# login_fun(username='Admin', password='admin@123', email='user123@gmail.com')


def function_5(param1, *args, **kwargs):
    print(f"Multiple by 2 : {param1} :", 2 * param1)
    result = [x ** 2 for x in args]
    print("square result :", result)

    for k, v in kwargs.items():
        print(k, ":", v)


# function_5(4, 2, 5, 6, name='rahul', phone=87876867, email='rahul@gmail.com')
"""
Multiple by 2 : 4 : 8
square result : [4, 25, 36]
name : rahul
phone : 87876867
email : rahul@gmail.com
"""


####################################
# function with return statement

# function that return a single value
def factorials(n):
    fact = 1
    for i in range(n, 0, -1):
        fact = fact * i

    return fact
    # Any code after the return statement will be unreachable
    # print("factorial calculated successfully")


result = factorials(6)
print("factorial result :", result)


# function that return multiple values
def function_three_return(n1, n2, n3):
    add = n1 + n2
    multiply = n1 * n2
    divide = n3 / n1
    return add, multiply, divide


result = function_three_return(5, 7, 8)  # [:2]
print("multiple return value :", result)  # (12, 35, 1.6)

p, q, r = function_three_return(5, 70, 80)
print("addition :", p)  # addition : 75
print("multiplication :", q)  # multiplication : 350
print("divide :", r)  # divide : 16.0

print("_" * 50)


# function with parameter data type and return type
def math_operation(num1: int, num2: str, num3: float) -> str:
    print("repeat string :", num2 * num1)
    # print("add float with int :", num1 + num3)
    return num2 * num1


# str_output = math_operation(2, 'Hello', 3.5)
# print("string output  :", str_output)

# provide un-expected data while calling the function, then it will show warning
# but still we can execute the code.
str_output = math_operation(4.5, 40, 'Python')

print("_" * 50)

# call function inside the function
def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def subtraction(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 // n2

def calc(choice, n1, n2):
    """
    These function act like calculator and user can define choice to perform the operation
    :param choice: Integer value to be pass between 1 to 4
    :param n1: first value param
    :param n2: second value param
    :return: None
    """
    if choice == 1:
        print("addition of values :", add(n1, n2))
    elif choice == 2:
        print("Multiplication of the values  :", multiply(n1, n2))
    elif choice == 3:
        print("Subtraction of the values :", subtraction(n1, n2))
    elif choice == 4:
        print("Division of values :", divide(n1, n2))

calc(1, 40, 50)
calc(2, 35, 50)
calc(3, 400, 50)
calc(4, 700, 50)

# retrive the documentation of any function
print(calc.__doc__)


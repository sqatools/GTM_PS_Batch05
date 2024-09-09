"""
Decorator which decorate the code without changing its existing functionality
"""

def decor_fun(func):
    def inner(*args):
        print("*"*30)
        func()
        print("*"*30)
    return inner


def decor_fun2(func):
    def inner(*args):
        print("#"*30)
        func()
        print("#"*30)
    return inner

@decor_fun
def greeting():
    print("Good Morning")


@decor_fun2
@decor_fun
def greeting():
    print("Good Morning")

"""
##############################
******************************
Good Morning
******************************
##############################
"""


greeting()



def number_decorator(func):
    def inner(n):
        if n > 20:
            n = 20
            func(n)
        else:
            func(n)
    return inner


@decor_fun
@number_decorator
def get_even_number(n):
    for i in range(1, n):
        if i%2 == 0:
            print(i, end=" ")

"""
get_even_number(100) # 2 4 6 8 10 12 14 16 18
print()
get_even_number(15) # 2 4 6 8 10 12 14
print()
get_even_number(30) # 2 4 6 8 10 12 14 16 18
"""

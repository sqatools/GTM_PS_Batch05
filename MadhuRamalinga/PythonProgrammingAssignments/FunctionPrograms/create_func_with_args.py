# Program to create a function with *args as parameters

"""
What is *args?
*args allows us to pass a variable number of non-keyword arguments to a Python function.

What is Function?
It is a block of code that executes when it is called.
To create a function use def keyword.

"""

def func(*args):
    for num in args:
        print(num**3, end=" ") # 1 125 27 64

func(1, 5, 3, 4)
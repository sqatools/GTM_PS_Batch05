# Program to execute a string containing Python code

'''

String: A string is any series of characters that are interpreted literally by a script. For example, “Python”.

What is Function?
It is a block of code that executes when it is called.
To create a function use def keyword.

'''

mycode = 'print("Python")'
code = """
def multiply(x,y):
    return x*y

print('sqatools')
"""

exec(mycode)
exec(code)

# Python
# sqatools
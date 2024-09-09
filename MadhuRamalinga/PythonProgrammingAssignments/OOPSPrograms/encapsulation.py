# Program to show encapsulation in python

class MyClass:
    def __init__(self):
        self.__private_var = 25
    def __private_method(self):
        print("Private method")
    def public_method(self):
        self.__private_method()

obj = MyClass()
obj.public_method()
print(obj._MyClass__private_var)

# Private method
# 25

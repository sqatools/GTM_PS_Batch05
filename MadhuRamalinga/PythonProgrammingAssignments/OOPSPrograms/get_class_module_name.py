# Program to create Python class to get class and module name

class MyClass:
    pass

obj = MyClass()
print("Class name:", obj.__class__.__name__)
print("Module name:", obj.__module__)

# Class name: MyClass
# Module name: __main__
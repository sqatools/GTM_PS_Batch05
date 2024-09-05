# Program to create a class with method overloading in Python

class MyClass:
    def method(self, param1, param2 = None):
        if param2 is None:
            print("Single parameter:", param1)
        else:
            print("Two parameters:", param1, param2)

obj = MyClass()

obj.method("Hello")
obj.method("Hello", "World")

# Single parameter: Hello
# Two parameters: Hello World
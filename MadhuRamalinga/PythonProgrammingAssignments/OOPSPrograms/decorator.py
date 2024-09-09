# Program to create a class with property decorator in Python

class MyClass:
    def __init__(self):
        self._my_property = None
    @property
    def my_property(self):
        return self._my_property
    @my_property.setter
    def my_property(self, value):
        self._my_property = value

obj = MyClass()
obj.my_property = "Hello"
print(obj.my_property)

# Hello
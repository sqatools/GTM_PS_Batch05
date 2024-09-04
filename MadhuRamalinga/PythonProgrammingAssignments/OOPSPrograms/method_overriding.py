# Program to show method overriding in Python

class ParentClass:
    def parent_method(self):
        print("Parent method")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Child method (overrides parent)")

obj = ChildClass()
obj.parent_method()

# Child method (overrides parent)
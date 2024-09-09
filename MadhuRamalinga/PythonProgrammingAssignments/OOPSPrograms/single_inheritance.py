# Program to create a class with single inheritance in Python

class ParentClass:
    def parent_method(self):
        print("Parent method")

class ChildClass(ParentClass):
    def child_method(self):
        print("Child method")

obj = ChildClass()
obj.parent_method()
obj.child_method()

# Parent method
# Child method
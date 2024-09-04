# Program to create a class with multiple inheritance in Python

class ParentClass1:
    def parent_method1(self):
        print("Parent method 1")

class ParentClass2:
    def parent_method2(self):
        print("Parent method 2")

class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("Child method")

obj = ChildClass()
obj.parent_method1()
obj.parent_method2()
obj.child_method()

# Parent method 1
# Parent method 2
# Child method
# Program to create a class with hierarchical inheritance in Python

class ParentClass():
    def parent_method(self):
        print("parent method")
class ChildClass1(ParentClass):
    def child_method1(self):
        print("Child method 1")

class ChildClass2(ParentClass):
    def child_method2(self):
        print("Child method 2")

obj1 = ChildClass1()
obj2 = ChildClass2()

obj1.parent_method()
obj1.child_method1()

obj2.parent_method()
obj2.child_method2()

# parent method
# Child method 1
# parent method
# Child method 2
# Program to create a class with multilevel inheritance in Python

class GrandParents():
    def grand_parents_method(self):
        print("Grandparents method")
class Parents(GrandParents):
    def parents_method(self):
        print("Parents method")
class Child(Parents):
    def child_method(self):
        print("Child method")

obj = Child()
obj.grand_parents_method()
obj.parents_method()
obj.child_method()

# Grandparents method
# Parents method
# Child method
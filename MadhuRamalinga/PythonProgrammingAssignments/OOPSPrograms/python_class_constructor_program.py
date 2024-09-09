# Python program to create a Python class constructor program

class MyClass:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name) #Name: Coco

obj = MyClass("Coco")
obj.display_name()
# Program to create a Python class with instance method

class MyClass():
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)

    def update_name(self, new_name):
        self.name =new_name

obj = MyClass("Coco")
obj.display_name()
obj.update_name("Snuffy")
obj.display_name()

# Name: Coco
# Name: Snuffy
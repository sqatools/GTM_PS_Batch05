# Program to write Python class under the given syntax

"""
In this Python oops program, we will write python class under syntax if __name__ == ‘__main__’.
The program demonstrates the usage of a class with a constructor and a method. It creates an object,
initializes its name attribute, and displays the name using the display_name method.
The code is enclosed in an if __name__ == '__main__': block to ensure it only runs when the script is executed directly.

"""
class MyClass:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)

if __name__ == '__main__':
    obj = MyClass("Coco")
    obj.display_name()

# Name: Coco

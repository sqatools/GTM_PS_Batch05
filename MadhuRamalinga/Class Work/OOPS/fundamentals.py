
class ABC():
    def Addition(self, num1, num2): # method
        print("Addition:", num1+num2) # Addition: 40

obj = ABC() # creating object
obj.Addition(10, 30)

################ Default Constructor ################
print("_"*50)

class xyz():
    def __init__(self): # default constructor
        print("Initialize the object") # Initialize the object

    def Subtraction(self):
        num3 = 500
        num4 = 100
        print("Subtraction:", num3-num4) # Subtraction: 400

    def Multiplication(self, a, b, c):
        multi_result = a * b * c
        print("Multiplication:", multi_result) # Multiplication: 250

    def Division(self, p, q):
        print("Division:", p//q) # Division: 3

obj1 = xyz()
obj1.Subtraction()
obj1.Multiplication(5, 10, 5)
obj1.Division(30,10)

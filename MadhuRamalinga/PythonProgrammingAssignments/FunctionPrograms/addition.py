# Python function program to add two numbers

def addition():
    a = 100
    b = 200
    result = a + b
    print("Addition od two numbers is:", result) # Addition od two numbers is: 300

addition()

########## OR ###########
print("_"*50)
def addition():
    x = 10
    y = 10
    print("x + y is:", x+y) # x + y is: 20

addition()

########## OR ###########
print("_"*50)

def add(a,b):
    total = a+b
    print("Total: ", total)

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

add(num1, num2)

# Enter num1: 2
# Enter num2: 3
# Total:  5
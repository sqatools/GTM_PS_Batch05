# Program to find the maximum of three numbers.

def largest(a, b, c):
    if a > b and a > c:
        print(f"{a}  is the greatest number")
    elif b > c and b > a:
        print(f"{b}  is the greatest number")
    else:
        print(f"{c}  is the greatest number")

num1 = int(input("Enter the value of a: "))
num2 = int(input("Enter the value of b: "))
num3 = int(input("Enter the value of c: "))

largest(num1, num2, num3)

################ OR ###################

print("_" * 50)

def largest1(a,b,c):
    if a>b:
        if a>c:
            print(f"{a} is the greatest number")
    elif b>a:
        if b>c:
            print(f"{b} is the greatest number")
    else:
        print(f"{c} is the greatest number")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

largest1(num1,num2,num3)
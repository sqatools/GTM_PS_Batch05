# Python function program to print a table of a number

def table():
    a = 0
    num = 5
    for i in range(1,11):
        a = i * num
        print(i, "*", num, "=", a)

table()

################## OR ###################

print("_"* 50)

def table(num1):
    b = 0
    for val in range(1,11):
        b = val * num1
        print(val, "*", num1, "=", b)
num2 = int(input("Enter the number: "))
table(num2)
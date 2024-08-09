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

# Enter the number: 5
# 1 * 5 = 5
# 2 * 5 = 10
# 3 * 5 = 15
# 4 * 5 = 20
# 5 * 5 = 25
# 6 * 5 = 30
# 7 * 5 = 35
# 8 * 5 = 40
# 9 * 5 = 45
# 10 * 5 = 50



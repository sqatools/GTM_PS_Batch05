# Get the Fibonacci series between 0 to 20

num1 = 0
num2 = 1
count = 0

while count < 10:
    print(num1, end=" ")
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    count = count + 1
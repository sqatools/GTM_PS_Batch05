# Program to get the Fibonacci series up to the given number

def fibo():
    num1 = 0
    num2 = 1
    count = 0

    while count < 10:
        print(num1, end=" ") # 0 1 1 2 3 5 8 13 21 34
        n2 = num1 + num2
        num1 = num2
        num2 = n2
        count += 1
fibo()
# Check a number is part of the Fibonacci series

fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
num = int(input("Enter a number: "))
if num in fibo:
    print("It is fibonacci series")
else:
    print("It is not a fibonacci series")
# Program to get the factorial of a given number

def fact(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    print(f"Factorial of {n}: {fact}")

n = int(input("Enter the number: "))
fact(n)

# Enter the number: 5
# Factorial of 5: 120
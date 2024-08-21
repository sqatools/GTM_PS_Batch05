# Python function program to find the HCF of two numbers

def hcf(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1

    for val in range(1, smaller+1):
        if ((num1 % val == 0) and (num2 % val == 0)):
            hcf = val

    print(f"HCF of {num1} and {num2}: {hcf}")

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

hcf(num1, num2)

# Enter num1: 4
# Enter num2: 6
# HCF of 4 and 6: 2
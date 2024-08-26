# Python function program to find the LCM of two numbers

def lcm(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while(True):
        if((greater % num1 == 0) and (greater % num2 == 0)):
            lcm = greater
            break
        greater += 1

    print(f"LCM of {num1} and {num2}: {lcm}")

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

lcm(num1, num2)

# Enter num1: 4
# Enter num2: 5
# LCM of 4 and 5: 20
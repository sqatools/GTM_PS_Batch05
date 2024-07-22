# write a python with nested if condition if its even, check number divide 4 or 8
# or if the number odd, then check the number can divide by 3 anf 7
print("_" * 50)

num1 = 10

if num1 % 2 == 0:
    print("This is even number")
    if num1 % 4 == 0 or num1 % 6 == 0:
        print("This is divisible by 4 or 6")
    else:
        print("This is not divisible by 4 or 6")

else:
    print("This is odd number")
    if num1 % 3 == 0 or num1 % 7 == 0:
        print("This is divisible by 3 or 7")
    else:
        print("This is not divisible by 3 or 7")


# python program to check given value is available in the list or not
print("_"*50)
list1 = [4, 6, 8, 2]
val1 = 5

if val1 in list1:
    print("value is available in the list")
else:
    print("value is not available in list")

# simple if condition with true or false
print("_"*40)
#p = True
p = ""

if p:
    print("P has True value")
else:
    print("P has false value")


# is not condition with if
print("_"*50)
#q = [4, 6, 7, 8]
q = None

if q is not None:
    print(q)
else:
    print("q has None value")


#############################
print("_"*50)
# write a python program to check given word is available in the string
str1 = "Hello Good Morning, Hope You are doing good"
word = "Good1"

if word in str1:
    print("Word is available in the string")
else:
    print("Word is not available in the string")

# Word is available in the string


######### write a if condition program in one single line ########
print("*"*50)
num1 = 51
result = "even" if num1%2 == 0 else "odd"
print("result :", result)


######## write a python program to create a caculator with if condition  ######
print("_"*50)

print("Please select option\n"
      "1. Addition \n"
      "2. Multiplication \n"
      "3. Subtraction \n"
      "4. Divide")

choise = int(input("Please enter your choice :"))
val1 = int(input("Please enter value 1:"))
val2 = int(input("Please enter value 2:"))

if choise == 1:
    print("addition :", val1+val2)
elif choise == 2:
    print("Multiplication :", val1*val2)
elif choise == 3:
    print("Subtraction :", val1-val2)
elif choise == 4:
    print("Division :", val1/val2)



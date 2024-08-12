# Program to multiply all the numbers in a list

def multiply():
    list1 = [2, 1, 3, 5]
    result = 1
    for val in list1:
        result *= val
    print("Multiplication of given numbers is: ", result) # 30

multiply()

############## OR #################
print("_"*50)
def multiply1(list2):
    result1 = 1
    for value in list2:
        result1 *= value
    print("Multiplication of given numbers is: ", result1) # Multiplication of given numbers is:  120

l = [3, 4, 10]
multiply1(l)
# Python function program to find the sum of all the numbers in a list

def Sum(list):
    s = 0
    for val in list:
        s += val
    print("Sum of all numbers is: ", s)

l = [2, 4, 5, 5]

Sum(l)

################## OR ###################

print("_"* 50)

def total(list1):
    t = 0
    for val in list1:
        t += val
    print("Sum of given list: ",t)

l2 = [6,9,4,5,3]
total(l2)
"""
Logical operator

> : greater than
< : less than
>= : greater than equal to
<= : less than equal to
!= : not equal

# and
cond1  and cond2
True and False : False
False and True : False
False and False : False
True and True : True

# or
cond1 or cond2
True or False : True
False or True : True
True or True : True
False or False : False
"""

print("_"*40)

# write a if condition program with and
a = 50
b = 80
c = 70

#   True and False : False
if b > a and b > c:
    print("B has greater value")
else:
    print("B doesn't have greater value")


# write a python program to check given number is divisible by 2 or 3.
print("_"*50)
num1 = 55
if num1%2 == 0 or num1%3 == 0:
    print("The number can divide by 2 or 3")
else:
    print("The number can not divide by 2 or 3")


# python program to check given number is divisible by 2 ,3 or 5
print("_"*50)
var1 = 25

if var1%2 == 0 or var1%3 == 0 and var1%5 == 0:
    print("This number can divide by 2 or 3 and 5")
else:
    print("The number can not divide by 2, 3 and 5")

"""
# Python If - elif - else condition

if cond1:
   code
elif cond2:
   code
elif cond3:
   code
elif cond4:
   code
else:
   code
"""
# write a python program to check the greater among the three different variables
print("_"*50)
"""
p = 70
q = 60
r = 70

if p > q and p > r:
    print("P has greater value :", p)
elif q >p and q > r:
    print("Q has greater value :", q)
elif r >p and r > q :
    print("R has greate value :", r)
else:
    print("None of the variable has greater value")
"""

p = 70
q = 60
r = 70


if p >= q and p >= r:
    print("P has greater value :", p)
elif q >=p and q >= r:
    print("Q has greater value :", q)
elif r >=p and r >= q :
    print("R has greate value :", r)
else:
    print("None of the variable has greater value")

# write a Python program to demonstrate grading of students as per the marks received.
print("_"*50)
#marks = int(input("Please enter value:"))
marks = 45
print(marks, type(marks))

if 30 < marks <= 40:
    print("Passed with 3rd grade")
elif 40 < marks <= 50:
    print("Passed with 2nd grade")
elif 50 < marks <= 60:
    print("Passed with 1st grade")
elif 60 < marks <= 80:
    print("Passed with A+ grade")
elif 80 < marks <= 90:
    print("Passed with A++ grade")
elif 90 < marks <= 100:
    print("Passed with Excellent grade")
elif marks <= 30:
    print("Failed in examination")
else:
    print("Marks value should between 0-100")


"""
Nested if condition

if cond1:
    code
    if cond2:
        code
        if cond3:
            code
        else:
            code
    else:
        code
else:
    code
"""
print("_"*50)
round1 = "pass"
round2 = "pass"
round3 = "pass"

if round1 == "pass":
    print("1st round is cleared")
    if round2 == "pass":
        print("2nd round is cleared")
        if round3 == "pass":
            print("congratulation you got placed")
        else:
            print("Failed in 3rd round, try next time")
    else:
        print("Failed in 2nd round try next time")

else:
    print("Failed in 1st round try nest time")






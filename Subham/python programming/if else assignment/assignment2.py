#program to check given number is divided by 3 or not
num=int(input("please enter a number:"))
if num%3==0:
    print("number divisble by 3")
else:
    print("number not divisble by 3")
#Enter a Number:15
#Given Number divided by 3

#Enter a Number:19
#Given number not divided by 3

print("_"*50)

#If else program to get all the numbers divided by 3 from 1 to 30
for i in range (1,31):
    if i%3==0:
        print (i)

print ("_"*50)


# If else program to assign grades as per total marks.
#marks > 40: Fail
#marks 40 – 50: grade C
#marks 50 – 60: grade B
#marks 60 – 70: grade A
#marks 70 – 80: grade A+
#marks 80 – 90: grade A++
#marks 90 – 100: grade Excellent
#marks > 100: Invalid marks


marks =int(input("please enter marks:"))
print(marks,type(marks))
if marks<=40:
    print("fail")
elif 40< marks <=50:
    print("passed with C garde")
elif 50< marks <=60:
    print("passed with B garde")
elif 60< marks <=70:
    print("passed with A garde")
elif 70< marks <=80:
    print("passed with A+ garde")
elif 80< marks <=90:
    print("passed with A++ garde")
elif 90< marks <=100:
    print("passed with excellent garde")
elif marks >=100:
    print ("invalid marks")

print("_"*50)

#program to check the given number divided by 3 and 5.

num = int(input("enter a number:"))
if num%3==0 and num%5==0:
    print("divided 3 and 5")
else:
    print("invalid")





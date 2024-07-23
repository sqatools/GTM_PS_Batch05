#### Check the number is divisible by 3 ####
numa = 21
if numa%3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")

#### check the numbers is dvisible by 3 between 1 to30 ####
print("_"*50)
for i in range(1,31):
    if i%3 == 0:
        print(i,end=" ")
        print()

#### If-else program to assign grades as per total marks ####
print("_"*70)
marks = 60
if marks<40:
    print("Fail")
elif marks>=40 and marks<=50:
    print("GraDe C")
elif marks>=50 and marks<=60:
    print("GraDe B")
elif marks>=60 and marks<=70:
    print("GraDe A")
elif marks>=70 and marks<=80:
    print("GraDe A+")
elif marks>=80 and marks<=90:
    print("GraDe A++")
elif marks>=90 and marks<=100:
    print("Excellent")
else:
    print("Inavlid marks")


#### Python program to check number is divided by 3 and 5 ####
print("_"*50)
numb = 15
if numb%3==0 and numb%5==0:
    print("Given number is  divided by 3 and 5")
else:
    print("Given number cant be divided by 3 and 5")

#### Python program to print the square of the number ####
print('_'*50)
var =  33
if var%11 == 0:
    print(var**2)
else:
    print("Number is not divisible by 11")

####Program to check whether the number is a prime number ####
print('_'*50)
numc = 7
count = 0
for i in range(2,numc):
    if numc%i == 0:
        count += 1
if count > 0:
    print("It is not a prime number")
else:
    print("It is a prime number")

####Program to check whether the number is odd or even ####
print('_'*50)
numd =  12
if numd%2 == 0:
   print("It is an even number")
else:
   print("It is an odd number")




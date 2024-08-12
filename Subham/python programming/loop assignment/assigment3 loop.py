for i in range(1500,2701):
        if i%7 == 0 and i%5 == 0:
            print(i, end=" ")

print("_" * 50)

for i in range(6):
    print(i* "*")
for i in range(4,-1,-1):
    print("*" *i )

print("_" * 50)

# Python Loops program to count the number of even and odd numbers from a series of numbers using

numbers = [1,2,3,4,5,6,7,8]

odd = 0
even=0

for val in numbers:
    if val%2 == 0:
        even+=1
    else:
        odd +=1

print("enter even number:", even)
print("enter odd number:", odd)

print("_" * 50)

#Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python
for i in range (0,10):
    if i != 3 or i !=6:
        print (i,end= " ")

print("_" * 50)


# Write a program to get the Fibonacci series between 0 to 20 using python.
#Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 418

num1 = 0
num2 = 1
count = 0

while count < 20:
    print(num1,end=" ")
    n2 = num1 + num2
    num1 = num2
    num2 = n2
    count += 1

print("_" * 50)

#Write a program that iterates the integers from 1 to 30 using  python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
#For numbers that are multiples of both three and five print #“FizzBuzz”.

for i in range (1,31):
    if i%3== 0 and i%5 == 0:
        print ("fizzbuzz")
    elif i%3 == 0:
        print ("fizz")

    elif i%5 == 0:
        print("fizz")


print("_" * 50)

#Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.

input1 = input("enter a word")
for char in input1:
    if char.isupper():
        print(char.lower())
    else:
        print (char)

print("_" * 50)

list_r = [4,6,2,37,1,8]
result =[]

for val in list_r:
    result.append(val**2)

print("result")
"""
list_j = [4,5,6,7,8,9,78,54,22]
even_value =[]

for val in list_j:
    if val %2==0
    even_value.append(val)

print(even_value)
"""

list= [5,6,12,45,223,56]
list.sort()
print("second highest element(list[-1])")


#list_2 = ['hello' 'python' 'subham']
#for i in list_2 :
   # reversed=  [::1]


print("_" * 50)


str2 = "hello good rning weare learning pytho programming"
x = str2.split(" ")
for i in x:
    if len(i) == 5:
        print(i)


print("_" * 50)

from pprint import pprint

  School = {
        'teacher': {
            'math': [
                {'Name': 'mohan', 'address': 'Pune', 'email': 'mohan@gmail.com'},
                {'Name': 'rahul', 'address': 'Mumbai', 'email': 'rahul@gmail.com'},
            ],
            'english': [
                {'Name': 'mohit', 'address': 'Indore', 'email': 'mohit@gmail.com'},
                {'Name': 'raghu', 'address': 'Chennai', 'email': 'raghu@gmail.com'}
            ],
            'chemistry': [
                {'Name': 'Aman', 'address': 'Pune', 'email': 'Aman@gmail.com'},
                {'Name': 'subham', 'address': 'Mumbai', 'email': 'subham@gmail.com'}
            ],
            'physics': [
                {'Name': 'madhu', 'address': 'Pune', 'email': 'madhu@gmail.com'},
                {'Name': 'shwetha', 'address': 'Mumbai', 'email': 'shwetha@gmail.com'}
            ]
        },
        'student': {
            '9th': [
                {'st_id': '9th_st_01', 'name': 'pooja', 'email': 'pooja@gmail.com', 'phone': 234567},
                {'st_id': '9th_st_02', 'name': 'megha', 'email': 'megha@gmail.com', 'phone': 76576746}
            ],
            '10th': [
                {'st_id': '10th_st_01', 'name': 'rishi', 'email': 'rishi@gmail.com', 'phone': 65476534},
                {'st_id': '10th_st_02', 'name': 'ashish', 'email': 'ashish@gmail.com', 'phone': 77775464}
            ],
            '11th': [
                {'st_id': '11th_st_01', 'name': 'amit', 'email': 'amit@gmail.com', 'phone': 76756756},
                {'st_id': '11th_st_02', 'name': 'ashish', 'email': 'amit@g

    # write a program to get specific student details with his name

    st_name = 'rishi'
    st_class = '12th'

    # first loop go through the school dict
    for k1, v1 in school.items():
        # print(k1, v1)
        if k1 == 'student':
            for k2, v2 in v1.items():
                # print(k2, v2)
                if k2 == st_class:
                    for st_data in v2:
                        # print(st_data['name'])
                        if st_name == st_data['name']:
                            print(st_data)
                else:
                    continue

    # write a python program to get teachers email id with their name



teacher_email = 'subham@gmail.com'
teacher_name = 'subham'


    for k1, v1 in teacher.items():
        if k1 == 'teacher':
            for k2, v2 in v1.items():
                if k2 == teacher_name:
                    for teacher_data in v2:
                        if teacher_email == teacher_data['email']:
                            print(teacher_data)
                else:
                    continue












































































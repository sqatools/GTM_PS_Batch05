1. program to check given number is divided by 3 or not.
# num = int(input("Please enter number :"))
# if num%3 == 0:
#     print("Number is divisible by 3")
# else:
#     print("Number is not divisible by 3")

#2. program to get all the numbers divided by 3 from 1 to 30.
# for i in range(1,31):
#     if i%3 == 0:
#         print(i, end = "")

# 3.Program to find grades of marks
# marks = int(input("Enter marks: "))
# if marks<40:
#     print("Fail")
# elif marks>=40 and marks>=50:
#     print("Grade C")
# elif marks>50 and marks<=60:
#     print("Grade B")
# elif marks>60 and marks<=70:
#     print("Grade A")
# elif marks>70 and marks<=80:
#     print("Grade A+")
# elif marks>80 and marks<=90:
#     print("Grade A++")
# elif marks>90 and marks<=100:
#     print("Excellent")
# else:
#     print("Invalid marks")

# 4.program  to find marks based on stream
# marks = int(input("Enter marks: "))
# if 85 <= marks <101:
#     print("Stream alloted: Science")
# elif 70 <= marks < 85:
#     print("Stream alloted: Commerce")
# elif 35 <= marks < 70:
#     print("Arts")
# elif 0 < marks < 35:
#     print("Stream alloted: Fail")
# else:
#     print("Invalid marks")
#
# 5.program to find temperature in fahrenhet
# temp = int(input("Enter temperature of water in Fahrenheit: "))
# if temp != 212:
#     print("Water is not boiling")
# else:
#     print("Water is boiling")

# 6.program to check whether the citizen is a senior citizen or not
# age = int(input("Enter age of a citizen: "))
#
# if age > 60:
#     print("The given citizen is a senior citizen")
# else:
#     print("The given citizen is not a senior citizen")

# 7.program to accept the city name and display its monuments (take Pune and Mumbai as cities).
# city = input("Enter city name: ").lower()
#
# if city == "pune":
#     print("Shaniwar vada\nLal mahal\nSinhgad fort")
# elif city == "mumbai":
#     print("Getway of India\nGandhi statue\nAjanta cave")
# else:
#     print("Invalid city")

# 8.program to create 10 groups of numbers between 1-100 and find out given input belongs to which group using python nested if else statements.
# num = int(input("Enter a number: "))
# if 1<= num <=10:
#     print("The given number belongs to 1st group")
# elif 11<= num <=20:
#     print("The given number belongs to 2nd group")
# elif 21<= num <=30:
#     print("The given number belongs to 3rd group")
# elif 31<= num <=40:
#     print("The given number belongs to 4th group")
# elif 41<= num <=50:
#     print("The given number belongs to 5th group")
# elif 51<= num <=60:
#     print("The given number belongs to 6th group")
# elif 61<= num <=70:
#     print("The given number belongs to 7th group")
# elif 71<= num <=80:
#     print("The given number belongs to 8th group")
# elif 81<= num <=90:
#     print("The given number belongs to 9th group")
# elif 91<= num <=100:
#     print("The given number belongs to 10th group")
# else:
#      print("Invalid number")

# 9.program to check whether the given number is an integer or not.
# num1 = 54
# if type(num1) == int:
#     print("True")
# else:
#     print("False")

# 10.program to check whether number is float or not
# num1 = 12.6
# if type(num1) == float:
#     print("True")
# else:
#     print("False")

# 11.program to print all the numbers from 10-15 except 13
# for i in range(10,16):
#     if i!=12:
#         print(i)

# 12.program to print the largest number from two numbers.
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
#
# if num1>num2:
#     print(f"{num1} is greatest")
# else:
#     print(f"{num2} is greatest")

# 13.program to check whether the given number is positive or negative and even or odd.
# num = int(input("Enter a number: "))
# if num>0:
#     if num%2 == 0:
#         print("The given number is positive and even")
#     else:
#         print("The given number is positive and odd")
# else:
#     if num%2 == 0:
#         print("The given number is negative and even")
#     else:
#         print("The given number is negative and odd")

# 14.program to check whether any given number is a palindrome.
# num1 = 121
# num2 = str(num1)
#
# if num1 == int(num2[::-1]):
#     print("It is a palindrome number")
# else:
#     print("It is not a palindrome number")

# # 15.program to check person eligible for vote or not
# age = int(input("Enter age: "))
#
# if age >= 18:
#     print("You are eligible")
# else:
#     print("You are not eligible")

# 16.program to describe the interview process
# round1 = input("Enter round1 result:")
# round2 = input("Enter round2 result:")
#
# if round1 == "passed":
#     print("Congrats your 1st round is clear")
#     if round2 == "passed":
#         print("Congrats 2nd round is clear, you are placed")
#     else:
#         print("Failed in 2nd round, please try next time")
# else:
#     print("Failed in 1st round, please try next time")

# 17.program to check whether a given character is uppercase or not
# char = input("Enter a character: ")
# if char.isupper():
#     print("True")
# else:
#     print("False")

# # 18.program to check whether the given character is lowercase or not.
# char = input("Enter a character: ")
#
# if char.islower():
#     print("True")
# else:
#     print("False")
# 19.  program to check authentication with the given username and password
# name = input("Enter name: ")
# password = input("Enter password: ")
# # Authenticate username and password
# if name == password:
# # Print output
#     print("It is valid")
# else:
# # Print output
#     print("It is not valid")
# 20. program to validate user_id in the list of user_ids
# id_list = [1,2,3,5,6,7,8]
# id_ = int(input("Enter ID number: "))
# if id_ in id_list:
#     print("Valid ID")
# else:
#     print("Invalid ID")
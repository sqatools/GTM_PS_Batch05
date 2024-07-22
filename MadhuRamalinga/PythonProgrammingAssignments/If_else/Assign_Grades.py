'''
Condition for grades:
Marks less than 40: Fail
Marks between 40-50: Grade C
Marks between 51-60: Grade B
Marks between 61-70: Grade A
Marks between 71-80: Grade A+
Marks between 81-90: Grade A++
Marks between 91-100: Excellent
'''

marks = int(input("Enter the marks: "))
if marks < 40:
    print("Failed")
# elif marks >= 40 and marks <= 50:
elif marks <= 50:
    print("Grade C")
elif marks > 50 and marks <= 60:
    print("Grade B")
elif marks > 60 and marks <= 70:
    print("Grade A")
elif marks > 70 and marks <= 80:
    print("Grade A+")
elif marks > 80 and marks <= 90:
    print("Grade A++")
elif marks > 90 and marks <= 100:
    print("Excellent")
else:
    print("Please enter the marks between 0 to 100")
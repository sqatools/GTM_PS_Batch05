"""
Properties
-> string is immutable data type
-> string can be defined in single/double/triple quotes.
-> string follows the positive negative indexing
->
"""
Name = "Rahul"
Age = 25
City = "Mumbai"
email = "rahul@ggmail.com"

# My name is Rahul and my age is 25 and living in mumbai

# 1. String concatenation

result = "My name is "+Name+" and my age is "+str(Age)+" and living in "+City
print(result)

# 2.  Format method
result2 =  "My name is {} and my age is {} and living in {}".format(Name, Age, City)
print("result2 :", result2)

# 3. F string formatting
result3 = f"My name is {Name} and my age is {Age}, {email} and living in {City}"
print("result3 :", result3)

print("_"*50)


# raw string

str2 = 'Hello Good Morning \n Hope you are doing "good" \t\t, Python Programming'
print(str2)

str3 = r"Hello Good Morning \n 'Hope you are doing good' \t\t, Python Programming"
print("str3 :", str3)

# Apply loop on the string
print("_"*50)

str4 = "Python Programming"
for char in str4:
    print(char)

# Apply loop with index position
print("_"*50)
str5 = "Good Morning"
len_str = len(str5)

for i in range(len_str):
    print(i,":", str5[i])

print("_"*50)
############  String Slicing ############
# Rule 1: str[initial index: last index]
# output will include initial index char and exclude last index character
# Output substring always get the output from left to right

str_a = "Good Morning"
output = str_a[0:8]
print("output :", output)
# with negative indexing
print(str_a[2: -2])  # od Morni

# as per the rule output can not contain char from negative to positive index
print(str_a[-1: 2]) # Noi output

str_b = "Python Programming"
print(str_b[4:8])  # on P
print(str_b[2:-5]) # thon Progra
print(str_b[-8: -2]) # grammi
print(str_b[7:-13]) # No output

####################
# Rule2
# i) str[:last index]
# default initial index is zero

# ii) str[initial index :]
# default last index will be end of the string

str_c = "Learning is Fun"
print(str_c[:5]) # Learn

print(str_c[:-2]) # Learning is F

print(str_c[:8]) # Learning

#ii) default end index would be end of the string

str_d = "Good Evening"
print(str_d[3:])  # d Evening
print(str_d[-5:]) # ening

print("_"*40)
##############
# Rule3 : str1[initial index: end index: difference]

str1 = "We Are Learning Python"

print(str1[3 :10: 1])  # Are Lea

print(str1[1:12:2])  # eAeLan

# get values with negative indexing
print(str1[-1:-10:-1])  # nohtyP gn

print(str1[4:-2:1]) # re Learning Pyth

##################
# Rule3: str1[:last index: difference]
# the default initial index would be zero if difference is positive
# The default initial index would be -1 if the difference is negative.


str_b = "Python is very to learn"
print(str_b[:-5:1])  # Python is very to
print(str_b[:-15:-2]) # nrae


# Rule4 :
print(str_b[::-1]) # str1[:: difference]
# default initial index would be zero
# default last index would end of the string.


str_c= "Good Morning"
print(str_c[2: 15])

print(str_c[::-1])
print(str_c[-1:-len(str_c)-1: -1])

print("_"*50)
# Q1:
str1 = "Best player is Virat"
# output = "Virat is best player"

w1 = str1[:12]
w2 = str1[12:14]
w3 = str1[15:]

print(f"{w3} {w2} {w1}")  # Virat is Best player

#Q2:
str1 = "India is Best Cricket Team"
# output = "mndia is Best Cricket TeaI"

first_char = str1[0]
last_char = str1[-1]
remaining_chars = str1[1:-1]

print(f"{last_char}{remaining_chars}{first_char}")























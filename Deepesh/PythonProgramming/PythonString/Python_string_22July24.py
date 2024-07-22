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





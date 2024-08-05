print(dir(str))
"""
'capitalize', 'casefold', 'center', 'count',
'encode', 'endswith', 'expandtabs', 'find', 
'format', 'format_map', 'index', 'isalnum',
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 
 'isidentifier', 'islower', 'isnumeric',
  'isprintable', 'isspace', 'istitle',
   'isupper', 'join', 'ljust', 'lower', 
   'lstrip', 'maketrans', 'partition',
    'removeprefix', 'removesuffix',
     'replace', 'rfind', 'rindex',
      'rjust', 'rpartition', 'rsplit', 
      'rstrip', 'split', 'splitlines', 'startswith', 
      'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

"""

str1 = "We Are Learning Python Programming"

#########
# upper() and lower method:
print("upper case : ", str1.upper()) # WE ARE LEARNING PYTHON PROGRAMMING
print("lower case : ", str1.lower()) #  we are learning python programming

########
# swapcase() method: This method convert lower case to upper and upper case to lower.
print("swapcase result :", str1.swapcase()) # wE aRE lEARNING pYTHON pROGRAMMING

str_2 = "Python"
print(str_2[2].upper()) # T
print(str_2[:3].upper()) # PYT

##########
print("_"*40)
# isupper() and islower() method.
# isupper method : This method return true if all characters are in upper case
# islower method : This method return true if all the characters in lower case.
str_a = "PYTHON"
str_b = "python"

print("str_a:", str_a.isupper(), str_a.islower())  # True , False
print("str_b:", str_b.isupper(), str_b.islower())  # False, True

##########
print("_"*50)
# title method(): This method convert first character each word in string to upper case.
str_c = "Hello good morning"
print("title case :", str_c.title())  # Hello Good Morning

# istitle method(): This method check the given string is in title case or not.
str_d = "Python Learning Is Fun"
str_e = "Programming language"

print("str_d :", str_d.istitle()) # True
print("str_e :", str_e.istitle()) # False

########
print("_"*50)
# split() method: Split method , split the string in list of substring from given delimeters.

str_f = "Python is Easy to Learn"
str_g = "Python,is,Easy,to,Learn"
str_h = "Good#Morning@Hope@You@are@good"

# split from space
print("space split result :", str_f.split(" ")) # ['Python', 'is', 'Easy', 'to', 'Learn']

# split from comma
print("split from comma :", str_g.split(",")) # ['Python', 'is', 'Easy', 'to', 'Learn']

#split from special character
print("split from special characters :", str_h.split("@")) # ['Good#Morning', 'Hope', 'You', 'are', 'good']

result = str_h.split("@")[0].split("#")[1] # Morning
print("result :", result)

###########
print("_"*50)
# replace() method: This method replace any given string from target string.

str_j = "Good#Morning@Hope@You@are@good"
result = str_j.replace("@", " ")
print("Replace result : ", result) # Good#Morning Hope You are good

result2 = result.replace("#", " ")
print("result2 :", result2) # Good Morning Hope You are good

result3 = str_j.replace("@", " ").replace("#", " ")
print("result3 :", result3)


###########
print("_"*40)
# join() method: This method join any given string with delimeters.
str_l = "Python"

result = "-".join(str_l)
print("result :", result) # P-y-t-h-o-n

str_z = "Hello%good%morning%Hope%you%enjoy%learning"
word_list = str_z.split("%")
print("word list :", word_list)

str_result = " ".join(word_list)
print("str_result :", str_result) # Hello good morning Hope you enjoy learning

list2 = ['a', 'b', 'c']
print("".join(list2)) # abc

##############################
print("_"*40)
# write a python program to get longest word in the given string.

str_x = "Dipawali is best holifestival in India we_celebrate_that_with_full_of_joy"
word_list = str_x.split(" ")
print(word_list)
#                             max_len_w
# ['Dipawali', 'is', 'best', 'holifestival', 'in', 'India']

max_len_word = word_list[0] # dipawali, holifestival

for word in word_list:
    if len(word) > len(max_len_word):
        max_len_word = word
    else:
        continue

print("longest_word :", max_len_word)  # we_celebrate_that_with_full_of_joy

print("_"*50)
## write a python program to remove duplicate word from given string
str_y = "Akash Manish Akshay Manish Akshay Rahul"
#output = "Akash Manish Akshay Rahul"

# print(" ".join(list(set(str_y.split(" ")))))  # Rahul Akash Manish Akshay

result = ""
word_list = str_y.split(" ")

for word in word_list:
    if word not in result:
        result = result + word + " "
    else:
        continue

print("Result :", result)
# Result : Akash Manish Akshay Rahul








from dateutil.parser import _resultbase

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
#####
#strip() method : This method remove trailing spaces from given string

str1 = "  Python Programming  "
print(str1)

result = str1.strip()
print(result)

str2 = "  Good Morning"
print(str2.strip())

print("_"*40)
# lstip() method : this will remove the left side space from given string
str_a = "  Good Evening  "
print(str_a)
print(str_a.lstrip())

# rtrip() method : this will remove the right side space from given string
print(str_a.rstrip())


# Remove spaces from good
str_b = "   G o o d Afternoon  "
result2 = str_b.strip()
print(result2)
word1 = result2[:7].replace(" ", "")
word2 = result2[8:]
print(" ".join([word1, word2])) # Good Afternoon
print(word1 + " " + word2) # Good Afternoon

print("_"*50)
###############
# count() method : this method return the count of specific char/substring in the given string

str_c = "Hello We are learning Python Programming"

print("count of o :", str_c.count('o'))  # count of o : 3
print("count of g :", str_c.count('g'))  # count of g : 3

temp = "" # Helo
for char in str_c: # Hello
    if char not in temp:
        print(char, str_c.count(char))
        temp = temp + char
    else:
        continue

print("_"*50)
######
# index() method : This method return the index position of any char/substring

str_d = "Today is rainy day"
print("index position of r :", str_d.index("r"))

print("rindex method get index of a :", str_d.rindex("a"))
# index position of r : 9

# check the char, which does not exist in the string
# print(str_d.index("W"))
#ValueError: substring not found

print("_"*50)
#######
# find() method: This method return the index position of any char or substring, if it is available in the given string.
#              If it is not available, then it will return -1

str_e = "India is best cricket team"
print("index of b :", str_e.find("b"))  # index of b : 9

print("index of W :", str_e.find("W"))  # -1, got result as -1, as this character is not available in the target string.

# get index position of all the characters.
for i in range(len(str_e)):
    print(i, ":", str_e[i])

print("_"*50)
##############################
# str.isalnum(): this method return True if string contains alphabate and numbers

str_j = "Good 567"
str_k = "Good567"
print("check is alphanum() :", str_j.isalnum()) # False
print("check is alphanum() :", str_k.isalnum()) # True

#########
# str.isalpha() method : This method check the given string is only contains alphabets
str_l = "Program"
print("check of isalpha :", str_l.isalpha()) # True

######
# str.isnumeric() method : This method check the given string only contains numeric values.
str_w = "45433645"
print("check string only contains number s:", str_w.isnumeric()) # True

########
# str.isspace() : this method return if given string only contains space

str_r = "Good Morning"
str_y = "    "
print("check for isspace :", str_r.isspace()) # False
print("check for isspace :", str_y.isspace()) # True


for char in str_r:
    print(char, char.isspace())


#Q1 write a python program to get all the word whose length is 5
str2 = "Hello Good rning , WeAre Learning Pytho Programming"
# output = "Hello rning WeAre Pytho"
output= "" # "Hello rning WeAre "
word_list = str2.split(" ")
for word in word_list:
    if len(word) == 5:
        output = output + word + " "
    else:
        continue

print("result :", output)



#Q2 write a python program to find the odd and even length words, and arrange them respectively
# even word come first then odd len word.
str_3 = "Good Morning , Hope you doing good"
#output = "good Hope Good Morning you doing"

odd_word = ""
even_word = ""
word_list = str_3.split(" ")
for word in word_list:
    if len(word)%2 == 0:
        even_word = even_word + word + " "
    else:
        odd_word = odd_word + word + " "

print(even_word + odd_word)

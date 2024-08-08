#Q1: My name is shreyas and my ages is 32 and living in delhi

Name="Shreyas"
Age= "32"
City= "delhi"

#string concatenation
#result= My name+"Name+" and my age is "+age+"and living in "+city+"
#print("result")

#Format Mrethod
#result2= "My name is{} and my age{} and living in{}".format(Name,age,city)
#print("result: ", result2)

#Q2:Write a Python program to get a string made of the first and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string

#string = "sqatools"

#if len(string) < 2:
#    print(True)
#else:
#    print(string[:2]+string[-2:])

#Q3:Python string program that takes a list of strings and returns the length of the longest string.

#string= ["i","am","learning","python","language"]

#temp=0
#for word in string:
#    a=len(word)
#    if a>temp:
#        temp = a
#        print(temp)----------Doubt output


#Q3:String made of 4 copies of last 2 characters
#string='saqtool'

#print(string[-2:]*4)

#Q4:Reverse a string if its length is multiple of 4

#string='Sqatools'
#if len(string) % 4==0:
#    print(string[::-1])

#Q5:Count occurrences of a substring in a string.

#string="pythoneasylanguage"

#sub= "a"
#string.count("a")---------doubt

#Q6:The passed letter is a vowel or consonant

#letter= "aeiousmvy"
#for char in letter:
#    if char =='a' or char =='e' or char =='i' or char=='o'or char =='s' or char =='s' :

#        print(f"{char}is vowel")
#    else:
#        print(f"{char}is consonat")-----------doubt in output

#Q7:find Longest and smallest word in the input string

#string = "python is easy language"

#list_1 = string.split(" ")
#print("longest word:",max(list_1,key=len))
#print("Smallest word:",min(list_1,key=len))

#Q8:Most simultaneously repeated character in string.

#Input string
#str1 = "Helllllo ffdfdas sdfsfsd sssfdddd"
#max_repeat_count = 0
#max_repeat_char = ''

#temp = 1
#for i in range(len(str1)-1):
#    if str1[i] == str1[i+1]:
#        temp = temp + 1
#        if temp > max_repeat_count:
#            max_repeat_count = temp
#            max_repeat_char = str1[i]
#    else:
#        temp = 1

#print("Max repeated char :", max_repeat_char,"\nMax repeated count :", max_repeat_count)--------Need to discus

#Q9:Calculate the length of a string with loop logic

#string="learning python language is fun"
#count=0

#for char in string:
#    count +=1
#    print("Length of the string using loop logic: ", count)
#    print("Length of the string using len(): ", len(string))

#Q10:Write a Python program to replace the second occurrence of any char with the special character $.
#Input = “Programming”
#utput = “Prog$am$in$”

#Input string
#str1 = "Programming"
#esult = ''

#for char in str1:
#    if char in result:
#        result = result + "$"
#    else:
#        result = result + char

#print("Result :", result)
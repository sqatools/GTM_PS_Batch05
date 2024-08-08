#Q2 write a python program to find the odd and even length words, and arrange them respectively
# even word come first then odd len word.
str_3 = "Good Morning , Hope you doing good"
#output = Good Hope good Morning , you doing
odd_word = ""
even_word = ""
word_list = str_3.split(" ")
for i in word_list:
    if len(i)%2 == 0:
        even_word = even_word + i + " "
    else:
        odd_word = odd_word + i + " "

print(even_word + odd_word)



#Q1 write a python program to get all the word whose length is 5
str2 = "Hello Good rning, WeAre Learning Pytho Programming"
output = ""
#output = "Hello rning WeAre Pytho"
resultL = str2.split(" ")
for i in resultL:
    if len(i) == 5:
        output = output + i + " "
    else:
        continue

print("resultL :", output)
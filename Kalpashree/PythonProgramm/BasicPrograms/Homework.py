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

# Q2 Write a python program to find out the second highest number from list#
list_q = [3,6,12,45,223,56]
result_q = list_q.sort(reverse=True)
print("Second highet:",list_q[1])

## square of all values
print('_'*50)
list1 = [4,6,8,10]
#result_s =[]
for val in range(len(list1)):
#result_s.append(val**2)
    list1[val] = list1[val]**2
print(list1)

#print("square of all values:",result_s)

## List Comperhension
print('_'*50)
result2 = [val**2 for val in list1]
print("square of all values:",result2)


##Nested for loop ##
print('_'*50)
result3 = [(x,y) for x in range(4) for y in ['p','q','r','s']]
print("result3:", result3)

### list all even numbers
print('_'*50)
list4 = [4,5,6,8,3,7]
even_value =[]
for val in list4:
    if val%2==0:
        even_value.append(val)

print("even values:", even_value)

## Q1 : Write a python program to change reverse each values in given list
list_r= ['Hello', 'Python', 'Programs']
# output = ['olleH', 'nohtyP', 'smargorP']
outp = []
for i in list_r:
    print(i[::-1])



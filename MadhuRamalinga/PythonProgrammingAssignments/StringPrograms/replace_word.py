# Replace the words in the given string

str1 = "I like Java programming"
list1 = str1.split()

for word in list1:
    if word == 'Java':
        index = list1.index(word)
        list1[index] = 'Python'
print(list1)        
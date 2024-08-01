# Exchange first and last character of each word

str1 = "python programming"
list1 = str1.split(" ") # ['python', 'programming']

for word in list1:
    new_word = word[-1] +  word[1:-1] + word[0]
    # nythop
    # grogramminp

    index = list1.index(word) #Finding index of the word
    list1[index] = new_word   #Replacing the word with new word

output = " ".join(list1)
print("Exchange of first and last characters of each word is:", output) # nythop grogramminp





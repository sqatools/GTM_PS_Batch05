"""
#Q2 write a python program to find the odd and even length words, and arrange them respectively
# even word come first then odd len word.
str_3 = "Good Morning , Hope you doing good"
output = "good Hope Good Morning you doing"
"""
str_3 = "Good Morning , Hope you doing good"
str_3 = str_3.replace(",","") # Good Morning  Hope you doing good

words = str_3.split() # ['Good', 'Morning', 'Hope', 'you', 'doing', 'good']
even_words = []
odd_words = []

for word in words:
    if len(word) % 2 == 0:
         even_words.append(word)
    else:
        odd_words.append(word)

output1 = " ".join(even_words)
output2 = " ".join(odd_words)
print(output1+" "+output2)
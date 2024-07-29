"""
Q1 write a python program to get all the word whose length is 5
str2 = "Hello Good rning, WeAre Learning Pytho Programming"
output = "Hello rning WeAre Pytho"
"""

str2 = "Hello Good rning, WeAre Learning Pytho Programming"
str2 = str2.replace(",","") # Hello Good rning WeAre Learning Pytho Programming

words = str2.split() # ['Hello', 'Good', 'rning', 'WeAre', 'Learning', 'Pytho', 'Programming']

words_with_length_5 = []

for word in words:
    if len(word) == 5:
        words_with_length_5.append(word)
"""['Hello']
['Hello', 'rning']
['Hello', 'rning', 'WeAre']
['Hello', 'rning', 'WeAre', 'Pytho'] """

output = " ".join(words_with_length_5)
print(output)
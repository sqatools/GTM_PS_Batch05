# Vowels in each word of string show as dictionary

str1 = "I like python programming"
list1 = str1.split() # ['I', 'like', 'python', 'programming']

vowels = 'aeiouAEIOU'
dictionary = dict()

for word in list1:
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    dictionary[word] = count

print(dictionary) # {'I': 1, 'like': 2, 'python': 1, 'programming': 3}


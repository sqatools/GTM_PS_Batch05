# Longest and smallest word in the input string

str1 = "I like Python Programming"
list1 = str1.split() # ['I', 'like', 'Python', 'Programming']
print("Longest word in the given string is: ", max(list1, key = len)) # Programming
print("Smallest word in the given string is: ", min(list1, key = len)) # I


######################### OR #########################
print("_"*50)

str2 = "I like Python Programming"
list2 = str2.split() # ['I', 'like', 'Python', 'Programming']
longest_word = ''
smallest_word = ''
for word in list2:
    if len(word) > len(longest_word):
        longest_word = word
    if len(word) < len(smallest_word):
        smallest_word = word
print("Longest word in the given string is: ", longest_word) # Programming
print("Smallest word in the given string is: ", smallest_word)
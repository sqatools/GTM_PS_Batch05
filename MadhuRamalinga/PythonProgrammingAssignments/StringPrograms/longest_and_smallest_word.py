# Longest and smallest word in the input string

str1 = "I like Python Programming"
list1 = str1.split() # ['I', 'like', 'Python', 'Programming']
print("Longest word in the given string is: ", max(list1, key = len)) # Programming
print("Smallest word in the given string is: ", min(list1, key = len)) # I
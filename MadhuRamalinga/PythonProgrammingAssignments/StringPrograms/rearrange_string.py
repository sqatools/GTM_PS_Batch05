# Re-arrange the string

str1 = "Cricket Plays Virat"
list1 = str1.split(" ") # ['Cricket', 'Plays', 'Virat']

list1.reverse()
output = ' '.join(list1)
print(output) # Virat Plays Cricket

# Remove duplicate words from the string

str1 = "I like like python programming"
list1 = str1.split()
list2 = []

for word in list1:
    if word not in list2:
        list2.append(word)

output = " ".join(list2)
print(output) # I like python programming





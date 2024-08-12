# Program to print the list in reverse order using for loop

list1 = [1, 8, 5, 4, 2]

print("Reverse values are:", list1[::-1]) # Reverse values are: [2, 4, 5, 8, 1]

##########Using Loop###########

list2 = [1, 10, 18, 5, 4]

for val in range(len(list1)-1,-1,-1):
    print(list2[val], end=" ") # 4 5 18 10 1
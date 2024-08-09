# Program to print the list in reverse order using while loop

list1 = [10, 5, 1, 4, 8]
count = len(list1)-1

while count >= 0:
    print(list1[count], end=" ") # 8 4 1 5 10
    count -= 1
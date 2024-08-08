# Q2 Write a python program to find out the second highest number from list
# list1 = [3, 6, 12, 45, 223, 56]
# output = 56

list1 = [3, 6, 12, 45, 223, 56]
first_highest = max(list1) # 223
new_list = []
for num in list1:
    if num != first_highest:
        new_list.append(num) # [3, 6, 12, 45, 56]
second_highest = max(new_list)
print("The second highest number is:", second_highest)

# using list comprehension

list1 = [3, 6, 12, 45, 223, 56]
first_highest = max(list1)
new_list = [num for num in list1 if num != first_highest] # [3, 6, 12, 45, 56]
second_highest = max(new_list)
print("The second highest number is:", second_highest)


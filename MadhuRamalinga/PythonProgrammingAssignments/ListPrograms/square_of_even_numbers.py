# Program to print squares of even numbers from a list

list1 = [2, 4, 5, 10, 3]
new_list = []

for val in list1:
    if val % 2 == 0:
        new_list.append(val**2)
        print(val, ":", val ** 2)
        # 2 : 4
        # 4 : 16
        # 10 : 100

print("Square of even numbers are: ", new_list) # Square of even numbers are:  [4, 16, 100]

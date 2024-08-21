# Program to find the even numbers from a given list

def even(list1):
    even_list = []
    for val in list1:
        if val % 2 == 0:
            even_list.append(val)
    print(even_list) # [4, 2, 8, 10]

l = [4, 1, 3, 2, 5, 8, 10]
even(l)
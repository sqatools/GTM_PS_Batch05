# Program to take a list and returns a new list with unique elements of the first list

def unique(list1):
    new_list = []
    for value in l:
        if value not in new_list:
            new_list.append(value)
    print("Unique elements are:",new_list) # Unique elements are: [1, 4, 5, 8]

l = [1, 4, 5, 1, 5, 4, 1, 8, 5]
unique(l)

####### Using Set ##########
print("_"*50)
def unique1(list2):
    print("Unique elements are:", list(set(list2))) # Unique elements are: [100, 25, 10, 4]

l1 = [4, 4, 10, 100, 25, 4, 100, 25, 25]
unique1(l1)
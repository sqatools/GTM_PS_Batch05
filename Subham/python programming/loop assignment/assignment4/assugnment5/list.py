# Problem to add elements from list1 to list2

list1 = [1,2,5]
list2 = [2,5,8]
result = list1+list2
print(result)#[1, 2, 5, 2, 5, 8]


print("_" * 50)

# Python program to calculate the sum of all elements from a list

list3 = [10,20,30,48,66]
total =sum(list3)
print (total)#174

print("_" * 50)

#Python program to calculate the square of each number from the given list.

list_4 = [55,2,4]
for val in list_4:
    print (val,":", val**2)
#55 : 3025
#2 : 4
#4 :

print("_" * 50)

#Python program to find the minimum and maximum elements from the list.

list_2 = [65,55,4,89,1001]

list_2.sort()

print ("minimum element:",list_2[2])#65
print ("maximum element:",list_2[4])


print("_" * 50)

#Python program to differentiate even and odd elements from the given list.


list_3 = [24,2,3,9,8,7,]

even = []
odd = []

for val in list_3:
    if val%2 == 0:
        even.append(val)
    else:
        odd.append(val)

print("even number:",even)#even number: [24, 2, 8]

print("odd number:",odd)#odd number: [3, 9, 7]


print("_" * 50)


#Python program to remove all duplicate elements from the list.

list_6 = [4,4,55,55,9,8,77,77,]
list_7 = []
for val in list_6:
    if val not in (list_7):
        list_7.append(val)

print(list_7)#[4, 55, 9, 8, 77]




























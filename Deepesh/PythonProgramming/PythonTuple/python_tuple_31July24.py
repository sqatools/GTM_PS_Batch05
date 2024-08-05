tup1 = (4, 6, 8, 2, 'Hello', (4, 6, 7), [5, 1, 4])

print(tup1) # (4, 6, 8, 2, 'Hello', (4, 6, 7), [5, 1, 4])
print(tup1[4]) # Hello
print(tup1[5][2]) # 7

print(tup1[-1][::-1])  # [4, 1, 5]

print(tup1[4][::2])  # Hlo

print(tup1[1::2])  # (6, 2, (4, 6, 7))
# HHelloo

print(f"{tup1[4][0]*2}-{tup1[4][1:-1]}-{tup1[4][-1]*2}" ) # HH-ell-oo

# reverse the data in the tuple
tup2 = (3, 5, 7, 1, 8)
print("revered values :", tup2[::-1]) # (8, 1, 7, 5, 3)


################ Apply loop on tuple values ####################

tup3 = (5, 8, 9, 12, 34, 56)
for val in tup3:
    print(val)

print("_"*50)

for i in range(len(tup3)):
    print(i, tup3[i])


print("_"*50)
################ Methods in tuple ############
print(dir(tuple))

# 'count', 'index'

# Index method: This method return the index position of specific element
tup4 = ('a', 'b', 'c', 'p', 'q', 'r', 'a', 'b', 'a')
print("index position of c :", tup4.index('c')) # 2

# count method : This method number of occurences of any value
print("count of a :", tup4.count('a')) # 3

tuple5 = (4, 15, 6, 1, 7, 34, 23)
print("Max values :", max(tuple5)) # 34
print("Min value :", min(tuple5)) # 1
print("Sum of values :", sum(tuple5)) # 90

##################################################
# write a python to create dict output where first tuple is keys and second is values

tup_a = ('a', 'b', 'c', 'd')
tup_b = (123, 456, 789, 324)
dict_output = {}

for i in range(len(tup_a)):
    dict_output[tup_a[i]] = tup_b[i]

print("dict output :", dict_output)

#Q1 : Write a python program to find out all values which are prime in the given tuple values
tup1 = (4, 7, 1, 8, 21, 23, 29)
output = [7, 23, 29]

# Q2 : Write a python program to factorial of given values
tup2 = (4, 5, 3, 7)
# fact 5: 5*4*3*2*1 = 120
#output = [24, 120, 6, 729]


print("_"*50)
# write a python program to print triangle pattern
"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(6):
    for j in range(i):
        print("*", end=" ")
    print()

# ASCII value

# 65-90 : Capital Letter
# 97-122 : Small letter

print(chr(65))  # print char with ascii value

# print all alphabate in camel case

count = 65
for _ in range(26):
    print(chr(count), end=" ")
    count += 1

print()

temp = 97
for _ in range(20):
    print(chr(temp), end=" ")
    temp += 1

print(ord("A")) # 65 print ASCII value of the character



# write python program to print character triangle pattern
ascii = 65
for i in range(1, 6):
    for j in range(i):
        print(chr(ascii), end=" ")
        ascii += 1
    print()

print("_"*50)
for i in range(1, 6):
    print(chr(ascii), end=" ")
    ascii += 1

print()
# print below number pattern
"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
print("_"*50)
count = 1
for i in range(5, 0, -1): # i=5, 4, 3, 2
    #count = 1  # 1
    for j in range(i):# 0-4
        print(count,end=" ")
        #count += 1 # 1-5 |  1-4 | 1-3 | 1-2
        count += 1 # 1-5 |  6-9 | 1-3 | 1-2
    print()

print("_"*50)
#############################################

"""
* * * * * * * * *
* * * * * * * * *
* * * * * * * * *
      * * *
      * * *
      * * *
      * * *
      * * *
"""
# PART1

for i in range(1, 4):
    for j in range(1, 10):
        print("*", end=" ")
    print()

# PART2

for i in range(1, 6):
    for j in range(1, 10):
        if j >3 and j < 7:
            print("*", end=" ")
        else:
             print(" ", end=" ")
    print()


print("_"*50)
###########################################
# while executes till the specified condition is true
n = 1
while n<=10:
    print(n)
    n += 1

######### write infinite loop with while ##########
"""
print("_"*50)
temp =1
while True:
    print(temp)
    temp += 1

"""
####### concept break and continue ######
print("_"*50)
# continue
num = 1
while num<=10:
    if num >4 and num <8:
        num += 1
        continue
    print(num)
    num += 1


print("_"*50)
# break
p = 1
while p<1000:
    print(p)
    p+= 1
    if p == 100:
        break

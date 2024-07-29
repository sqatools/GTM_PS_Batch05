# write a python program for fabonacci series.

a = 1
b = 2
#    a
# 1, 2, 3, 5, 8, 13, 21 .......
#       b
a = 1
b = 2
for i in range(10):
    print(a, end=" ")
    a, b = b, a+b

# 1 2 3 5 8 13 21 34 55 89

# Q: write a python to remove all the duplicate character from string:

str_a = "Python Programming"
#output = "Python rgami"
output = ""

for char in str_a: # Python P
    #print(char)
    if char not in output:
        output += char  # Python
    else:
        continue

print(output)  # Python rgami


#153 = 1^3 + 5^3 + 3^3

# Get a string made of first and the last 2 chars
str1 = "PythonProgramming"
for char in str1:
    result1 = str1[0:2]
    result2 = str1[15:]
print(result1 + result2) # Pyng

########################### Alternate Method #############################

string = "sqatools"

#Printing output
if len(string) < 2:
    print(True)
else:
    print(string[:2]+string[-2:]) #sqls
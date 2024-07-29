#####get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string#
Str_1 = "EPOSAUDIO"
if len(Str_1) < 2:
    print(True)
else:
    print(Str_1[:2]+Str_1[-2:])

#####From list of strings, length of longest string#####
print('_'*50)
strt_2 = ["is","the","python","program"]
temp = 0
for j in strt_2:
    a = len(j)
    if a > temp:
        temp = a
print(temp)
# Python program to sort a dictionary using keys

dict1 = {'d':21,'b':53,'a':13,'c':41}

for key in sorted(dict1):
    print("%s: %s" % (key,dict1[key]))

# a: 13
# b: 53
# c: 41
# d: 21
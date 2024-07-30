list_r = [4, 5, 7, 2, 1, 9]
result = []
for val in list_r:
    result.append(val**2)

print(result)
print('-'*50)
## list comprehension
result2 = [val**2 for val in list_r]
print(result)


####### nested for loop with list comprehension

result1 = [(x, y) for x in range (3) for y in ['a', 'b', 'c']]

print (result1)

######## even values in a list

result3 = [val for val in list_r]

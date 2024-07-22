# Print all even numbers between 1 to 100

count = 2
while count <= 100:
    print(count, end=" ")
    count += 2

################### OR ##########################

print("")
print("_"*50)

for i in range(1,101):
    if i%2 == 0:
        print(i,end=" ")
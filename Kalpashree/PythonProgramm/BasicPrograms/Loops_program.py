#####Find numbers divisible by a certain number####
for i in range(14,200):
        if i%7 == 0 and i%5 == 0:
            print(i, end=" ")

#######Construct the  pattern.####
for i in range(6):
    print(i*"*")
for i in range(4,-1,-1):
    print(i*"*")
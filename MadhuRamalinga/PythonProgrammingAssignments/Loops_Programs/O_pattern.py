# Print the alphabet pattern ‘O’
for i in range(0,7):
    for j in range (0,7):
        if (i == 0 or i == 6) and (1 < j < 5):
            print("*", end="")
        elif (i == 1 or i == 5) and (j == 1 or j == 5):
            print("*", end="")
        elif (i == 2 or i == 3 or i == 4) and (j == 1 or j == 5):
            print("*", end="")
        else:
            print(" ", end="")
    print()





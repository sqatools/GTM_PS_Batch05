# Program to reverse a list with reversed and reverse methods

############## Using reversed() ###############

list1 = [1, 5, 4, 2, 8]

print("Using reversed method:", list(reversed(list1))) # Using reversed method: [8, 2, 4, 5, 1]

############## Using reverse() ###############

list2 = [10, 18, 5, 4, 6]

list2.reverse()
print("Using reverse:", list2) # Using reverse: [6, 4, 5, 18, 10]
# Determine whether a number is available in the list
list = [1, 4, 5, 8, 10]
num = int(input("Enter the number: "))
if num in list:
    print(f"{num} is available in the list")
else:
    print(f"{num} is not available in the list")
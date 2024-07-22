# Print a square or cube of the given number
num = int(input("Enter the number: "))
if num%2 == 0:
    print("Square of the number is: ", num**2)
elif num%3==0:
    print(("Cube of the number is: ",num**3))
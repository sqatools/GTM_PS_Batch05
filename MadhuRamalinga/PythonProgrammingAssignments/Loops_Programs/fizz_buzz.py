# Print Fizz Buzz for multiples of certain numbers

for i in range(1,12):
    if i%2 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%2 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")


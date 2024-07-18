#Armstrong --> 3^3 + 7^3 + 1^3 = 371

"""num = 153
temp = num
count = 0
while temp > 0:
    temp = temp // 10
    count = count + 1
temp = num
sum_of_powers = 0
while temp > 0:
    digit = temp % 10
    temp = temp // 10
    power = 1

for _ in range(count):
   power = power * digit
   sum_of_powers = sum_of_powers + power

if sum_of_powers == num:
    print(f"It is a armstrong number")
else:
    print(f"It is not a armstrong number") """

num = a = 153
rev = 0

while a>0:
    rem = a%10
    rev = rev +rem**3
    a= a//10

if rev == num:
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")


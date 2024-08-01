# Write a python program to factorial of given values
# tup2 = (4, 5, 3, 7)
# # fact 5: 5*4*3*2*1 = 120
# #output = [24, 120, 6, 729]

tup2 = (4, 5, 3, 7)
result = []

for n in tup2:
    fact = 1
    for i in range(n, 0, -1):
        fact = fact*i # 6 # 30 # 120 # 360 # 720

    result.append(fact)

print("output :", result)
a=30
b=40
print(a+b)
address=id(a)
print("address;", address)

p=6
q=7
r=8
print("address p:",id(p))
print("address q:",id(q))
print("address r:",id(r))

#
p=6
q=6
r=6


print("address p:",id(p))
print("address q:",id(q))
print("address r:",id(r))

#assign multiple variable diffrent at a time
x,y,z=4,5,6
print("value of x:",x)
print("value of y:",y)
print("value of z:",z)


#assign  same  value to diffrent variable
a=b=c=2
print("value of a:",a)
print("value of b:",b)
print("value of c:",c)


from faker import Faker


fk = Faker()
for i in range(50):

  print(fk.user_name())
  print(fk.email())
  print(fk.phone_number())
  print(fk.city)
  print("number:",i)
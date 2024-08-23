from datetime import datetime

print(datetime.now())  # 2024-08-20 20:49:06.898218

print(datetime.now().date()) # 2024-08-20

print(datetime.now().month) # 8

print(datetime.now().year) # 2024

print(datetime.now().time()) # 20:50:16.798598

print(datetime.now().day) # 20

print(datetime.now().strftime("%d_%m_%Y_%H_%M_%S")) # 20_08_2024_20_53_00

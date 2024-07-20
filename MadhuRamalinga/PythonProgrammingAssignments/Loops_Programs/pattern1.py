'''
Python program to construct the following star pattern.

   *
   * *
   * * *
   * * * *
   * * * * *
   * * * *
   * * *
   * *
   *

'''
for i in range(6):
    print(i*" *") #0, 1, 2, 3, 4, 5
for i in range(4,-1,-1):
   print(i*" *")
''' 
when i=0, 0*"*" = "" --> empty string
When i=1, 1 * "*" = "*"
When i=2, 2 * "*" = "**"
When i=3, 3 * "*" = "***"
When i=4, 4 * "*" = "****"
When i=5, 5 * "*" = "*****"
'''
# a = 2 * " *"
# print(a)
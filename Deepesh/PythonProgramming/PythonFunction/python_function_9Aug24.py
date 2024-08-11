def get_prime_number(*args):
    prime_list = []
    for n in args: # 4
        prime = True
        for i in range(2, n): # 2-7
            if n%i == 0:
                prime = False
                break

        if prime:
            #print(n)
            prime_list.append(n)

    return prime_list


#result = get_prime_number(4, 6, 8, 2, 7, 11, 19, 17, 23, 25, 28, 29)
#print("prime number list :", result)

# get square of all the prime number from previous program

def get_square_of_prime_number(*args):
    prime_numbers = get_prime_number(*args)
    square_values = [(x, x**2) for x in prime_numbers]
    return square_values


square_result = get_square_of_prime_number(5, 7, 9, 2, 15, 12, 21, 23, 27, 29, 41)
print("square result :", square_result)


print("_"*50)
# recursion in the function
def get_natural_number(n):
    print(n)
    if n == 10:
        exit()
    get_natural_number(n+1)

get_natural_number(1)

# write a python program to get all the number are polimdrome in the given values
# 121, 454, 556, 767, 812, 959

#def get_polimdrome_number(*args):


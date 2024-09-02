def greeting():
    return "Good Morning"
    return "Good Evening"
result = greeting()
print(result)              ##without generator

################################################################
################################################################

def greeting_gen():
    yield "This is Shreyas Bhokare"
    yield "Worked in product based company"
    yield "Total 2+ years experience"
    yield "Now learning selenium with python"
result_1 = greeting_gen()
print(result_1)
print(next(result_1))              #to extract generator object code used "next"

#print(next(result_1))
print("_"*40)
for val in result_1:                   #with this condition can print all the values at single time
    print(val)
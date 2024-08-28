"""
Generator helps to load one item at a time in the memory, then it is called generator.
Generator can handle millions and billions of info without crashing the memory
"""


def greeting():
    return "good morning"
    return "Good Evening"


result = greeting()
print(result)


def greeting_gen():
    yield "Good Morning"
    yield "Have a nice day"
    yield "Today is rainy day"
    yield "We are learning python"


result_2 = greeting_gen()
print(result_2)
"""
print(next(result_2))
print(next(result_2))
print(next(result_2))
print(next(result_2))
print(next(result_2)) # StopIteration
"""

for val in result_2:
    print(val)

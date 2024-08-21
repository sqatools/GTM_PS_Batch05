# Python function program to access a function inside a function

def test(a):
        def add(b):
            nonlocal a
            a += 0
            return a+b
        return add
func = test(10)
print(func(10)) # 20
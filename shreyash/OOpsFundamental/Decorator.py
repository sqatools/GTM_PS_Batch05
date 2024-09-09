#def greeting():
#    print("Good Morning")
#greeting()                    #without decorator

###########################################################

def decor_fun(func):
    def inner(*args):
        print("*"*30)
        func()
        print("*"*30)
    return inner
@decor_fun
def greeting():
    print("Good Morning")

greeting()
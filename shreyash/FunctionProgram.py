#additon of two number
#def addition():
#    num1 = 50
#    num2 = 40
#    print("addition:", num1 + num2)
#addition()

#Q2:multiplication of two numbers.

#def multiply_value(param1,param2):
#    print("value of param1:",param1)
#    print("value of param2:",param2)
#    print("multiplication of numbers:", param1*param2)
#multiply_value(7,8)

#Q3:passing by reference value
#X = 6
#Y = 6
#def multiply_value(param1,param2):
#    print("value of param1:",param1)
#    print("value of param2:",param2)
#    print("multiplication of numbers:", param1*param2)

#multiply_value(X,Y)

#Q4:Function with default parameters division of two numbers

#def function_2(P1,P2=100):
#    print("division of values:",P2/P1)
#function_2(10)

##eg:2
#def function_2(P1,P2):
#    print("division of values:",P2/P1)
#function_2(50,200)

##eg:3
#def function_3(a=100,b):
#    print("value of a and b:", a,b)

#function_3(30) #error will display

#Q5:Print square of each value

#def function_4(X,Y,Z):
#    print("sqaure of each value:",X**2,":",Y**2,":",Z**2)
#function_4(6,5,1)  #if anyone of value missing then error msg will display

#Q:6 args argument values

#def print_values(*args):
#    print("args values:", args)
#    for val in args:
#        print(val)
#print_values(6,8,12,[1,2,3],'Hello')

#Q9:Kwargs methos:login with username and password

#def login_fun(**kwargs):
#    print(kwargs)
#login_fun(Username='shreyas',Password='shreyas@123')

##eg:2
#def login_fun(**kwargs):
#    print(kwargs)
#    db_username= 'shrey'
#    db_password= 'shr123'
#    if kwargs['username']==db_username and kwargs['password']==db_password:
#        print("login succesfull")
#    else:
#        print("login failed")

#login_fun(username='shrey',password='shr123')

#Q10:combination of all param args and kawargs.
#def function_5(param1,*args,**kwargs):
#   print(f"multiply by 2:{param1}:",2*param1)
#    result=[X**2 for X in args]
#    print("square result:",result)
#    for K,V in kwargs.items():
#        print(K,":",V)

#function_5(4,2,5,6, name= 'rahul',phone=98988798,email='shr@g.com')

#Q11:Function with return statement
#factorial number

#def factorials(n):
#    fact = 1
#    for i in range(n,0,-1):
#        fact = fact * i
#        return fact
    #result = factorial(6)   #NOTE: Any code after return statement will be unreachable
    #print("factorial result:",result)

#Eg: Function that return multiple values:

#def function_three_return(n1,n2,n3):
#    add= n1 + n2
#    Multiply= n1 * n2
#    Divide = n3/n1
#    return add,Multiply,Divide
#    result_function_three_return(5,7,8)

#    print("Multiple return value:",result)

#---------
#Q12:Global Vairble:

Var_X=700     #global variable
def function1():
    var_Y=400       #local variable define inside function
    print("local variable var_Y:",var_Y)
    print("Global variable var_X:",Var_X)

def function2():
    var_z = 200   #local variable
    print("local variable var_z:",var_z)
    print("global variable Var_X:",Var_X)
function1()

function2()

#Eg2:Updating the global value

def function3():
    global var_X
    var_y = 500
    var_x = 800
    print("local variable var-y:",var_y)
    print("global variable var_x:",var_x)

def function4():
    var_z = 100
    print("local variable var_z:",var_z)
    print("global variable var_x:",var_x)
function3()
print("_"*50)
function1()
print("_"*50)
function4()
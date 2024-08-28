def try_exception_finally():

    try:
        num1 = 100
        num2 = '300'
        num4 = 500
        print("Addition:", num1 + num2 + num4)

    except Exception as e:
        print(e)

    finally:
        print("The edition operation is successful")

try_exception_finally()
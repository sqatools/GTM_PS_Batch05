def try_except_programs():
    try:
        num1 = 10
        num2 = '20'
        print("addition of values :", num1 + num2)
    except Exception as e:
        print(e)
        print("Addition of integer and string is not allowed")

    print("Good Morning")


# try_except_programs()


# Explicitly raise exception to stop the program to execute further

def try_except_programs_with_raise():
    try:
        num1 = 10
        num2 = '20'
        print("addition of values :", num1 + num2)
    except Exception as e:
        # print(e)
        print("Addition of integer and string is not allowed")
        raise

    print("Good Morning")  # This wont executes if any exception occurred


# try_except_programs_with_raise()


# try-except with else condition

def try_except_else_condition():
    try:
        num1 = 50
        num2 = 2
        print("Division of values :", num1 // num2)
    except Exception as e:
        print(e)
    else:  # else condition only executes when there is no exception.
        print("Divide operation is successful")


# try_except_else_condition()


# try-except and finally block
def try_exception_finally():
    try:
        num1 = 100
        num2 = '300'
        num4 = 5000000
        print("addition :", num1 + num2 + num4)
    except Exception as e:
        print(e)
    # finally block always going to execute, even there is exception or no exception.
    finally:
        print("The Addition  operation is successful")


# try_exception_finally()

# handle multiple exception for the operation:

def math_operations_with_multiple_exception():
    try:
        num1 = 10
        num2 = 20
        num3 = 30
        print("addition of numbers", num1 + 40)
        # assert num1 == 20
        division = num3 // 0
        print("Division error msg :", division)
    except ZeroDivisionError as e:
        print(e)
        print("Number can not divide by zero")
    except TypeError as e:
        print(e)
        print("Addition of number and string is not possible")
    except AssertionError as e:
        print(e)
        print(f"Both values are not equal, {num1}, {num2}")
    except Exception:
        raise


# math_operations_with_multiple_exception()


# nested exception handling

def nested_exception_handling():
    try:
        num1 = 50
        num2 = 70
        print("Addition of values :", num1 + num2)
        try:
            assert num1 == num2
        except Exception as e:
            print(f"Inner exception {e}")
            print("both values are not equal")

    except Exception as e:
        print(f"Outer exception : {e}")



nested_exception_handling()

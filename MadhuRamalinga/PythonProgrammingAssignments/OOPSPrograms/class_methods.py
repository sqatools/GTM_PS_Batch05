# Program to create Python class with class method

class MyClass:
    class_var = "Hello"
    @classmethod
    def class_method(abc):
        print("Class variable:", abc.class_var) # Class variable: Hello

MyClass.class_method()
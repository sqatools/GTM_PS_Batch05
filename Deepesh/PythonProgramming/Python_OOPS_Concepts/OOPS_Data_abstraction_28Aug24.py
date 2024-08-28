"""
When we do not show the internal architecture of the feature functionality, only provide the
overview about the feature then it is known as abstraction
"""
from abc import abstractmethod


class Animal:
    @abstractmethod
    def animal_voice(self):
        pass

    @abstractmethod
    def animal_bread(self):
        pass

    @abstractmethod
    def animal_age(self):
        pass


class Dog(Animal):
    def animal_voice(self):
        print("Barking")

    def animal_bread(self):
        print("Pamerian")

    def animal_age(self):
        print("The dog is 2 years old")

obj = Dog()
obj.animal_voice()


str1 ="Hello"
print(str1.upper())

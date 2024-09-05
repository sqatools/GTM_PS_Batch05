# Program to show abstract method using Python class
from abc import ABC, abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass
class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implemented abstract method")

obj = ConcreteClass()
obj.abstract_method()

# Implemented abstract method
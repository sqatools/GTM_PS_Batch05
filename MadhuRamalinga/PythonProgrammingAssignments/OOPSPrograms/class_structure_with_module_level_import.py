# Program to show class structure in Python with module-level import
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

circle_obj = Circle(10)
area = circle_obj.calculate_area()
print("Area of the circle:", area) # Area of the circle: 314.1592653589793
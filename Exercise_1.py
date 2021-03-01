# Exercise 1
# Write a Python class named Circle constructed by a radius and two methods which will
# compute the area and the perimeter of a circle. Test your code with examples.


# A=3.14*r^2
# P=3.14*r+r
# creating a class
class Circle:

    """creating a function that will calculate area and parameter of a circle"""
    def __init__(self, area, perimeter):
        self.area = area * area * 3.14
        self.perimeter = 3.14 * (perimeter + perimeter)

# adding examples:
circle_1 = Circle(3, 3)
circle_2 = Circle(2, 2)

print(circle_1.area, circle_1.perimeter)
print(circle_2.area, circle_2.perimeter)

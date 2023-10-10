import math


class Shape():
    '''This is the base class for all shapes and has the following attributes
    and methods:'''
    def __init__(self, color, name):
        '''Initializes the Shape object with the given name and color.'''
        self.color = color
        self.name = name

    def say_name(self):
        '''Prints the name of the shape'''
        return f"My name is {self.name}"


class Rectangle(Shape):
    '''The Rectangle class inherits from the Shape class and adds functionality
    specific to rectangles:'''
    def __init__(self, color, name, width, height):
        '''Initializes the Rectangle object with the given name, color, width,
        and height.'''
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self):
        '''Overrides the base class method to print the name of the rectangle
        along with its shape type ((e.g. “My name is Rei and I am a rectangle”))
        . '''
        return Shape.say_name(self) + " and I am a rectangle."


    def area(self):
        '''Calculates and returns the area of the rectangle.'''
        return self.width * self.height

    def perimeter(self):
        '''Calculates and returns the perimeter of the rectangle. '''
        return 2 * (self.width + self.height)

class Circle(Shape):
    '''The Circle class inherits from the Shape class and adds functionality
    specific to circles:'''
    def __init__(self, color, name, radius):
        '''Initializes the Circle object with the given name, color, and
        radius.'''
        super().__init__(color, name)
        self.radius = radius

    def say_name(self):
        '''Overrides the base class method to print the name of the circle
        along with its shape type (e.g. “My name is Kvothe and I am a circle”)
        .'''
        return Shape.say_name(self) + " and I am a circle."

    def area(self):
        '''Calculates and returns the area of the circle. '''
        return math.pi * self.radius * self.radius

    def perimeter(self):
        '''Calculates and returns the perimeter of the circle. '''
        return 2 * math.pi * self.radius

#!/usr/bin/python3
"""
Defines a class rectangle
"""
from models.base import Base

class Rectangle(Base):
    """Representation of a rectangle that inherits from a base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(id)
        """calling the id instance from the Base superclass"""

        self.width = width
        self.height = height
        self.x =  x
        self.y = y


    def typeChecker(self, name, value):
        """validates the type"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def value_Wid_Hei_Checker(self, name, value):
        """checks the value of height and width"""
        if value <= 0:
            raise ValueError("{}  must be > 0".format(name))


    def value_X_Y_Checker(self, name, value):
        """x and y value validation"""
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """getter width"""
        self.__width

    @width.setter
    def width(self, value):
        """width setter, gets validated"""
        self.typeChecker("width", value)
        self.value_Wid_Hei_Checker("width", value)
        self.__width = value

    @property
    def height(self):
        """getter height"""
        self.__height

    @height.setter
    def height(self, value):
        """height setter, gets validated"""
        self.typeChecker("height", value)
        self.value_Wid_Hei_Checker("height", value)
        self.__height = value

    @property
    def x(self):
        """getter x"""
        self.__x

    @x.setter
    def x(self, value):
        """x setter, gets validated"""
        self.typeChecker("x", value)
        self.value_X_Y_Checker("x", value)
        self.__x =  value

    @property
    def y(self):
        """getter y"""
        self.__y

    @y.setter
    def y(self, value):
        """y setter, gets validated"""
        self.typeChecker("y", value)
        self.value_X_Y_Checker("y", value)
        self.__y = value


    def area(self):
        """calculates area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """shows a display of #s """
        print("\n".join(("#" * self.__width) for i in range(self.__height)))

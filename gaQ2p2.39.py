""" Harold Bernie P. Garcia
DATALOG lab02
Feb. 19, 2020
I have neither received nor provided any help on this (exercice) activity,
nor have I concealed any violation of the Honor Code.
"""
from abc import abstractmethod, ABCMeta
import math

class Polygon(metaclass=ABCMeta):
    def __init__(self, side_lengths=[1, 1, 1], num_sides=3):
        self._side_lengths = side_lengths
        self._num_sizes = 3

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __repr__(self):
        return (str(self._side_lengths))


class Triangle(Polygon):
    def __init__(self, side_lengths):
        super().__init__(side_lengths, 3)
        self._perimeter = self.perimeter()
        self._area = self.area()

    def perimeter(self):
        return (sum(self._side_lengths))

    def area(self):
        s = self._perimeter / 2
        product = s
        for i in self._side_lengths:
            product *= (s - i)
        return product ** 0.5


class EquilateralTriangle(Triangle):
    def __init__(self, length):
        super().__init__([length] * 3)


t1 = Triangle([1, 2, 2])
print(t1.perimeter(), t1.area())


print(t1)

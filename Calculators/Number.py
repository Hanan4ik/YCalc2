from Functions.base_funcs import *


class Number(float):

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return add(self.value, other.value)

    def __sub__(self, other):
        return add(self.value, -other.value)

    def __mul__(self, other):
        return mul(self.value, other.value)

    def __truediv__(self, other):
        return divide(self.value, other.value)

print(sin(Number(30)))
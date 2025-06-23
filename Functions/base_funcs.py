import math


class Number(float):

    def __init__(self, value):
        self.value = value

    def __index__(self):
        return int(self.value)

    def __add__(self, other):
        if isinstance(other, Number):
            return add(self.value, other.value)
        if isinstance(other, float) or isinstance(other, int):
            return add(self.value, other)

    def __sub__(self, other):
        if isinstance(other, Number):
            return add(self.value, -other.value)
        if isinstance(other, float) or isinstance(other, int):
            return add(self.value, -other)

    def __mul__(self, other):
        if isinstance(other, Number):
            return mul(self.value, other.value)
        if isinstance(other, float) or isinstance(other, int):
            return mul(self.value, other)

    def __truediv__(self, other):
        if isinstance(other, Number):
            return divide(self.value, other.value)
        if isinstance(other, float) or isinstance(other, int):
            return divide(self.value, other)


def add(x, y):
    s_x = str(x)
    x_dot = s_x.find(".")
    s_y = str(y)
    y_dot = s_y.find(".")
    x_remain = len(s_x)-x_dot-1
    y_remain = len(s_y)-y_dot-1
    mul = 10**max(x_remain, y_remain)
    x *= mul; x = int(x)
    y *= mul; y = int(y)
    if x_dot == y_dot == -1:
        return Number((x + y)//mul)
    return Number((x + y) / mul)

def mul(x: float, y: float):
    s_x = str(x)
    x_dot = s_x.find(".")
    x_remain = 0
    if x_dot != -1:
        x_remain = len(s_x) - x_dot - 1
    s_y = str(y)
    y_remain = 0
    y_dot = s_y.find(".")
    if y_dot != -1:
        y_remain = len(s_y) - y_dot - 1

    mul_ = 10**(x_remain+y_remain)
    x = int(s_x.replace(".", ""))
    y = int(s_y.replace(".", ""))
    if x_dot == y_dot == 0:
        return Number((x * y)//mul_)
    return Number((x * y) / mul_)

def divide(x, y):  # TODO
    return x / y

if __name__ == "__main__":
    print(format(add(0.21233123121, 6)))
    print(mul(1.1213, 6.3))





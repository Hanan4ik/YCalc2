from math import *
from decimal import Decimal
# Sum of float numbers to avoid strange results
# (Add description)
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
        return (x + y)//mul
    return (x + y) / mul

def mul(x: float, y: float):
    s_x = str(x)
    x_dot = s_x.find(".")
    if x_dot == -1:
        x_dot = 0
    s_y = str(y)
    y_dot = s_y.find(".")
    if y_dot == -1:
        y_dot = 0
    x_remain = len(s_x)-x_dot-1
    y_remain = len(s_y)-y_dot-1

    mul_ = 10**(x_remain+y_remain)
    x = int(s_x.replace(".", ""))
    y = int(s_y.replace(".", ""))
    if x_dot == y_dot == 0:
        return (x * y)//mul_
    return (x * y) / mul_

def divide(x, y):
    return x / y

if __name__ == "__main__":
    print(format(add(0.21233123121, 6), ".210f"))
    print(mul(1.1213, 6))





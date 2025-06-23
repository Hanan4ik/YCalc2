from math import *

# Sum of float numbers to avoid strange results
# (Add description)
def add(x: float, y: float):
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

if __name__ == "__main__":
    print(add(123.123, -312.1234))





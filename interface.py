import sys

from Calculators import Calc

print("YCalc2")

cur_calc = Calc()

try:
    while True:
        expression = cur_calc.input()
        if expression == "chmod":
            pass
except KeyboardInterrupt:
    print("\nExiting")
    sys.exit(0)
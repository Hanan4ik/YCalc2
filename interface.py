import math
import sys
import colorama
from Calculators.Calc import Calc
import pyreadline

colorama.init()
print(colorama.Style.BRIGHT, end="")
print("YCalc2")
Calcs = [Calc(), Calc()]
chosen = 0
cur_calc = Calcs[chosen]
Calcs[1].calc_name = "calc2"


try:
    while True:
        for e in test_expressions:
            expression = cur_calc.input(e)
            if expression == "chmod":
                chosen = (chosen+1)%2
                cur_calc = Calcs[chosen]
            print(colorama.Fore.CYAN, e, " = ", expression, colorama.Fore.RESET, sep="")
        break
except KeyboardInterrupt:
    print("\nExiting")
    sys.exit(0)
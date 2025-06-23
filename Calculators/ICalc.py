from Functions.base_funcs import *


class ICalc:

    def __init__(self):
        self.calc_name = "icalc"
        self.expression = ""

    def input(self, expression):
        self.expression = expression
        if self.expression == "whatcalc":
            return self.calc_name
        elif self.expression == "help":
            return self.help()
        elif expression == "chmod":
            pass



    def help(self):
        raise NotImplementedError
from Calculators.ICalc import ICalc
from fnmatch import fnmatch
class Calc(ICalc):

    def __init__(self):
        super().__init__()


    def input(self, expression):
        super().input(expression)

        self.__format()
        self.__calculate()
        return self.result

    def __format(self) -> None:

        # Pythonize input
        self.expression = self.expression.replace(" ", "")
        self.expression = self.expression.replace("^", "**")
        self.expression = self.expression.replace(")(", ")*(")

        # Adding multiplication sign between digit and parenthesis
        i = 1
        len_exp = len(self.expression)
        while i < len_exp:
            if self.expression[i] == "(" and self.expression[i-1].isdigit():
                self.expression = self.expression[:i] + "*" + self.expression[i:]
            elif i+1 != len_exp and self.expression[i] == ")"  and self.expression[i+1].isdigit():
                self.expression = self.expression[:i+1] + "*" + self.expression[i+1:]
            else:
                i += 1
        del i, len_exp

        if "+" not in self.expression and "-" not in self.expression:
            return

        # Replace plus/minus sign into add function





    def __calculate(self):
        try:
            self.result = eval(self.expression)
        except SyntaxError:
            return "Invalid input"
        except ZeroDivisionError:
            return "Zero Division"
        except Exception:
            return "Error while calculating"




        if type(self.result) == float and self.result.as_integer_ratio()[1] == 1:
            self.result = self.result.as_integer_ratio()[0]









a = Calc()
print(a.input("(132+64) - 33*64(128/5) + 3**2 + 3"))


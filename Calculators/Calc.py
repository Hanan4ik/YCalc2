from Calculators.ICalc import ICalc
from Functions.base_funcs import *
import re


class Calc(ICalc):

    def __init__(self):
        super().__init__()

    def input(self, expression):
        super().input(expression)
        self.__format()
        return self.__calculate()

    def __format(self) -> None:

        # Pythonize input
        self.expression = self.expression.replace(" ", "")
        self.expression = self.expression.replace("^", "**")
        self.expression = self.expression.replace(")(", ")*(")

        # Adding multiplication sign between digit and parenthesis
        i = 1
        len_exp = len(self.expression)
        while i < len_exp:
            if self.expression[i] == "(" and self.expression[i - 1].isdigit():
                self.expression = self.expression[:i] + "*" + self.expression[i:]
            elif i + 1 != len_exp and self.expression[i] == ")" and self.expression[i + 1].isdigit():
                self.expression = self.expression[:i + 1] + "*" + self.expression[i + 1:]
            else:
                i += 1
        del i, len_exp

        def wrap_numbers(expression):

            number_pattern = r'\b\d+\.?\d*\b'

            wrapped_expression = re.sub(
                number_pattern,
                lambda match: f'Number({match.group(0)})',
                expression
            )

            return wrapped_expression

        self.expression = wrap_numbers(self.expression)

    def __calculate(self):
        try:
            result = eval(self.expression)
        except SyntaxError:
            return "Invalid input"
        except ZeroDivisionError:
            return "Zero Division"
        except ValueError:
            return "Error while calculating"

        if isinstance(result, float) and result.as_integer_ratio()[1] == 1:
            result = result.as_integer_ratio()[0]
        return result


a = Calc()
print(a.input("(134.312)+(123)56"))

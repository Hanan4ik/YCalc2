from Calculators.ICalc import ICalc


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
            if self.expression[i] == "(" and self.expression[i - 1].isdigit():
                self.expression = self.expression[:i] + "*" + self.expression[i:]
            elif i + 1 != len_exp and self.expression[i] == ")" and self.expression[i + 1].isdigit():
                self.expression = self.expression[:i + 1] + "*" + self.expression[i + 1:]
            else:
                i += 1
        del i, len_exp

        import re

        def wrap_numbers(expression):

            # Регулярное выражение для поиска чисел (целых и с плавающей точкой)
            number_pattern = r'\b\d+\.?\d*\b'

            # Заменяем все числа на Number(число)
            wrapped_expression = re.sub(
                number_pattern,
                lambda match: f'Number({match.group(0)})',
                expression
            )

            return wrapped_expression

        self.expression = wrap_numbers(self.expression)



    def __calculate(self):
        try:
            self.result = eval(self.expression)
        except SyntaxError:
            return "Invalid input"
        except ZeroDivisionError:
            return "Zero Division"
        except Exception:
            return "Error while calculating"

        if isinstance(self.result, float) and self.result.as_integer_ratio()[1] == 1:
            self.result = self.result.as_integer_ratio()[0]


a = Calc()
print(a.input("(132+64.31) - (-2) + 33*64(128/5) + 3**2 + 3 + sin(30)"))

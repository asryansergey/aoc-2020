from typing import List, Dict, Optional
import os

MAX_JOLTAGE_DIFF = 3


def process_input(file_name):
    with open(file_name) as report:
        return [line.strip().replace(" ", "") for line in report]


class Number:
    """ Wrapper to change operation specification. """

    def __init__(self, num):
        self.val = num

    def __add__(self, num):
        ...

    def __sub__(self, num):
        ...

    def __mul__(self, num):
        ...


def eval_expression_part_1(expr_list: List[str]) -> int:
    def add(self, num):
        return Number(self.val + num.val)

    def mul(self, num):
        return Number(self.val * num.val)

    Number.__add__ = add # type: ignore
    Number.__sub__ = mul # type: ignore

    res = 0
    for expr in expr_list:
        wrapped_str = ""
        for el in expr.replace("*", "-"):
            if el not in "(+-)":
                wrapped_str += f"Number({el})"
            else:
                wrapped_str += el
        res += eval(wrapped_str).val
    return res


def eval_expression_part_2(expr_list: List[str]) -> int:
    def mul(self, num):
        return Number(self.val * num.val)

    def add(self, num):
        return Number(self.val + num.val)

    Number.__mul__ = add # type: ignore
    Number.__sub__ = mul # type: ignore

    res = 0
    for expr in expr_list:
        wrapped_str = ""
        for el in expr.replace("*", "-").replace("+", "*"):
            if el not in "(-*)":
                wrapped_str += f"Number({el})"
            else:
                wrapped_str += el
        res += eval(wrapped_str).val
    return res


if __name__ == "__main__":
    expr_list = process_input(os.path.join("src", "day_18", "input.in"))
    print(eval_expression_part_1(expr_list))
    print(eval_expression_part_2(expr_list))

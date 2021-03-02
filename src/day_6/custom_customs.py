from typing import List, Optional
import os
from functools import reduce
import math
import itertools


def process_input(file_name):
    result = []
    with open(file_name) as report:
        return [line.replace("\n", "") for line in report.read().split("\n\n")]


def sum_of_yes_answers(answers: List[str]) -> int:
    count_sum = 0
    for line in answers:
        count_sum += len(set(line))
    return count_sum


if __name__ == "__main__":
    answers = process_input(os.path.join("src", "day_6", "input.in"))
    print(sum_of_yes_answers(answers))
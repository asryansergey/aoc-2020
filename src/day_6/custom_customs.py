from typing import List, Optional
import os
from functools import reduce
import math
import itertools


def process_input(file_name):
    result = []
    with open(file_name) as report:
        return [line.replace("\n", " ") for line in report.read().split("\n\n")]


def sum_of_yes_answers_part_1(answers: List[str]) -> int:
    count_sum = 0
    for line in answers:
        count_sum += len(set(line.replace(" ", "")))
    return count_sum


def sum_of_yes_answers_part_2(answers: List[str]) -> int:
    count_sum = 0
    for line in answers:
        set_list = [set(x) for x in line.split(" ")]
        intersection = set_list[0]
        for person_answer in set_list[1:]:
            intersection = intersection & person_answer
        count_sum += len(intersection)
    return count_sum


if __name__ == "__main__":
    answers = process_input(os.path.join("src", "day_6", "input.in"))
    print(sum_of_yes_answers_part_1(answers))
    print(sum_of_yes_answers_part_2(answers))
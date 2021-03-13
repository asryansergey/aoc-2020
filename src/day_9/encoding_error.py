from typing import List
import os


def process_input(file_name):
    with open(file_name) as report:
        return [int(line.strip()) for line in report]


def can_sum(preamble: List[int], target_num):
    ...


def find_target_number(number_list: List) -> int:
    ...


if __name__ == "__main__":
    number_list = process_input(os.path.join("src", "day_9", "input.in"))
    print(number_list)
    print(find_target_number(number_list))
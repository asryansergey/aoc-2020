from typing import List, Optional
import os

PREAMBLE_RANGE = 25


def process_input(file_name):
    with open(file_name) as report:
        return [int(line.strip()) for line in report]


def can_sum(preamble: List[int], target_num: int):
    if target_num < 0:
        return False
    if target_num == 0:
        return True
    for idx, num in enumerate(preamble, 1):
        next_num = target_num - num
        if can_sum(preamble[idx:], next_num):
            return True
    return False


def find_target_number(number_list: List) -> Optional[int]:
    for idx in range(len(number_list[:-PREAMBLE_RANGE])):
        preamble = number_list[idx : idx + PREAMBLE_RANGE]
        target_num = number_list[idx + PREAMBLE_RANGE]
        if not can_sum(preamble, target_num):
            return preamble, target_num
    return None


if __name__ == "__main__":
    number_list = process_input(os.path.join("src", "day_9", "input.in"))
    print(find_target_number(number_list))